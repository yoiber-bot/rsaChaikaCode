"""
RSA System - Command Line Interface
"""

import argparse
import sys
from src.rsa_orchestrator import RSAOrchestrator


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='RSA (Recursive Self-Aggregation) System - Mejora respuestas de LLMs mediante refinamiento iterativo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Usar con configuración por defecto
  python main.py "Escribe un algoritmo de ordenamiento quicksort en Python"

  # Configuración personalizada
  python main.py "Explica cómo funcionan las redes neuronales" --population 12 --group-size 3 --loops 7

  # Modo silencioso
  python main.py "Debug este código: [código aquí]" --quiet

Para más información: https://github.com/yoiber-bot/rsaChaikaCode
        """
    )
    
    parser.add_argument(
        'prompt',
        type=str,
        help='Prompt o problema a resolver'
    )
    
    parser.add_argument(
        '--population',
        type=int,
        default=8,
        help='Tamaño de población inicial (default: 8)'
    )
    
    parser.add_argument(
        '--group-size',
        type=int,
        default=4,
        help='Tamaño de grupos para agregación (default: 4)'
    )
    
    parser.add_argument(
        '--loops',
        type=int,
        default=3,
        help='Número de loops RSA (default: 3)'
    )
    
    parser.add_argument(
        '--temperature',
        type=float,
        default=1.0,
        help='Temperatura para generación (0.0-2.0, default: 1.0)'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-4o',
        help='Modelo a usar (default: gpt-4o, disponibles: gpt-4o, gpt-4o-mini, gpt-4-turbo)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (solo muestra resultado final)'
    )
    
    parser.add_argument(
        '--api-key',
        type=str,
        help='API key de Google Gemini (opcional, se puede usar .env)'
    )
    
    args = parser.parse_args()
    
    # Validate parameters
    if args.population < 2:
        print("❌ Error: --population debe ser al menos 2")
        sys.exit(1)
    
    if args.group_size < 2:
        print("❌ Error: --group-size debe ser al menos 2")
        sys.exit(1)
    
    if args.loops < 1:
        print("❌ Error: --loops debe ser al menos 1")
        sys.exit(1)
    
    if not (0.0 <= args.temperature <= 2.0):
        print("❌ Error: --temperature debe estar entre 0.0 y 2.0")
        sys.exit(1)
    
    try:
        # Initialize orchestrator
        orchestrator = RSAOrchestrator(
            api_key=args.api_key,
            model_name=args.model,
            population_size=args.population,
            group_size=args.group_size,
            loops=args.loops,
            temperature=args.temperature,
            verbose=not args.quiet
        )
        
        # Run RSA pipeline
        result = orchestrator.run(args.prompt)
        
        # Print result
        print("\n" + "="*60)
        print("📌 SOLUCIÓN FINAL")
        print("="*60 + "\n")
        print(result)
        print("\n" + "="*60 + "\n")
        
    except ValueError as e:
        print(f"❌ Error de configuración: {e}")
        print("\nAsegúrate de configurar GEMINI_API_KEY en .env o usar --api-key")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error durante ejecución: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
