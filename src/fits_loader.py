from astropy.io import fits
import numpy as np

def load_fits(ruta):
    hdul = fits.open(ruta)

    flux = hdul[0].data

    header = hdul[0].header

    wave = header["CRVAL1"] + np.arange(len(flux))*header["CDELT1"]

    hdul.close()

    return wave, flux