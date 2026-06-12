from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
import os

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


def generate_report(clase, error, info, fig):

    carpeta_reportes = os.path.join(
    os.getcwd(),
    "reports"
    )

    os.makedirs(
    carpeta_reportes,
    exist_ok=True
    )

    contador = 0

    while True:

        if contador == 0:
            nombre_pdf = "informe_asteroide.pdf"
        else:
            nombre_pdf = f"informe_asteroide{contador}.pdf"

        ruta_pdf = os.path.join(
            carpeta_reportes,
            nombre_pdf
        )

        if not os.path.exists(ruta_pdf):
            break

        contador += 1

    doc = SimpleDocTemplate(ruta_pdf) 

    styles = getSampleStyleSheet()
    from reportlab.lib.styles import ParagraphStyle

    styles["Title"].fontName = "Times-Bold"

    body_style = styles["BodyText"]
    body_style.fontName = "Times-Roman"
    body_style.alignment = TA_JUSTIFY

    body_style = styles["BodyText"]

    body_style.alignment = TA_JUSTIFY

    subtitle_style = ParagraphStyle(
    "subtitle_style",
    parent=body_style,
    fontName="Times-Bold",
    fontSize=14
    )



    contenido = []

    # Título
    titulo = Paragraph(
        "CLASIFICACIÓN ESPECTRAL DE ASTEROIDES",
        styles["Title"]
    )

    contenido.append(titulo)
    contenido.append(Spacer(1,0.5*cm))

    # Tabla de resultados
    datos = [

        ["Tipo taxonómico", clase],

        ["Error de ajuste", f"{error:.2e}"],

        ["Composición", info["composicion"]],

        ["Minerales", info["minerales"]],

        ["Bandas de absorción", info["bandas_absorcion"]],

        ["Longitudes características", info["longitudes_absorcion"]],

        ["Pendiente espectral", info["pendiente"]],

        ["Ubicación probable", info["ubicacion_probable"]],

        ["Meteoritos análogos", info["meteoritos_analogos"]]

    ]

    tabla = Table(datos)

    tabla.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

            ("FONTNAME",(0,0),(-1,-1),"Times-Roman"),

            ("BOX",(0,0),(-1,-1),1,colors.black),

            ("GRID",(0,0),(-1,-1),0.5,colors.black),

            ("PADDING",(0,0),(-1,-1),8)

        ])

    )

    contenido.append(tabla)

    contenido.append(Spacer(1,0.7*cm))

    # Comentario
    contenido.append(
    Paragraph(
        "Comentario:",
        subtitle_style
    )
    )

    comentario = Paragraph(
    info["comentario"],
    body_style
    )

    contenido.append(comentario)

    ruta_figura = os.path.join(
    carpeta_reportes,
    "temp_plot.png"
    )
    fig.savefig(
    ruta_figura,
    dpi=300,
    bbox_inches="tight"
    )

    contenido.append(
    Spacer(1,0.5*cm)
    )

    contenido.append(
    Image(
        ruta_figura,
        width=16*cm,
        height=10*cm
      )
    )

    conclusion = Paragraph(

    f"El espectro analizado presenta una excelente coincidencia con la clase taxonómica {clase}. "

    + f"{info['descripcion']}. "

    + f"Los minerales predominantes corresponden a {info['minerales']}. "

    + f"{info['bandas_absorcion']}. "

    + f"Las características espectrales observadas son compatibles con una composición "

    + f"{info['composicion']}. "

    + f"Este tipo de objetos se encuentra preferentemente en {info['ubicacion_probable']}.",

    body_style

)

    contenido.append(
    Spacer(1,0.5*cm)
     )
    contenido.append(
    Paragraph(
        "Conclusión:",
        subtitle_style
    )

    )

    contenido.append(
    Spacer(1,0.2*cm)
)

    contenido.append(conclusion)

    doc.build(contenido)
    print(ruta_pdf)
    if os.path.exists(ruta_figura):
        os.remove(ruta_figura)