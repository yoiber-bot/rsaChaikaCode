"""
Aggregation Module
Handles grouping and aggregation of responses using RSA technique
"""

from typing import List


def create_groups(responses: List[str], group_size: int) -> List[List[str]]:
    """
    Divide responses into groups of specified size
    
    Args:
        responses: List of response strings
        group_size: Size of each group
        
    Returns:
        List of groups, where each group is a list of responses
    """
    groups = []
    
    for i in range(0, len(responses), group_size):
        group = responses[i:i + group_size]
        groups.append(group)
    
    return groups


def create_aggregation_prompt(responses: List[str], original_prompt: str) -> str:
    """
    Create a prompt for aggregating multiple responses
    
    Args:
        responses: List of responses to aggregate
        original_prompt: The original user prompt
        
    Returns:
        Aggregation prompt for the LLM
    """
    prompt = f"""Estas son varias soluciones diferentes al siguiente problema:

PROBLEMA ORIGINAL:
{original_prompt}

---

SOLUCIONES A ANALIZAR:

"""
    
    for i, response in enumerate(responses, 1):
        prompt += f"\n{'='*60}\nSOLUCIÓN {i}:\n{'='*60}\n{response}\n"
    
    prompt += f"""

{'='*60}
TU TAREA:

1. Analiza cada solución cuidadosamente
2. Identifica las partes correctas de cada una
3. Detecta errores, inconsistencias o contradicciones
4. Combina lo mejor de todas las soluciones
5. Produce UNA solución superior que sea:
   - Más correcta que cualquiera de las individuales
   - Más coherente y completa
   - Sin errores ni contradicciones
   - Optimizada y bien estructurada

Proporciona ÚNICAMENTE la solución mejorada, sin explicaciones sobre el proceso de agregación.
"""
    
    return prompt


def create_final_aggregation_prompt(responses: List[str], original_prompt: str) -> str:
    """
    Create a prompt for final consolidation of all refined solutions
    
    Args:
        responses: List of final refined responses
        original_prompt: The original user prompt
        
    Returns:
        Final aggregation prompt for the LLM
    """
    prompt = f"""Has completado múltiples rondas de refinamiento para el siguiente problema:

PROBLEMA ORIGINAL:
{original_prompt}

---

SOLUCIONES REFINADAS (después de múltiples iteraciones):

"""
    
    for i, response in enumerate(responses, 1):
        prompt += f"\n{'='*60}\nSOLUCIÓN REFINADA {i}:\n{'='*60}\n{response}\n"
    
    prompt += f"""

{'='*60}
TAREA FINAL:

De todas estas soluciones refinadas, produce la MEJOR VERSIÓN FINAL que sea:
- Completamente corregida y sin errores
- Optimizada al máximo
- La más clara y coherente posible
- La más completa y robusta

Esta es la respuesta definitiva que se entregará al usuario. Hazla perfecta.
"""
    
    return prompt
