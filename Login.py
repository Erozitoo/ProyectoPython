import streamlit as st
import sqlite3


def verificar_usuario(nombreUsuario, password):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nombreUsuario=? AND password=?", (nombreUsuario, password))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# Inicializamos estado
if "logueado" not in st.session_state:
    st.session_state.logueado = False

# Si ya está logueado, mostramos acceso
if st.session_state.logueado:
    st.success("Has iniciado sesión correctamente ✅")
    st.page_link("pages/Opciones.py", label="Ir a Opciones 👉", icon="➡️")
    st.stop()

# Interfaz de login
st.title("Login")

nombreUsuario = st.text_input("Ingrese su nombre de usuario")
password = st.text_input("Ingrese su contraseña", type="password")

if st.button("Ingresar"):
    if verificar_usuario(nombreUsuario, password):
        st.session_state.logueado = True
        st.rerun()
    else:
        st.error("Nombre de usuario o contraseña incorrectos")

st.markdown("---")
st.page_link("pages/Registro.py", label="¿No tienes cuenta? Regístrate aquí 👉", icon="📝")
