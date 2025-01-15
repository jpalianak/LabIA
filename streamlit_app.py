import streamlit as st
import requests

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


