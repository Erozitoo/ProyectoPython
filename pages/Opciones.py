import streamlit as st

# Verificamos que esté logueado
if 'logueado' not in st.session_state or not st.session_state.logueado:
    st.error("Debes iniciar sesión primero.")
    st.stop()

# Mostramos el saludo
usuario = st.session_state.get("name", "Usuario")
st.title(f"Hola {usuario} 👋")