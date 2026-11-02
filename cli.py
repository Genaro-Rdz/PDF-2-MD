"""Versión de línea de comandos: útil para probar converter.py sin la ventana.

Uso:  python cli.py ruta\\a\\carpeta_o_pdf
"""
import sys
from pathlib import Path

import config
from converter import convert_batch, find_pdfs


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python cli.py <carpeta o archivo.pdf>")
        return
    target = Path(sys.argv[1])
    files = find_pdfs(target) if target.is_dir() else [target]

    # TODO (Semana 1): permitir elegir la carpeta de salida. Pista: módulo argparse.
    for f, msg in convert_batch(files, config.DEFAULT_OUTPUT_DIR):
        print(f"{f.name}: {msg}")


if __name__ == "__main__":
    main()
