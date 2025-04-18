import streamlit as st
import sqlite3
import os
from User import Usuario  # Asegúrate de que esté bien escrito (respetar mayúscula U)

st.set_page_config(page_title="Registro", layout="centered")

# Función para crear una base de datos limpia
def crear_base_nueva():
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
    conn.commit()
    conn.close()
    st.info("Se ha creado una nueva base de datos limpia.")

# Función para verificar si el usuario ya existe
def usuario_existe(nombreUsuario):
    try:
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

    except sqlite3.DatabaseError as e:
        st.error("⚠️ La base de datos está dañada o corrupta.")
        st.error(f"Detalle del error: {e}")
        if os.path.exists("clientes.db"):
            os.rename("clientes.db", "clientes_corrupta.db")
            st.warning("La base de datos corrupta se ha renombrado a 'clientes_corrupta.db'.")
            crear_base_nueva()
        return False  # Permitimos continuar porque ya se creó una base nueva

# Función para guardar un usuario nuevo
def guardar_usuario(usuario):
    try:
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
                  (usuario.nombre, usuario.nombreUsuario, usuario.telefono, usuario.correo, usuario.password))
        conn.commit()
        conn.close()

    except sqlite3.DatabaseError as e:
        st.error("⚠️ Error al guardar el usuario. La base de datos puede estar dañada.")
        st.error(f"Detalle del error: {e}")
        if os.path.exists("clientes.db"):
            os.rename("clientes.db", "clientes_corrupta.db")
            st.warning("La base de datos corrupta se ha renombrado a 'clientes_corrupta.db'.")
            crear_base_nueva()

# Interfaz con Streamlit
st.title("Registro de Usuario")

# Inputs del formulario
nombre = st.text_input("Nombre")
nombreUsuario = st.text_input("Nombre de Usuario")
telefono = st.text_input("Número de Teléfono")
correo = st.text_input("Correo")
password = st.text_input("Contraseña", type="password")
confirmar_password = st.text_input("Confirmar Contraseña", type="password")

# Validación en tiempo real
if password and confirmar_password:
    if password != confirmar_password:
        st.error("Las contraseñas no coinciden")

# Botón de registro
if st.button("Registrarme"):
    if not nombre or not nombreUsuario or not telefono or not correo or not password or not confirmar_password:
        st.error("Por favor, completa todos los campos.")
    elif len(nombreUsuario) < 3:
        st.error("El nombre de usuario debe tener al menos 3 caracteres.")
    elif usuario_existe(nombreUsuario):
        st.error("Ese nombre de usuario ya está registrado.")
    elif password != confirmar_password:
        st.error("Las contraseñas no coinciden.")
    else:
        nuevo_usuario = Usuario(nombre, nombreUsuario, telefono, correo, password)
        guardar_usuario(nuevo_usuario)
        st.success("Usuario registrado")
