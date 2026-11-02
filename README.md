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

## Calendario semanal

| Semana | Área | Qué haces | Entregable |
|---|---|---|---|
| 1 | Entorno + CLI | Instala, corre ambos scripts con 2 o 3 PDFs reales. En `cli.py` agrega `argparse` con `-o carpeta_salida`. | `python cli.py carpeta -o salida` funciona |
| 2 | Lógica (`converter.py`) | Búsqueda en subcarpetas, que un PDF dañado no detenga el lote, nombres únicos. | Lote de 10 PDFs (uno corrupto) termina con reporte OK/ERROR |
| 3 | Interfaz (`main.py`) | Agregar carpeta, quitar y limpiar, elegir salida, evitar duplicados, que la ventana no se congele. | Ventana usable de principio a fin sin congelarse |
| 4 | Calidad y extras | Botón "Abrir carpeta", opción de combinar en un solo `.md`, revisar la calidad del Markdown en PDFs escaneados (MarkItDown no hace OCR por sí solo). | Lista de 3 mejoras probadas con PDFs reales |
| 5 | Empaquetado | Crear `.exe` con PyInstaller y probarlo en otra PC sin Python. | `PDF2MD.exe` que abre con doble clic |

## Cómo trabajamos

- Atórate primero un rato. Luego pregúntame "¿cómo hago X?" y te explico el concepto con una pista.
- Si quieres el código completo de algo, pídelo explícitamente.
- Pásame tu código y te digo qué falla y por qué, sin reescribirlo.
