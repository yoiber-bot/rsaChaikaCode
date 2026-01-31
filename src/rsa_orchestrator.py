"""
RSA (Recursive Self-Aggregation) Orchestrator
Main class that implements the complete RSA pipeline
"""

from typing import List, Optional
from src.gemini_client import OpenAIClient
from src.aggregation import create_groups, create_aggregation_prompt, create_final_aggregation_prompt


class RSAOrchestrator:
    """
    Orchestrates the RSA (Recursive Self-Aggregation) process
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gpt-4o",
        population_size: int = 8,
        group_size: int = 4,
        loops: int = 3,
        temperature: float = 1.0,
        verbose: bool = True
    ):
        """
        Initialize RSA Orchestrator
        
        Args:
            api_key: Google API key
            model_name: Gemini model to use
            population_size: Number of initial responses to generate
            group_size: Size of groups for aggregation (k parameter)
            loops: Number of RSA iteration rounds
            temperature: Temperature for response generation (diversity)
            verbose: Whether to print progress messages
        """
        self.client = OpenAIClient(api_key=api_key, model_name=model_name)
        self.population_size = population_size
        self.group_size = group_size
        self.loops = loops
        self.temperature = temperature
        self.verbose = verbose
        
        if self.verbose:
            print(f"🚀 RSA Orchestrator initialized:")
            print(f"   - Model: {model_name}")
            print(f"   - Population size: {population_size}")
            print(f"   - Group size: {group_size}")
            print(f"   - Loops: {loops}")
            print(f"   - Temperature: {temperature}")
    
    def _log(self, message: str):
        """Print message if verbose mode is enabled"""
        if self.verbose:
            print(message)
    
    def generate_initial_population(self, prompt: str) -> List[str]:
        """
        Generate initial population of diverse responses
        
        Args:
            prompt: User's original prompt
            
        Returns:
            List of initial responses
        """
        self._log(f"\n{'='*60}")
        self._log(f"📝 FASE 1: Generación de población inicial")
        self._log(f"{'='*60}")
        self._log(f"Generando {self.population_size} respuestas diversas...\n")
        
        responses = self.client.generate_multiple_responses(
            prompt=prompt,
            count=self.population_size,
            temperature=self.temperature,
            delay=1.0
        )
        
        self._log(f"\n✅ Población inicial generada: {len(responses)} respuestas")
        return responses
    
    def aggregate_population(self, responses: List[str], original_prompt: str, loop_num: int) -> List[str]:
        """
        Perform one round of aggregation on the population
        
        Args:
            responses: Current population of responses
            original_prompt: Original user prompt
            loop_num: Current loop number (for logging)
            
        Returns:
            New population after aggregation
        """
        self._log(f"\n{'='*60}")
        self._log(f"🔄 LOOP {loop_num}: Fase de agregación")
        self._log(f"{'='*60}")
        
        # Create groups
        groups = create_groups(responses, self.group_size)
        self._log(f"Dividiendo {len(responses)} respuestas en {len(groups)} grupos de tamaño ~{self.group_size}")
        
        # Aggregate each group
        new_population = []
        for i, group in enumerate(groups, 1):
            self._log(f"\n🔀 Agregando grupo {i}/{len(groups)} ({len(group)} respuestas)...")
            
            # Create aggregation prompt
            agg_prompt = create_aggregation_prompt(group, original_prompt)
            
            # Get aggregated response
            aggregated = self.client.generate_response(
                prompt=agg_prompt,
                temperature=0.7  # Lower temperature for aggregation
            )
            
            new_population.append(aggregated)
            self._log(f"   ✓ Grupo {i} agregado exitosamente")
        
        self._log(f"\n✅ Loop {loop_num} completado: {len(new_population)} respuestas agregadas")
        return new_population
    
    def run(self, prompt: str) -> str:
        """
        Run the complete RSA pipeline
        
        Args:
            prompt: User's original prompt/problem
            
        Returns:
            Final refined solution
        """
        self._log(f"\n{'#'*60}")
        self._log(f"🎯 INICIANDO PIPELINE RSA")
        self._log(f"{'#'*60}")
        self._log(f"\nPrompt original:\n{prompt}\n")
        
        # Step 1: Generate initial population
        population = self.generate_initial_population(prompt)
        
        # Step 2: Perform RSA loops
        for loop_num in range(1, self.loops + 1):
            population = self.aggregate_population(population, prompt, loop_num)
        
        # Step 3: Final aggregation
        self._log(f"\n{'='*60}")
        self._log(f"🏁 FASE FINAL: Consolidación")
        self._log(f"{'='*60}")
        self._log(f"Consolidando {len(population)} soluciones refinadas en solución final...")
        
        final_prompt = create_final_aggregation_prompt(population, prompt)
        final_solution = self.client.generate_response(
            prompt=final_prompt,
            temperature=0.3  # Low temperature for final refinement
        )
        
        self._log(f"\n{'#'*60}")
        self._log(f"✨ PIPELINE RSA COMPLETADO")
        self._log(f"{'#'*60}\n")
        
        return final_solution
