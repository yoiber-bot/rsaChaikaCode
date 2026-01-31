"""
Ejemplo básico de uso del sistema RSA
"""

from src.rsa_orchestrator import RSAOrchestrator


def example_basic():
    """Ejemplo básico con configuración por defecto"""
    print("="*60)
    print("EJEMPLO BÁSICO: Uso del sistema RSA")
    print("="*60)
    
    # Inicializar orchestrator
    rsa = RSAOrchestrator(
        population_size=8,  # Población pequeña para el ejemplo
        group_size=4,
        loops=3,
        temperature=1.0,
        verbose=True
    )
    
    # Prompt de ejemplo
    prompt = """
Escribe una función en Python que implemente el algoritmo de búsqueda binaria.
La función debe:
- Recibir una lista ordenada y un valor a buscar
- Retornar el índice si lo encuentra, -1 si no
- Incluir manejo de casos edge
- Tener complejidad O(log n)
"""
    
    # Ejecutar RSA
    result = rsa.run(prompt)
    
    # Mostrar resultado
    print("\n" + "="*60)
    print("RESULTADO FINAL")
    print("="*60)
    print(result)


def example_advanced():
    """Ejemplo avanzado con configuración personalizada"""
    print("="*60)
    print("EJEMPLO AVANZADO: Configuración personalizada")
    print("="*60)
    
    # Configuración avanzada
    rsa = RSAOrchestrator(
        population_size=20,  # Más diversidad
        group_size=5,
        loops=7,  # Más refinamiento
        temperature=1.2,  # Más creatividad
        verbose=True
    )
    
    # Problema complejo
    prompt = """
Diseña una arquitectura de microservicios para un sistema de e-commerce que soporte:
- 10,000 usuarios concurrentes
- Procesamiento de pagos
- Gestión de inventario en tiempo real
- Sistema de recomendaciones
- Alta disponibilidad

Incluye:
- Diagrama de componentes
- Tecnologías recomendadas
- Estrategia de escalabilidad
- Manejo de fallas
"""
    
    result = rsa.run(prompt)
    
    print("\n" + "="*60)
    print("RESULTADO FINAL")
    print("="*60)
    print(result)


if __name__ == "__main__":
    print("Selecciona un ejemplo:")
    print("1. Ejemplo básico (rápido)")
    print("2. Ejemplo avanzado (más completo)")
    
    choice = input("\nOpción (1 o 2): ").strip()
    
    if choice == "1":
        example_basic()
    elif choice == "2":
        example_advanced()
    else:
        print("Opción inválida")
