# Guía de Uso - RSA System

## 🚀 Inicio Rápido

### 1. Instalación

```bash
# Clonar repositorio
git clone https://github.com/yoiber-bot/rsaChaikaCode.git
cd rsaChaikaCode

# Instalar dependencias
pip install -r requirements.txt

# Configurar API key
cp .env.example .env
# Editar .env y agregar tu GEMINI_API_KEY
```

### 2. Obtener API Key de Google Gemini

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Create API Key"
4. Copia la clave y pégala en el archivo `.env`:

```
GEMINI_API_KEY=tu_clave_aqui
```

### 3. Primer Uso

```bash
python main.py "Escribe una función para calcular números de Fibonacci"
```

## 📖 Ejemplos Detallados

### Ejemplo 1: Algoritmo Simple

```bash
python main.py "Implementa un algoritmo de búsqueda binaria en Python con manejo de errores" \
  --population 8 \
  --group-size 4 \
  --loops 3
```

**Cuándo usarlo**: Problemas de programación básicos o medianos.

### Ejemplo 2: Problema Complejo

```bash
python main.py "Diseña una arquitectura completa de microservicios para Netflix" \
  --population 20 \
  --group-size 5 \
  --loops 7 \
  --temperature 1.2
```

**Cuándo usarlo**: Problemas de diseño de sistemas, arquitectura compleja.

### Ejemplo 3: Debugging

```bash
python main.py "Este código tiene un bug, encuéntralo y corrígelo: [tu código]" \
  --population 12 \
  --group-size 3 \
  --loops 4 \
  --temperature 0.9
```

**Cuándo usarlo**: Encontrar y corregir bugs en código existente.

### Ejemplo 4: Razonamiento Lógico

```bash
python main.py "Resuelve el problema de las N reinas para un tablero de 8x8" \
  --population 16 \
  --group-size 4 \
  --loops 6
```

**Cuándo usarlo**: Problemas algorítmicos complejos, puzzles lógicos.

## 🎛️ Configuración de Parámetros

### Cómo elegir `population_size`

| Tamaño | Uso | Ventajas | Desventajas |
|--------|-----|----------|-------------|
| 4-8 | Pruebas rápidas | Muy rápido | Poca diversidad |
| 12-16 | Uso general | Buen balance | Tiempo moderado |
| 20-24 | Problemas complejos | Alta diversidad | Lento, más costoso |

### Cómo elegir `group_size`

| Tamaño | Efecto | Cuándo usar |
|--------|--------|-------------|
| 2 | Muchas iteraciones, agregación simple | Refinamiento gradual |
| 3-4 | Balance óptimo | Uso general (recomendado) |
| 5-6 | Pocas iteraciones, agregación compleja | Problemas muy complejos |

### Cómo elegir `loops`

| Loops | Tiempo | Calidad | Cuándo usar |
|-------|--------|---------|-------------|
| 2-3 | Rápido | Básica | Pruebas o problemas simples |
| 4-6 | Moderado | Buena | Uso general |
| 7-10 | Lento | Excelente | Problemas críticos |

### Cómo elegir `temperature`

| Temperatura | Comportamiento | Cuándo usar |
|-------------|----------------|-------------|
| 0.7-0.9 | Más conservador, consistente | Debugging, corrección de código |
| 1.0 | Balanceado | Uso general |
| 1.1-1.3 | Más creativo, diverso | Diseño, arquitectura, ideas nuevas |

## 💡 Casos de Uso Específicos

### Caso 1: Generar Código Robusto

**Objetivo**: Obtener código de alta calidad con manejo de errores.

```bash
python main.py "Crea una API REST en Flask para gestión de usuarios con autenticación JWT" \
  --population 16 \
  --group-size 4 \
  --loops 5 \
  --temperature 1.0
```

**Por qué estos parámetros**:
- `population 16`: Suficiente diversidad en implementaciones
- `group_size 4`: Balance entre iteraciones y complejidad
- `loops 5`: Suficiente refinamiento para eliminar bugs
- `temperature 1.0`: Balance creatividad/consistencia

### Caso 2: Optimizar Algoritmo

**Objetivo**: Encontrar la implementación más eficiente.

