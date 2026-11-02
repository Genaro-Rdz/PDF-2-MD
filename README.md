# PDF → Markdown (app de escritorio con MarkItDown)

Esqueleto funcional: ya abre una ventana, deja elegir varios PDFs y los convierte a `.md`.
Lo demás lo completas tú siguiendo los `# TODO` de cada archivo (cada uno indica su semana).

## Estructura

| Archivo | Responsabilidad |
|---|---|
| `config.py` | Constantes: título, extensiones, carpeta de salida |
| `converter.py` | Lógica de conversión con MarkItDown, sin interfaz |
| `cli.py` | Versión de terminal para probar `converter.py` sola |
| `main.py` | Ventana de escritorio (tkinter) |
| `requirements.txt` | Dependencias |

Idea clave: la interfaz (`main.py`) **llama** a la lógica (`converter.py`), nunca al revés.

## Cómo arrancar (Windows)

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python cli.py C:\ruta\a\mis_pdfs     :: prueba por terminal
python main.py                       :: abre la ventana
```

Los `.md` se guardan en `Documentos\markdown_salida`.

