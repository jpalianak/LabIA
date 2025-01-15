import streamlit as st
import requests

st.title("Consulta Embedding Lambda")

# Input del usuario
query = st.text_input("Introduce tu consulta:")

if st.button("Enviar"):
    url = "https://abc123.execute-api.us-east-1.amazonaws.com/prod/query-embedding"
    headers = {"Content-Type": "application/json"}
    payload = {"query": query}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Respuesta: {data['answer']}")
            st.write("Fuentes:", data['sources'])
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error("No se pudo conectar con el servidor.")
        st.write(str(e))
