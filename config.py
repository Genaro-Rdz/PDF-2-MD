"""Configuración central de la app. Cambia aquí, no en el resto del código."""
from pathlib import Path

APP_TITLE = "PDF → Markdown (MarkItDown)"
WINDOW_SIZE = "640x420"

# Extensiones que la app acepta. MarkItDown también soporta .docx, .pptx, .xlsx.
SUPPORTED_EXTENSIONS = {".pdf"}
# TODO (Semana 4): ¿quieres aceptar Word/PowerPoint/Excel? Agrégalos aquí
#                  y revisa qué "extras" de markitdown necesitas en requirements.txt.

# Carpeta de salida por defecto.
DEFAULT_OUTPUT_DIR = Path.home() / "Documents" / "markdown_salida"

OUTPUT_ENCODING = "utf-8"
