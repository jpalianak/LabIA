import streamlit as st
import requests

# Estilos personalizados con CSS
st.markdown(
    """
    <style>
    /* Centrar el contenido de la barra lateral */
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centrar elementos */
        justify-content: flex-start;
        padding-top: 20px; /* Espaciado superior */
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
        padding: 5px 0;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }

    /* Enlaces del footer */
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

    <!-- Footer HTML -->
    <div class="footer">
        <p>Developed by AIRBIZ<br>
        <a href="https://www.airbiz.com.ar/" target="_blank">www.airbiz.com.ar</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Barra lateral
with st.sidebar:
    # Contenedor del logo
    #st.image("https://raw.githubusercontent.com/jpalianak/LabIA/main/airbiz.png", width=150)
    
    # Espaciado adicional entre logo y selectbox
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Lista desplegable para seleccionar convenios
    doc_option = st.selectbox(
        "Selecciona el convenio a consultar:",
        ["ATE", "UOM", "CTERA", "UOCRA"]
    )

st.title("Consulta convenio")

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

            # Mostrar respuesta final de OpenAI
            openai_answer = data.get('answer', 'No se obtuvo respuesta de OpenAI')
            st.subheader("Respuesta")
            st.success(openai_answer)
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error("No se pudo conectar con el servidor.")
        st.write(str(e))






