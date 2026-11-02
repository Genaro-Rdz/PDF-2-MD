"""Lógica de conversión (sin interfaz). La usan tanto main.py como cli.py.

Regla de diseño: este módulo NO debe importar tkinter. Así puedes probarlo solo.
"""
from pathlib import Path

from markitdown import MarkItDown

import config

_md = MarkItDown()


def convert_one(pdf_path: Path, output_dir: Path) -> Path:
    """Convierte UN archivo y devuelve la ruta del .md creado. (Ya funciona.)"""
    output_dir.mkdir(parents=True, exist_ok=True)
    result = _md.convert(str(pdf_path))
    out_path = output_dir / f"{pdf_path.stem}.md"
    out_path.write_text(result.text_content, encoding=config.OUTPUT_ENCODING)
    return out_path


def find_pdfs(folder: Path) -> list[Path]:
    """Devuelve los archivos soportados dentro de una carpeta."""
    # TODO (Semana 2): hoy solo mira el primer nivel. Pista: Path.glob vs Path.rglob.
    return sorted(p for p in folder.glob("*") if p.suffix.lower() in config.SUPPORTED_EXTENSIONS)


def convert_batch(files: list[Path], output_dir: Path, on_progress=None) -> list[tuple[Path, str]]:
    """Convierte varios archivos. Devuelve una lista de (archivo, mensaje)."""
    results = []
    for i, f in enumerate(files, start=1):
        # TODO (Semana 2): si UN PDF falla, hoy se cae todo el lote.
        #   Pista: ¿qué estructura de Python te deja "atrapar" un error y seguir?
        out = convert_one(f, output_dir)
        results.append((f, f"OK -> {out.name}"))

        # TODO (Semana 2): dos PDFs con el mismo nombre en carpetas distintas
        #   se sobrescriben. Piensa cómo generar un nombre único.

        if on_progress:
            on_progress(i, len(files))
    return results


# TODO (Semana 4, opcional): función combine(...) que una todos los .md en uno solo.
