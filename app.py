import streamlit as st
import os
from langchain_cohere import ChatCohere
from langchain_community.document_loaders import PyPDFLoader

# Configuración de la página
st.set_page_config(page_title="Agente BimBamBuy", page_icon="🤖")
st.title("🤖 Asistente Inteligente BimBam Buy")

# Lectura segura de la llave (desde Streamlit Secrets o desde tu .env local)
if "COHERE_API_KEY" in st.secrets:
    mi_llave = st.secrets["COHERE_API_KEY"]
else:
    mi_llave = os.environ.get("COHERE_API_KEY")

# Configuración del modelo
llm = ChatCohere(model="command-r7b-arabic-02-2025", cohere_api_key=mi_llave)

# Cargar el PDF
nombre_archivo = "preguntas frecuentes_metodos de pago_BimBamBuy.pdf"

if os.path.exists(nombre_archivo):
    cargador = PyPDFLoader(nombre_archivo)
    documento = cargador.load()
    texto_pagina = documento[0].page_content

    st.write("✅ Documento cargado exitosamente.")

    # Instrucción
    instruccion = f"""
    Eres un asistente inteligente de la empresa BimBam Buy. 
    Por favor, lee el siguiente texto y dime cuáles son los 3 primeros temas del índice.

    Texto del documento:
    {texto_pagina}
    """

    # Ejecución
    if st.button("Consultar temas del índice"):
        with st.spinner('Consultando a Cohere...'):
            respuesta = llm.invoke(instruccion)
            st.subheader("Respuesta del Agente:")
            st.write(respuesta.content)
else:
    st.error(f"❌ No se encontró el archivo: {nombre_archivo}. Asegúrate de subirlo a tu entorno.")
