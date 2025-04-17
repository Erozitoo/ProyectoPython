import streamlit as st
import sqlite3

st.set_page_config(page_title="Registro", layout="centered")


def usuario_existe(nombreUsuario):
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nombreUsuario TEXT,
            telefono TEXT,
            correo TEXT,
            password TEXT
        )
    ''')
    c.execute("SELECT * FROM clientes WHERE nombreUsuario = ?", (nombreUsuario,))
    resultado = c.fetchone()
    conn.close()
    return resultado is not None


def guardar_usuario(nombre, nombreUsuario, telefono, correo, password):
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nombreUsuario TEXT,
            telefono TEXT,
            correo TEXT,
            password TEXT
        )
    ''')
    c.execute("INSERT INTO clientes (nombre, nombreUsuario, telefono, correo, password) VALUES (?, ?, ?, ?, ?)",
              (nombre, nombreUsuario, telefono, correo, password))
    conn.commit()
    conn.close()

# Título
st.title("Registro de Usuario")

# Inputs
nombre = st.text_input("Nombre")
nombreUsuario = st.text_input("Nombre de Usuario")
telefono = st.text_input("Número de Teléfono")
correo = st.text_input("Correo")
password = st.text_input("Contraseña", type="password")
confirmar_password = st.text_input("Confirmar Contraseña", type="password")


if password and confirmar_password:
    if password != confirmar_password:
        st.error("Las contraseñas no coinciden")


if st.button("Registrarme"):
    if not nombre or not nombreUsuario or not telefono or not correo or not password or not confirmar_password:
        st.error("Por favor, completa todos los campos.")
    elif len(nombreUsuario) < 3:
        st.error("El nombre de usuario debe tener al menos 3 caracteres")
    elif usuario_existe(nombreUsuario):
        st.error("Ese nombre de usuario ya está registrado. Por favor elige otro.")
    elif password != confirmar_password:
        st.error("Las contraseñas no coinciden")
    else:
        guardar_usuario(nombre, nombreUsuario, telefono, correo, password)
        st.success("Usuario registrado con éxito ✅")
