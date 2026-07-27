# 🤖 Asistente Inteligente BimBam Buy

🔗 **[¡Prueba la aplicación en vivo en Streamlit!](https://proyectoagente-m6qpyfxrb8ojepj85rbobc.streamlit.app/)**

## 📖 Descripción general del proyecto
Este proyecto consiste en un agente conversacional interactivo diseñado para el área de atención al cliente de la empresa ficticia **BimBam Buy**. El objetivo principal del agente es responder de forma precisa y amigable a las dudas de los usuarios sobre los métodos de pago, basando sus respuestas estrictamente en un documento oficial proporcionado en formato PDF. Esto evita que la inteligencia artificial "alucine" o invente información que no corresponde a las políticas de la empresa.

## 🏗️ Arquitectura de la solución implementada
La solución sigue un flujo de trabajo basado en la arquitectura **RAG (Retrieval-Augmented Generation)** simplificada:
1. **Interfaz de Usuario (Frontend):** Se utiliza Streamlit para renderizar una página web interactiva con una caja de chat.
2. **Ingesta de Datos:** Mediante la librería `pypdf`, el sistema carga y extrae el texto del documento base (`preguntas frecuentes_metodos de pago_BimBamBuy.pdf`).
3. **Orquestación (Middleware):** LangChain toma la pregunta del usuario y la combina con el texto extraído del documento dentro de una plantilla de instrucciones estructurada (Prompt Engineering).
4. **Procesamiento LLM (Backend):** La instrucción combinada se envía a la API del modelo de lenguaje de Cohere, el cual procesa la información y genera una respuesta contextualizada.
5. **Respuesta:** El agente devuelve la respuesta procesada a la interfaz web de Streamlit para el usuario.
6. **Despliegue (Nube):** El código se aloja en GitHub y se despliega mediante Integración Continua (CI/CD) nativa en Streamlit Community Cloud.

## 🛠️ Tecnologías y herramientas utilizadas
* **Lenguaje de programación:** Python 3
* **Framework Frontend / Web:** [Streamlit](https://streamlit.io/)
* **Orquestación de IA:** [LangChain](https://www.langchain.com/) (`langchain-cohere`, `langchain-community`)
* **Procesamiento de documentos:** `pypdf`
* **Modelo de Lenguaje (LLM):** Cohere (`command-r7b-arabic-02-2025`)
* **Control de versiones:** Git y GitHub
* **Entorno de desarrollo:** GitHub Codespaces

## 💻 Instrucciones para ejecutar el proyecto

Si deseas ejecutar este proyecto de manera local, sigue los siguientes pasos:

1. **Clona el repositorio en tu máquina:**
   ```bash
   git clone [https://github.com/TU_USUARIO/proyecto_agente.git](https://github.com/TU_USUARIO/proyecto_agente.git)
   cd proyecto_agente


   Instala las dependencias necesarias:

Bash
pip install -r requirements.txt
Configura tus variables de entorno:
Crea un archivo llamado .env en la raíz del proyecto y agrega tu llave secreta de la API de Cohere:

Plaintext
COHERE_API_KEY="tu_llave_de_cohere_aqui"
Inicia la aplicación:

Bash
streamlit run app.py
(Esto abrirá automáticamente una pestaña en tu navegador web local con la interfaz del agente).

❓ Ejemplos de preguntas que el agente puede responder
Debido a que el agente está limitado al contexto del documento de preguntas frecuentes, puedes realizarle consultas como:

"¿Cuáles son los métodos de pago disponibles?"

"¿Aceptan tarjetas de crédito y cuáles son?"

"¿Tienen la opción de pago a meses sin intereses?"

"Dime el propósito y el alcance de este documento."

💬 Ejemplos de respuestas generadas por el agente
Pregunta del usuario: "¿Cuáles son los 3 primeros temas del índice?"

Respuesta del Agente BimBamBuy:
"Los 3 primeros temas del índice del documento son:

Propósito

Alcance

Métodos de pago disponibles"

Pregunta del usuario: "¿Qué tarjetas aceptan?"

Respuesta del Agente BimBamBuy:
"De acuerdo con el documento, en BimBam Buy aceptamos las principales tarjetas de crédito y débito, incluyendo Visa, MasterCard y American Express."


*(No olvides reemplazar `TU_USUARIO` en la sección de clonación por tu nombre real de GitHub).*

Una vez que pegues esto, guárdalo y ejecuta los comandos habituales para subirlo:
```bash
git add README.md
git commit -m "Actualizando README con requerimientos completos"
git push origin master

