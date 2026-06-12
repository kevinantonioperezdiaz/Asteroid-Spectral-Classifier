import tkinter as tk
import os
from src.fits_loader import load_fits
from src.classifier import classify_asteroid
from src.taxonomy import get_taxonomy
from tkinter import filedialog
from src.plotter import plot_comparison
from src.report_generator import generate_report

import sys

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)

carpeta_demeo = resource_path(
    os.path.join("data", "demeo")
)
clase = None
error = None
info = None
wave_ast = None
flux_ast = None
flux_modelo = None
fig = None
ventana = tk.Tk()
ventana.configure(bg="#1e1e1e")

ventana.title("Asteroid Spectral Classifier v1.0")
ventana.geometry("400x600")

# Título
titulo = tk.Label(
    ventana,
    text="Asteroid Spectral Classifier",
    font=("Times New Roman",18,"bold"),
    fg="white",
    bg="#1e1e1e"
)
titulo.pack(pady=10)

# Autor
autor = tk.Label(
    ventana,
    text="Created by:\nKevin Antonio Perez Diaz",
    font=("Times New Roman",10),
    fg="white",
    bg="#1e1e1e"
)
autor.pack()

# Mostrar archivo seleccionado
archivo_label = tk.Label(
    ventana,
    text="Ningún archivo seleccionado",
    fg="white",
    bg="#1e1e1e",
    font=("Times New Roman",10)
)


ruta_archivo = ""

# Función para seleccionar archivo
def seleccionar_archivo():

    global ruta_archivo

    ruta_archivo = filedialog.askopenfilename(
        filetypes=[("Archivos FITS","*.fits")]
    )

    if ruta_archivo:
        archivo_label.config(
        text=os.path.basename(ruta_archivo)
    )

def clasificar():

    global clase, error, info
    global wave_ast, flux_ast, flux_modelo

    wave_ast, flux_ast = load_fits(ruta_archivo)

    clase, error, flux_modelo = classify_asteroid(
        wave_ast,
        flux_ast,
        carpeta_demeo
    )

    info = get_taxonomy(clase)

    resultado_label.config(
        text=
        f"Tipo: {clase}\n\n"
        f"Composición:\n{info['composicion']}\n\n"
        f"Ubicación:\n{info['ubicacion_probable']}"
    )

def mostrar_grafica():

    global fig

    fig = plot_comparison(
        wave_ast,
        flux_ast,
        flux_modelo,
        clase,
        error,
        info
    )

def exportar_pdf():

    fig = plot_comparison(
    wave_ast,
    flux_ast,
    flux_modelo,
    clase,
    error,
    info,
    mostrar=False
    )

    generate_report(
    clase,
    error,
    info,
    fig
    )
# Botón seleccionar archivo
boton_archivo = tk.Button(
    ventana,
    text="Seleccionar archivo FITS",
    bg="#3c3f41",
    fg="white",
    activebackground="#4a4d50",
    activeforeground="white",
    command=seleccionar_archivo
)

boton_archivo.pack(pady=10)
archivo_label.pack(pady=5)


# Botón clasificar
boton_clasificar = tk.Button(
    ventana,
    text="Clasificar asteroide",
    bg="#3c3f41",
    fg="white",
    activebackground="#4a4d50",
    activeforeground="white",
    command=clasificar
)

boton_clasificar.pack(pady=10)

resultado_label = tk.Label(
    ventana,
    text="",
    fg="white",
    bg="#1e1e1e",
    font=("Times New Roman",10)
)

resultado_label.pack(pady=10)


# Botón mostrar gráfica
boton_grafica = tk.Button(
    ventana,
    text="Mostrar gráfica",
    bg="#3c3f41",
    fg="white",
    activebackground="#4a4d50",
    activeforeground="white",
    command=mostrar_grafica
)

boton_grafica.pack(pady=10)


# Botón exportar PDF
boton_pdf = tk.Button(
    ventana,
    text="Exportar PDF",
    bg="#3c3f41",
    fg="white",
    activebackground="#4a4d50",
    activeforeground="white",
    command=exportar_pdf
)

boton_pdf.pack(pady=10)

ventana.mainloop()