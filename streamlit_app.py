import streamlit as st

# Estilo personalizado con CSS
st.markdown(
    """
    <style>
    /* Estilo para centrar el contenido de la barra lateral */
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start; /* Ajustar para espacio extra arriba */
        padding-top: 20px; /* Espacio adicional arriba */
    }

    /* Ajustar el estilo de la imagen del logo */
    .sidebar .logo-container img {
        width: 100px;
        height: auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra lateral
with st.sidebar:
    # Contenedor del logo
    st.image("https://raw.githubusercontent.com/jpalianak/LabIA/main/airbiz.png", width=150)
    
    # Espaciado adicional entre logo y selectbox
    st.markdown("<br>", unsafe_allow_html=True)
    
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
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error("No se pudo conectar con el servidor.")
        st.write(str(e))






