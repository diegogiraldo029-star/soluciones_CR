import streamlit as st
from word_a_pdf import*

   
#Botones
st.html("""
<style>

/* =========================
   ESTILO 1 - PRINCIPAL
   ========================= */

button[kind="primary"] {
    width: 100%;
    height: 72px !important;

    background: linear-gradient(
        90deg,
        #5C481F 0%,
        #29251C 8%,
        #15181B 100%
    ) !important;

    color: #F2E8D0 !important;

    border: 1px solid #806A35 !important;
    border-radius: 14px !important;
    
    font-size: 20px !important;
    font-weight: 1000 !important;
    letter-spacing: 0.8px;

    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}


/* =========================
   ESTILO 2 - SECUNDARIO
   ========================= */

button[kind="secondary"] {
    width: 100%;
    height: 72px !important;

    background: linear-gradient(
        90deg,
        #5C481F 0%,
        #29258C 8%,
        #15181B 100%
    ) !important;

    color: #F2E8D0 !important;

    border: 1px solid white !important;
    border-radius: 14px !important;

    font-size: 20px !important;
    font-weight: 1000 !important;

    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
button[kind="tertiary"] {
    width: 100%;
    height: 72px !important;

    background: linear-gradient(
        90deg,
        #4A121A 0%,    /* Vino tinto profundo */
        #2D0B10 40%,   /* Vino tinto más oscuro */
        #150507 100%  
    ) !important;

    color: #F2E8D0 !important;

    border: 1px solid white !important;
    border-radius: 14px !important;

    font-size: 20px !important;
    font-weight: 1000 !important;

    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

</style>
""")




#titulo

st.title("SOLUCIONES CR")


#----------Estados cerrados
if "pdf_a_word" not in st.session_state:
    st.session_state.pdf_a_word = False


#aplicaciones 
if st.button("CONVIERTE PDF A WORD",use_container_width=True):
    st.session_state.pdf_a_word = True



#--------ESTADOS APLICACIONES-------
if st.session_state.pdf_a_word:
    archivo = st.file_uploader("SUBA EL PDF QUE QUIERE CONVERTIR A TIPO WORD", type=["pdf"])
    if archivo:
        archivo_convertido=convertir_a_word(archivo)
    name_archivo="documento_convertido"

    with open(name_archivo+ ".docx", "rb") as file:
        docx_bytes = file.read()


    if st.download_button(
        "Descargar Word",
        data=docx_bytes,
        file_name=name_archivo + ".docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
        type="tertiary"
    ):
        st.rerun()

#py -3.12 -m streamlit run Soluciones_CR.py