import streamlit as st

st.title("Login")

nombre = st.text_input("Ingrese su nombre")
password = st.text_input("Ingrese su contraseña", type="password")

if st.button("Ingresar"):
    st.success(f"Bienvenido {nombre}")

st.markdown("---")

# ✅ Este es el método correcto:
st.page_link("pages/Registro.py", label="¿No tienes cuenta? Regístrate aquí 👉", icon="📝")
