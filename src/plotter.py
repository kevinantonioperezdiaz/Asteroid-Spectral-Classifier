import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def plot_comparison(
        wave_ast,
        flux_ast,
        flux_modelo,
        clase,
        error,
        info,
        mostrar=True):

    plt.figure(figsize=(9,6))

    # Espectro observado
    plt.plot(
        wave_ast,
        flux_ast,
        color="black",
        linewidth=2.5,
        label="Asteroide observado"
    )

    # Modelo DeMeo
    plt.plot(
        wave_ast,
        flux_modelo,
        color="red",
        linewidth=2,
        label=f"Modelo DeMeo {clase}"
    )

    # Etiquetas
    plt.xlabel("Longitud de onda (μm)")
    plt.ylabel("Reflectancia")

    # Título
    plt.title(
        f"Clasificación espectral: {clase}\n"
        f"MSE = {error:.2e}"
    )

    # Cuadrícula suave
    plt.grid(alpha=0.3)

    # Leyenda
    plt.legend(frameon=True)

    # Texto con información taxonómica
    texto = (
        f"Tipo: {clase}\n\n"
        f"Minerales:\n"
        f"{info['minerales']}\n\n"
        f"Bandas:\n"
        f"{info['bandas_absorcion']}\n\n"
        f"Ubicación:\n"
        f"{info['ubicacion_probable']}"
    )

    plt.text(
        0.98,
        0.03,
        texto,
        transform=plt.gca().transAxes,
        fontsize=9,
        verticalalignment="bottom",
        horizontalalignment="right",
        bbox=dict(
            facecolor="white",
            alpha=0.8,
            edgecolor="gray"
        )
    )

    plt.tight_layout()
    fig = plt.gcf()

    if mostrar:
      plt.show()

    return fig