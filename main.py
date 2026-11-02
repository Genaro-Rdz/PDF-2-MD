"""Ventana de escritorio (tkinter, viene incluido con Python).

Ejecuta:  python main.py
"""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import config
from converter import convert_batch


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry(config.WINDOW_SIZE)
        self.files: list[Path] = []
        self.output_dir = config.DEFAULT_OUTPUT_DIR
        self._build_ui()

    def _build_ui(self):
        bar = ttk.Frame(self, padding=8)
        bar.pack(fill="x")
        ttk.Button(bar, text="Agregar PDFs…", command=self.add_files).pack(side="left")
        # TODO (Semana 3): botón "Agregar carpeta…". Pista: filedialog.askdirectory + find_pdfs.
        # TODO (Semana 3): botón "Quitar seleccionados" y "Limpiar lista".

        self.listbox = tk.Listbox(self, selectmode="extended")
        self.listbox.pack(fill="both", expand=True, padx=8)

        out = ttk.Frame(self, padding=8)
        out.pack(fill="x")
        self.out_label = ttk.Label(out, text=f"Salida: {self.output_dir}")
        self.out_label.pack(side="left")
        # TODO (Semana 3): botón "Cambiar…" para elegir la carpeta de salida.

        self.progress = ttk.Progressbar(self, mode="determinate")
        self.progress.pack(fill="x", padx=8)
        ttk.Button(self, text="Convertir", command=self.convert).pack(pady=8)

    def add_files(self):
        paths = filedialog.askopenfilenames(filetypes=[("PDF", "*.pdf")])
        for p in paths:
            self.files.append(Path(p))
            self.listbox.insert("end", Path(p).name)
        # TODO (Semana 3): evitar duplicados si el usuario agrega el mismo PDF dos veces.

    def convert(self):
        if not self.files:
            messagebox.showinfo(config.APP_TITLE, "Agrega al menos un PDF.")
            return
        self.progress["maximum"] = len(self.files)

        # TODO (Semana 3): con muchos PDFs la ventana se "congela" mientras convierte.
        #   Concepto clave: el hilo de la interfaz. Pista: threading + self.after(...).
        results = convert_batch(self.files, self.output_dir, on_progress=self._on_progress)

        messagebox.showinfo(config.APP_TITLE, f"Listo: {len(results)} archivo(s) en\n{self.output_dir}")
        # TODO (Semana 4): botón "Abrir carpeta de salida". Pista: os.startfile en Windows.

    def _on_progress(self, done, total):
        self.progress["value"] = done
        self.update_idletasks()


if __name__ == "__main__":
    App().mainloop()
