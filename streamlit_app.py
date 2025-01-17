import streamlit as st

# Estilo personalizado con CSS
st.markdown(
    """
    <style>
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
        line-height: 1.5;
    }

    /* Centrar contenido de la barra lateral */
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Centrar específicamente la imagen */
    .sidebar .logo-container img {
        display: block;
        margin: 0 auto;
    }
    </style>

    <div class="footer">
        <p>Desarrollado por AIRBIZ<br>
        <a href="https://www.airbiz.com.ar/" target="_blank">www.airbiz.com.ar</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Barra lateral
with st.sidebar:
    # Agregar el logo centrado
    st.markdown(
        """
        <div class="logo-container">
            <img src="https://raw.githubusercontent.com/jpalianak/LabIA/main/airbiz.png" alt="Logo" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Espaciado entre el logo y el selectbox
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Lista desplegable para seleccionar convenios
    doc_option = st.selectbox(
        "Selecciona el convenio a consultar:",
        ["ATE", "UOM", "CTERA", "UOCRA"]
    )

st.title("Consulta convenio Plástico")

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
            st.error(f"Error: {response.status_cod






