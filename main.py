import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader

# 1. Seguridad: Leemos la llave secreta desde el entorno, NO la escribimos aquí.
mi_llave = os.environ.get("GEMINI_API_KEY")

# 2. Configuramos el cerebro
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", api_key=mi_llave)

# 3. Configuramos los ojos (Asegúrate de que este nombre sea exactamente el de tu PDF)
nombre_archivo = "preguntas frecuentes_metodos de pago_BimBamBuy.pdf"
cargador = PyPDFLoader(nombre_archivo)
documento = cargador.load()

# 4. Instrucción
texto_pagina = documento[0].page_content
instruccion = f"""
Eres un asistente inteligente de la empresa BimBam Buy. 
Por favor, lee el siguiente texto extraído de nuestro documento y dime cuáles son los 3 primeros temas del índice.

Texto del documento:
{texto_pagina}
"""

# 5. Ejecución
print("Pensando...")
respuesta_final = llm.invoke(instruccion)

# Extraemos el texto limpio del paquete de respuesta
texto_limpio = respuesta_final.content[0]['text']
print("\nRespuesta:")
print(texto_limpio)