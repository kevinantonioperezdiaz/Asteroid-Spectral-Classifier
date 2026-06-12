from src.fits_loader import load_fits
from src.classifier import classify_asteroid
from src.fits_loader import load_fits
from src.classifier import classify_asteroid
from src.plotter import plot_comparison
from src.taxonomy import get_taxonomy
from src.report_generator import generate_report
# =====================================
# Cargar espectro del asteroide
# =====================================
wave_ast, flux_ast = load_fits("Asteroid-Spectral-Classifier/data/examples/asteroide1.fits")
# =====================================
# Clasificación
# =====================================
carpeta_demeo = "Asteroid-Spectral-Classifier/data/demeo"

clase, error, flux_modelo = classify_asteroid(wave_ast,flux_ast,carpeta_demeo)
print("Clase encontrada:", clase)
print("Error:", error)

wave_ast, flux_ast = load_fits(
    "Asteroid-Spectral-Classifier/data/examples/asteroide1.fits"
)

carpeta_demeo = "Asteroid-Spectral-Classifier/data/demeo"

clase, error, flux_modelo = classify_asteroid(
    wave_ast,
    flux_ast,
    carpeta_demeo
)

# =====================================
# Resultados
# =====================================

print("Clase encontrada:", clase)
print("Error:", error)

info = get_taxonomy(clase)

print("\n==============================")
print("INFORMACIÓN TAXONÓMICA")
print("==============================")

print("Clase taxonómica:", clase)

print("\nComposición:")
print(info["composicion"])

print("\nMinerales dominantes:")
print(info["minerales"])

print("\nMeteoritos análogos:")
print(info["meteoritos_analogos"])

print("\nBandas de absorción:")
print(info["bandas_absorcion"])

print("\nLongitudes características:")
print(info["longitudes_absorcion"])

print("\nPendiente espectral:")
print(info["pendiente"])

print("\nDescripción:")
print(info["descripcion"])

print("\nUbicación probable:")
print(info["ubicacion_probable"])

print("\nComplejo taxonómico:")
print(info["complejo"])

print("\nAlbedo:")
print(info["albedo"])

print("\nComentario:")
print(info["comentario"])

fig = plot_comparison(
    wave_ast,
    flux_ast,
    flux_modelo,
    clase,
    error,
    info
)

generate_report(
    clase,
    error,
    info,
    fig
)