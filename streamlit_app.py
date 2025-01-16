import streamlit as st
import requests

# Agregar el logo y el footer con CSS
st.markdown(
    """
    <style>
    /* Espacio superior para evitar que el logo se solape */
    .main {
        padding-top: 80px; /* Ajustar según sea necesario */
    }

    /* Contenedor del logo */
    .logo-container {
        position: fixed;
        top: 10px; /* Asegura que el logo no quede cortado */
        left: 10px;
        width: 150px;
        z-index: 1000;
    }

    /* Estilo del footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 5px 0; /* Reducir espacio vertical */
        font-size: 14px;
        border-top: 1px solid #ddd;
        line-height: 1.5; /* Controlar el espacio entre líneas */
    }

    /* Estilo de los enlaces */
    a:link, a:visited {
        color: blue;
        background-color: transparent;
        text-decoration: underline;
    }
    a:hover, a:active {
        color: red;
        background-color: transparent;
        text-decoration: underline;
    }
    </style>

    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/jpalianak/LabIA/main/airbiz.png" alt="Logo" width="150">
    </div>

    <div class="footer">
        <p>Developed by AIRBIZ<br>
        <a href="https://www.airbiz.com.ar/" target="_blank">www.airbiz.com.ar</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Consulta convenio Plastico")

# Input del usuario
query = st.text_input("Introduce tu consulta:")

if st.button("Enviar"):
    url = "https://fzfi0gugng.execute-api.us-east-1.amazonaws.com/Prod/query"
    headers = {"Content-Type": "application/json"}
    payload = {"query": query}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            # Mostrar la respuesta completa para diagnosticar
            #st.write("Respuesta completa de la API:")
            #st.json(data)  # Esto mostrará toda la respuesta JSON

            # Mostrar respuesta de Pinecone
            #pinecone_response = data.get('pinecone', 'No se encontró respuesta de Pinecone')
            #st.subheader("Respuesta de Pinecone")
            #st.write(pinecone_response)

            # Mostrar respuesta final de OpenAI
            openai_answer = data.get('answer', 'No se obtuvo respuesta de OpenAI')
            st.subheader("Respuesta")
            st.success(openai_answer)
            
            # Mostrar fuentes
            #sources = data.get('sources', [])
            #st.write("Fuentes:", sources)
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error("No se pudo conectar con el servidor.")
        st.write(str(e))


