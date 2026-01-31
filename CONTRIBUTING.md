# Contribuir al Proyecto RSA

¡Gracias por tu interés en contribuir al sistema RSA! Este documento te guiará en el proceso.

## 🤝 Cómo Contribuir

### Reportar Bugs

Si encuentras un bug, por favor abre un issue con:

1. **Título descriptivo**
2. **Descripción del problema**
3. **Pasos para reproducir**
4. **Comportamiento esperado vs actual**
5. **Configuración utilizada** (population_size, group_size, loops, etc.)
6. **Versión de Python y dependencias**

### Sugerir Mejoras

Para sugerencias de nuevas funcionalidades:

1. **Verifica** que no exista ya un issue similar
2. **Describe** el caso de uso
3. **Explica** por qué sería útil
4. **Propón** una posible implementación si tienes ideas

### Pull Requests

1. **Fork** el repositorio
2. **Crea** una rama desde `main`:
   ```bash
   git checkout -b feature/mi-nueva-funcionalidad
   ```
3. **Implementa** tus cambios
4. **Prueba** que todo funciona
5. **Commit** con mensajes descriptivos:
   ```bash
   git commit -m "Add: nueva funcionalidad X"
   ```
6. **Push** a tu fork:
   ```bash
   git push origin feature/mi-nueva-funcionalidad
   ```
7. **Abre** un Pull Request

## 🏗️ Estructura del Código

```
rsaChaikaCode/
├── src/
│   ├── gemini_client.py      # Cliente API de Gemini
│   ├── aggregation.py         # Lógica de agregación
│   └── rsa_orchestrator.py    # Orquestador principal
├── main.py                     # CLI
├── examples.py                 # Ejemplos de uso
├── test_logic.py              # Tests de lógica
└── demo.py                     # Demo sin API
```

## 🧪 Testing

Antes de enviar un PR, ejecuta los tests:

```bash
# Tests de lógica (sin API)
python test_logic.py

# Demo
python demo.py
```

Si agregas nuevas funcionalidades, añade tests apropiados.

## 📝 Estilo de Código

- Sigue **PEP 8**
- Usa **docstrings** para funciones y clases
- **Comenta** código complejo
- Nombres de variables en **inglés** preferiblemente
- Mensajes de usuario en **español**

Ejemplo:

```python
def create_groups(responses: List[str], group_size: int) -> List[List[str]]:
    """
    Divide responses into groups of specified size
    
    Args:
        responses: List of response strings
        group_size: Size of each group
        
    Returns:
        List of groups, where each group is a list of responses
    """
    # Implementation
    pass
```

## 🎯 Áreas de Contribución

### Prioridad Alta

- [ ] Añadir más tests unitarios
- [ ] Optimización de rate limiting
- [ ] Soporte para otros modelos de Gemini
- [ ] Caché de respuestas
- [ ] Métricas de calidad

### Prioridad Media

- [ ] Interfaz web (Gradio/Streamlit)
- [ ] Soporte para múltiples APIs (OpenAI, Anthropic)
- [ ] Sistema de logging avanzado
- [ ] Visualización del proceso RSA
- [ ] Exportación de resultados

### Ideas Futuras

- [ ] Paralelización de llamadas API
- [ ] Fine-tuning de prompts de agregación
- [ ] Modo interactivo
- [ ] API REST
- [ ] Dashboard de métricas

## 🐛 Debugging

Para debuggear problemas:

```python
# Activar verbose
rsa = RSAOrchestrator(verbose=True)

# Ver prompts generados
from src.aggregation import create_aggregation_prompt
print(create_aggregation_prompt(responses, prompt))
```

## 📚 Recursos

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Best Practices](https://docs.python-guide.org/)
- [Git Commit Messages](https://chris.beams.io/posts/git-commit/)

## ⚖️ Licencia

Al contribuir, aceptas que tu código esté bajo la misma licencia del proyecto (MIT).

## 💬 Preguntas

¿Tienes dudas? Abre un issue con la etiqueta `question`.

---

¡Gracias por contribuir! 🎉
