# 🧠 RSA (Recursive Self-Aggregation) System

Sistema de auto-refinamiento iterativo para LLMs que mejora la calidad de respuestas en tareas complejas mediante técnicas de agregación recursiva.

## 🎯 ¿Qué es RSA?

RSA (Recursive Self-Aggregation) es una técnica que convierte un LLM normal en un modelo con razonamiento mejorado mediante:

- **Generación diversa**: Crea múltiples soluciones diferentes al mismo problema
- **Agregación iterativa**: Combina y refina soluciones en múltiples rondas
- **Auto-corrección**: Elimina errores y contradicciones progresivamente
- **Refinamiento evolutivo**: Cada iteración mejora la calidad de las soluciones

**No es un chat** - Es un orquestador automático de múltiples llamadas al modelo.

## 🚀 Características

- ✅ Integración con **Google Gemini API**
- ✅ Pipeline completamente automatizado
- ✅ Parámetros configurables (población, grupos, loops, temperatura)
- ✅ Manejo de rate limits y reintentos
- ✅ Interfaz CLI y API programática
- ✅ Logging detallado del proceso
- ✅ Ideal para tareas complejas:
  - Programación
  - Razonamiento lógico
  - Algoritmos
  - Debugging
  - Diseño de sistemas

## 📋 Requisitos

- Python 3.7+
- API Key de Google Gemini (gratuita en [Google AI Studio](https://makersuite.google.com/app/apikey))

## 🔧 Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/yoiber-bot/rsaChaikaCode.git
cd rsaChaikaCode
```

2. **Crear entorno virtual**:
```bash
python -m venv venv
```

3. **Activar el entorno virtual**:
   - En Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

5. **Configurar API Key**:
```bash
cp .env.example .env
# Editar .env y agregar tu GEMINI_API_KEY
```

> **Nota**: Recuerda activar el entorno virtual cada vez que trabajes en el proyecto usando `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)

## 💻 Uso

### Interfaz de Línea de Comandos (CLI)

**Uso básico**:
```bash
python main.py "Escribe un algoritmo de ordenamiento quicksort en Python"
```

**Con configuración personalizada**:
```bash
python main.py "Explica cómo funcionan las redes neuronales" \
  --population 12 \
  --group-size 3 \
  --loops 7 \
  --temperature 1.2
```

**Modo silencioso**:
```bash
python main.py "Tu prompt aquí" --quiet
```

**Opciones disponibles**:
- `--population N`: Tamaño de población inicial (default: 16)
- `--group-size K`: Tamaño de grupos para agregación (default: 4)
- `--loops L`: Número de iteraciones RSA (default: 5)
- `--temperature T`: Temperatura para diversidad (0.0-2.0, default: 1.0)
- `--model M`: Modelo de Gemini (default: gemini-flash-latest)
- `--quiet`: Solo muestra el resultado final
- `--api-key KEY`: API key alternativa

### Uso Programático (API Python)

```python
from src.rsa_orchestrator import RSAOrchestrator

# Inicializar
rsa = RSAOrchestrator(
    population_size=16,
    group_size=4,
    loops=5,
    temperature=1.0,
    verbose=True
)

# Ejecutar
prompt = "Diseña una API RESTful para un sistema de gestión de tareas"
result = rsa.run(prompt)

print(result)
```

### Ejemplos Incluidos

```bash
python examples.py
```

## 🔄 Cómo Funciona

### Flujo del Pipeline RSA

```
1. GENERACIÓN INICIAL (Población N)
   ├── Respuesta 1 (temperatura alta)
   ├── Respuesta 2
   ├── ...
   └── Respuesta N

2. AGREGACIÓN ITERATIVA (Loop 1...L)
   ├── Dividir en grupos de tamaño K
   ├── Agregar cada grupo → Nueva respuesta
   └── Repetir L veces

3. CONSOLIDACIÓN FINAL
   └── Agregar todas las respuestas → Solución final
```

### Ejemplo de Flujo

```
Población inicial: 16 respuestas
   ↓
Loop 1: 16 → 4 grupos de 4 → 4 respuestas agregadas
   ↓
Loop 2: 4 → 1 grupo de 4 → 1 respuesta agregada
   ↓
Loop 3: 1 respuesta (ya convergió)
   ↓
Consolidación final → Solución óptima
```

## ⚙️ Parámetros y Configuración

### `population_size` (N)
- **Descripción**: Número de respuestas iniciales diversas
- **Rango recomendado**: 8-24
- **Efecto**: 
  - ↑ Más diversidad pero más lento
  - ↓ Más rápido pero menos opciones

### `group_size` (K)
- **Descripción**: Tamaño de grupos para agregación
- **Rango recomendado**: 3-5
- **Efecto**:
  - ↑ Menos iteraciones, agregación más compleja
  - ↓ Más iteraciones, agregación más simple

### `loops` (L)
- **Descripción**: Número de rondas de refinamiento
- **Rango recomendado**: 3-10
- **Efecto**:
  - ↑ Más refinamiento pero más lento
  - ↓ Más rápido pero menos refinado

### `temperature`
- **Descripción**: Controla creatividad/diversidad
- **Rango**: 0.0-2.0
- **Recomendado**: 0.9-1.2 para diversidad inicial

## 📊 Casos de Uso Ideales

| Tarea | Población | Grupos | Loops | Temperatura |
|-------|-----------|--------|-------|-------------|
| **Código simple** | 8 | 4 | 3 | 1.0 |
| **Algoritmos complejos** | 16 | 4 | 5 | 1.1 |
| **Diseño de sistemas** | 20 | 5 | 7 | 1.2 |
| **Debugging** | 12 | 3 | 4 | 0.9 |
| **Razonamiento lógico** | 16 | 4 | 6 | 1.0 |

## 🏗️ Estructura del Proyecto

```
rsaChaikaCode/
├── src/
│   ├── __init__.py
│   ├── gemini_client.py      # Cliente API de Gemini
│   ├── aggregation.py         # Lógica de agregación
│   └── rsa_orchestrator.py    # Orquestador principal
├── main.py                     # CLI
├── examples.py                 # Ejemplos de uso
├── requirements.txt            # Dependencias
├── .env.example                # Template de configuración
└── README.md                   # Este archivo
```

## 🔒 Seguridad

- **No incluyas** tu API key en el código
- Usa el archivo `.env` (está en `.gitignore`)
- No compartas tu `.env` en repositorios públicos

## 📝 Limitaciones

- Requiere API key de Google Gemini
- Sujeto a rate limits de la API (se manejan automáticamente)
- El tiempo de ejecución depende de la configuración:
  - Configuración básica: ~2-5 minutos
  - Configuración avanzada: ~10-20 minutos
- Costo de API basado en número de tokens

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🙏 Agradecimientos

Basado en técnicas de auto-refinamiento y agregación para LLMs, inspirado en investigación sobre mejora de razonamiento en modelos de lenguaje.

## 📬 Contacto

- GitHub: [@yoiber-bot](https://github.com/yoiber-bot)
- Proyecto: [rsaChaikaCode](https://github.com/yoiber-bot/rsaChaikaCode)

---

**¿Tienes dudas o sugerencias?** Abre un issue en GitHub.
