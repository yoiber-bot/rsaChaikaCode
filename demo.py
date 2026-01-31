"""
Demo script that simulates RSA without API calls
Shows the flow and structure of the system
"""

import time


class MockGeminiClient:
    """Mock client for demonstration"""
    
    def __init__(self):
        self.call_count = 0
    
    def generate_response(self, prompt, temperature=1.0):
        """Simulate API response"""
        self.call_count += 1
        time.sleep(0.1)  # Simulate network delay
        return f"Mock response {self.call_count} (temp={temperature})"
    
    def generate_multiple_responses(self, prompt, count, temperature=1.0, delay=0.5):
        """Simulate multiple responses"""
        responses = []
        for i in range(count):
            print(f"🔄 Generating response {i + 1}/{count}...")
            response = self.generate_response(prompt, temperature)
            responses.append(response)
        return responses


def demonstrate_rsa_flow():
    """Demonstrate RSA flow without real API"""
    print("="*60)
    print("🎬 RSA SYSTEM - DEMO (Sin API real)")
    print("="*60)
    print("\nEste demo muestra cómo funciona el sistema RSA")
    print("sin hacer llamadas reales a la API.\n")
    
    # Configuration
    population_size = 16
    group_size = 4
    loops = 3
    
    print(f"Configuración:")
    print(f"  - Población inicial: {population_size}")
    print(f"  - Tamaño de grupos: {group_size}")
    print(f"  - Loops: {loops}")
    print(f"  - Temperatura: 1.0")
    
    # Mock client
    client = MockGeminiClient()
    
    # Phase 1: Initial generation
    print(f"\n{'='*60}")
    print(f"📝 FASE 1: Generación de población inicial")
    print(f"{'='*60}\n")
    
    responses = client.generate_multiple_responses(
        "Ejemplo de prompt",
        count=population_size,
        temperature=1.0,
        delay=0.1
    )
    
    print(f"\n✅ Generadas {len(responses)} respuestas iniciales")
    print(f"   API calls hasta ahora: {client.call_count}")
    
    # Phase 2: Aggregation loops
    current_population = responses
    
    for loop_num in range(1, loops + 1):
        print(f"\n{'='*60}")
        print(f"🔄 LOOP {loop_num}: Fase de agregación")
        print(f"{'='*60}")
        
        # Create groups
        num_groups = (len(current_population) + group_size - 1) // group_size
        print(f"\nDividiendo {len(current_population)} respuestas en {num_groups} grupos")
        
        # Aggregate each group
        new_population = []
        for i in range(num_groups):
            print(f"🔀 Agregando grupo {i + 1}/{num_groups}...")
            aggregated = client.generate_response("Aggregation prompt", temperature=0.7)
            new_population.append(aggregated)
            print(f"   ✓ Grupo {i + 1} agregado")
        
        current_population = new_population
        print(f"\n✅ Loop {loop_num} completado: {len(current_population)} respuestas")
        print(f"   API calls hasta ahora: {client.call_count}")
        
        # Check convergence
        if len(current_population) == 1:
            print(f"   ⚡ Convergencia alcanzada en loop {loop_num}")
            break
    
    # Phase 3: Final aggregation
    print(f"\n{'='*60}")
    print(f"🏁 FASE FINAL: Consolidación")
    print(f"{'='*60}\n")
    
    print(f"Consolidando {len(current_population)} soluciones refinadas...")
    final_solution = client.generate_response("Final aggregation prompt", temperature=0.3)
    
    print(f"\n{'='*60}")
    print(f"✨ RESULTADO FINAL")
    print(f"{'='*60}")
    print(f"\n{final_solution}")
    
    # Statistics
    print(f"\n{'='*60}")
    print(f"📊 ESTADÍSTICAS")
    print(f"{'='*60}")
    print(f"Total API calls: {client.call_count}")
    print(f"Población inicial: {population_size}")
    print(f"Loops completados: {loop_num}")
    print(f"Soluciones finales consolidadas: 1")
    
    print(f"\n{'='*60}")
    print(f"✅ DEMO COMPLETADO")
    print(f"{'='*60}")
    print("\nPara usar con la API real de Gemini:")
    print("1. Instala dependencias: pip install -r requirements.txt")
    print("2. Configura GEMINI_API_KEY en .env")
    print("3. Ejecuta: python main.py \"tu prompt\"")


if __name__ == "__main__":
    demonstrate_rsa_flow()
