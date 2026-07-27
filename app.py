import streamlit as st
import os
from langchain_cohere import ChatCohere
from langchain_community.document_loaders import PyPDFLoader

# Configuración de la página
st.set_page_config(page_title="Agente BimBamBuy", page_icon="🤖")
st.title("🤖 Asistente Inteligente BimBam Buy")

# Lectura segura de la llave
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

    st.success("✅ Documento cargado exitosamente. ¡Hazme una pregunta!")

    # ---------------------------------------------------------
    # AQUI ESTÁ LA MAGIA NUEVA: Una caja de texto para el usuario
    # ---------------------------------------------------------
    pregunta_usuario = st.text_input("Escribe tu pregunta sobre los métodos de pago:")

    if st.button("Enviar pregunta"):
        if pregunta_usuario:
            # Ahora la instrucción usa TU pregunta, no una fija
            instruccion = f"""
            Eres un amable asistente inteligente de la empresa BimBam Buy. 
            Responde la pregunta del usuario basándote ÚNICAMENTE en el siguiente documento.
            
            Documento:
            {texto_pagina}

            Pregunta del usuario: {pregunta_usuario}
            """
            with st.spinner('Consultando a Cohere...'):
                respuesta = llm.invoke(instruccion)
                st.write("**🤖 Agente BimBamBuy:**")
                st.info(respuesta.content)
        else:
            st.warning("Por favor, escribe una pregunta primero antes de enviar.")
else:
    st.error(f"❌ No se encontró el archivo: {nombre_archivo}. Asegúrate de subirlo a tu entorno.")