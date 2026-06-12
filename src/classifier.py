import numpy as np
import os
from src.fits_loader import load_fits

def interpolate_spectrum(wave_ref, flux_ref, wave_target):
    flux_interp = np.interp(wave_target,wave_ref,flux_ref)
    return flux_interp

def calculate_error(flux_ast, flux_ref):

    error = np.mean((flux_ast - flux_ref)**2)

    return error

def classify_asteroid(wave_ast, flux_ast, carpeta_demeo):

    mejor_error = np.inf

    for archivo in os.listdir(carpeta_demeo):

        ruta = os.path.join(carpeta_demeo, archivo)

        wave_ref, flux_ref = load_fits(ruta)

        flux_interp = interpolate_spectrum(
            wave_ref,
            flux_ref,
            wave_ast
        )

        error = calculate_error(
            flux_ast,
            flux_interp
        )

        if error < mejor_error:

            mejor_error = error
            mejor_clase = archivo.replace(".fits", "")
            mejor_flux_interp = flux_interp

    return mejor_clase, mejor_error, mejor_flux_interp