```bash
python main.py "Optimiza este algoritmo de ordenamiento: [tu código]" \
  --population 12 \
  --group-size 3 \
  --loops 6 \
  --temperature 1.1
```

**Por qué estos parámetros**:
- `population 12`: Varias estrategias de optimización
- `group_size 3`: Más iteraciones para refinamiento gradual
- `loops 6`: Convergencia hacia solución óptima
- `temperature 1.1`: Creatividad para optimizaciones no obvias

### Caso 3: Explicación Didáctica

**Objetivo**: Obtener explicación clara y completa.

```bash
python main.py "Explica cómo funciona el algoritmo de Dijkstra con ejemplos" \
  --population 10 \
  --group-size 5 \
  --loops 4 \
  --temperature 1.2
```

**Por qué estos parámetros**:
- `population 10`: Diferentes enfoques explicativos
- `group_size 5`: Agregar múltiples perspectivas
- `loops 4`: Balance tiempo/calidad
- `temperature 1.2`: Creatividad en ejemplos

## 📊 Estimación de Tiempos

| Configuración | Tiempo Aprox. | Tokens Aprox. |
|---------------|---------------|---------------|
| Rápida (8/4/3) | 2-3 min | ~50K |
| Normal (16/4/5) | 5-8 min | ~120K |
| Completa (20/5/7) | 12-18 min | ~250K |

*Tiempos y tokens son aproximados y varían según complejidad del prompt.*

## 🔍 Modo Verbose vs Quiet

### Verbose (default)

```bash
python main.py "tu prompt"
```

Muestra todo el proceso:
- Generación inicial
- Cada loop de agregación
- Consolidación final
- Resultado

**Usar cuando**: Quieres ver el progreso o debuggear.

### Quiet

```bash
python main.py "tu prompt" --quiet
```

Solo muestra el resultado final.

**Usar cuando**: Solo te interesa el resultado.

## 🐛 Solución de Problemas

### Error: "GEMINI_API_KEY not found"

**Solución**:
```bash
# Verifica que .env existe
ls -la .env

# Si no existe, créalo
cp .env.example .env

# Edita y agrega tu key
nano .env
```

### Error: "Rate limit exceeded"

**Solución**: La API tiene límites de requests. El sistema ya maneja reintentos, pero si persiste:
- Reduce `population_size`
- Espera unos minutos e intenta de nuevo

### Resultado no satisfactorio

**Solución**:
1. Aumenta `loops` para más refinamiento
2. Aumenta `population_size` para más diversidad
3. Ajusta `temperature` según necesites más creatividad o consistencia
4. Reformula el prompt con más detalles

## 💻 Uso Programático Avanzado

```python
from src.rsa_orchestrator import RSAOrchestrator

# Configuración personalizada
config = {
    'population_size': 16,
    'group_size': 4,
    'loops': 5,
    'temperature': 1.0,
    'verbose': True
}

rsa = RSAOrchestrator(**config)

# Ejecutar
result = rsa.run("Tu prompt aquí")

# Usar resultado
print(result)
# O guardar en archivo
with open('resultado.txt', 'w') as f:
    f.write(result)
```

## 📈 Tips para Mejores Resultados

1. **Sé específico en el prompt**: Cuanto más detallado, mejor.

   ❌ Mal: "Escribe un sort"
   ✅ Bien: "Implementa quicksort en Python con manejo de edge cases y complejidad O(n log n)"

2. **Incluye requisitos**: Lista lo que necesitas.

   ```
   Crea una API REST que:
   - Use FastAPI
   - Tenga autenticación JWT
   - Incluya validación de datos
   - Tenga tests unitarios
   ```

3. **Para debugging**: Incluye el error completo.

   ```
   Debuggea este código que da error:
   [código]
   
   Error: IndexError: list index out of range
   ```

4. **Ajusta según resultados**: Si la primera vez no es perfecta, ajusta parámetros y reintenta.

## 🎯 Conclusión

El sistema RSA es más potente cuando:
- El problema es complejo
- Necesitas alta calidad
- Puedes esperar unos minutos
- Quieres múltiples perspectivas combinadas

¡Experimenta con diferentes configuraciones para encontrar lo que mejor funciona para tu caso!
