import streamlit as st

st.title("Registro de Usuario")

usuario = st.text_input("Nombre de usuario")
clave = st.text_input("Contraseña", type="password")

if st.button("Registrar"):
    st.success("Usuario registrado con éxito 🎉")

st.page_link("Login.py", label="⬅ Volver al Login")
