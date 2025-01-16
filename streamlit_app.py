import streamlit as st
import requests

# Footer
footer="""<style>
a:link , a:visited{color: blue;background-color: transparent;text-decoration: underline;}
a:hover,  a:active {color: red;background-color: transparent;text-decoration: underline;}
.footer {position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;}
</style>
<div class="footer">
<p>Developed by AIRBIZ <a style='display: block; text-align: center;' href="https://www.airbiz.com.ar/" target="_blank">www.airbiz.com.ar</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# Agregar el logo con CSS
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        padding-top: 0;
    }
    .logo-container {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 150px;
    }
    </style>
    <div class="logo-container">
        <img src="https://https://github.com/jpalianak/LabIA/blob/main/airbiz.png" alt="Logo" width="150">
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


