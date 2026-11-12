#py -m pip install python-docx
from docx import Document
from fpdf import FPDF


import fitz
from docx import Document
from docx.shared import Inches
from io import BytesIO
def convertir_a_word(archivo):
# Abrir PDF y crear documento Word
    
    pdf = fitz.open(stream=archivo.getvalue(), filetype="pdf")
    word = Document()

    for numero, pagina in enumerate(pdf):

        word.add_heading(f"Página {numero + 1}", level=1)

        # Obtener bloques de contenido
        contenido = pagina.get_text("dict")

        for bloque in contenido["blocks"]:

            # 1. EXTRAER TEXTO
            if "lines" in bloque:

                texto = ""

                for linea in bloque["lines"]:
                    for span in linea["spans"]:
                        texto += span["text"]

                    texto += "\n"

                if texto.strip():
                    word.add_paragraph(texto.strip())

            # 2. EXTRAER IMÁGENES
            elif "image" in bloque:

                imagen = bloque["image"]

                word.add_picture(
                    BytesIO(imagen),
                    width=Inches(4)
                )

        # 3. EXTRAER TABLAS
        tablas = pagina.find_tables()

        for tabla in tablas.tables:

            datos = tabla.extract()

            if not datos:
                continue

            filas = len(datos)
            columnas = max(len(fila) for fila in datos)

            tabla_word = word.add_table(
                rows=filas,
                cols=columnas
            )

            tabla_word.style = "Table Grid"

            for i, fila in enumerate(datos):
                for j, valor in enumerate(fila):

                    tabla_word.cell(i, j).text = str(
                        valor if valor is not None else ""
                    )

        # Separar páginas
        if numero < len(pdf) - 1:
            word.add_page_break()

    # Guardar documento
    word.save("documento_convertido.docx")

    
