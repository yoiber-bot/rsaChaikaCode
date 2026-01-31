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

- ✅ Integración con **GitHub Models** (GPT-4o, GPT-4o-mini, Llama, Mistral, etc.)
- ✅ **Uso gratuito** para desarrollo personal
- ✅ Pipeline completamente automatizado
- ✅ Parámetros configurables (población, grupos, loops, temperatura)
- ✅ Manejo inteligente de rate limits y reintentos
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
- GitHub Personal Access Token (gratuito en [GitHub Settings](https://github.com/settings/tokens))

## 🔧 Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/yoiber-bot/rsaChaikaCode.git
cd rsaChaikaCode
```

2. **Configurar versión de Python (si usas pyenv)**:
```bash
pyenv local 3.11.9
```

3. **Crear entorno virtual**:
```bash
python -m venv venv
```

4. **Activar el entorno virtual**:
   - En Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   - En Windows:
   ```powershell
   .\venv\Scripts\activate
   ```

5. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

6. **Configurar GitHub Token**:
   - Ve a [github.com/settings/tokens](https://github.com/settings/tokens)
   - Crea un nuevo Personal Access Token (no necesitas permisos especiales)
   - Crea un archivo `.env` en la raíz del proyecto:
   ```bash
   echo "GITHUB_TOKEN=tu_token_aqui" > .env
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
- `--population N`: Tamaño de población inicial (default: 8)
- `--group-size K`: Tamaño de grupos para agregación (default: 4)
- `--loops L`: Número de iteraciones RSA (default: 3)
- `--temperature T`: Temperatura para diversidad (0.0-2.0, default: 1.0)
- `--model M`: Modelo a usar (default: gpt-4o, disponibles: gpt-4o, gpt-4o-mini, gpt-4-turbo)
- `--quiet`: Solo muestra el resultado final
- `--api-key KEY`: GitHub token alternativo

### Uso Programático (API Python)

```python
from src.rsa_orchestrator import RSAOrchestrator

# Inicializar
rsa = RSAOrchestrator(
    model_name="gpt-4o",  # o "gpt-4o-mini" para más velocidad
    population_size=8,
    group_size=4,
    loops=3,
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

| Tarea | Población | Grupos | Loops | Modelo |
|-------|-----------|--------|-------|--------|
| **Código simple** | 4 | 4 | 2 | gpt-4o-mini |
| **Algoritmos complejos** | 8 | 4 | 3 | gpt-4o |
| **Diseño de sistemas** | 12 | 4 | 3 | gpt-4o |
| **Debugging** | 6 | 3 | 2 | gpt-4o-mini |
| **Razonamiento lógico** | 8 | 4 | 3 | gpt-4o |

## 🏗️ Estructura del Proyecto

```
rsaChaikaCode/
├── src/
│   ├── __init__.py
│   ├── gemini_client.py      # Cliente API (GitHub Models)
│   ├── aggregation.py         # Lógica de agregación
│   └── rsa_orchestrator.py    # Orquestador principal
├── main.py                     # CLI
├── examples.py                 # Ejemplos de uso
├── requirements.txt            # Dependencias
├── .env                        # Configuración (crear manualmente)
└── README.md                   # Este archivo
```

## 🔒 Seguridad

- **No incluyas** tu GitHub token en el código
- Usa el archivo `.env` (está en `.gitignore`)
- No compartas tu `.env` en repositorios públicos
- El token solo necesita acceso básico (sin permisos especiales)

## 📝 Limitaciones

- Requiere GitHub Personal Access Token (gratuito)
- Sujeto a rate limits de GitHub Models (15 RPM, se manejan automáticamente)
- El tiempo de ejecución depende de la configuración:
  - Configuración rápida (4 población, 2 loops): ~1-2 minutos
  - Configuración estándar (8 población, 3 loops): ~3-5 minutos
  - Configuración compleja (12 población, 3 loops): ~5-8 minutos
- **GitHub Models es gratuito para uso personal y desarrollo**

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
