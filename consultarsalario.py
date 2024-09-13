import streamlit as st
import sqlite3
import pandas as pd

# Conexión a la base de datos SQLite
def get_connection():
    
    conn = sqlite3.connect('datoslemp.db')
    return conn

# Función para consultar la base de datos según los filtros
def consulta_bd(NOMBRE, EMPLEADO):
    conn = get_connection()
    query = """
    SELECT * FROM nombre_de_la_tabla
    WHERE NOMBRE LIKE ? AND EMPLEADO LIKE ?
    """
    # Parámetros para la consulta SQL
    params = (f"%{NOMBRE}%",f"%{EMPLEADO}%")
    
    # Ejecutar la consulta
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

# Título de la aplicación
st.title("Consulta de Datos de Personas")

# Crear cuadros de entrada para nombre, apellido y empresa
empresa = st.text_input("Ingrese el nombre de la Empresa")
empleado = st.text_input("Ingrese el Apellido y Nombre")


# Botón para consultar
if st.button("Consultar"):
    # Verificar que los campos no estén vacíos
    if empresa or empleado:
        # Realizar consulta a la base de datos
        df = consulta_bd(empresa, empleado)
        
        # Verificar si hay resultados
        if not df.empty:
            st.write(f"Resultados encontrados para: ** en la empresa **{empresa}**")
            st.dataframe(df)  # Mostrar el DataFrame con los resultados
        else:
            st.write("No se encontraron resultados para los datos ingresados.")
    #else:
        #st.dataframe(df)  # Mostrar el DataFrame con los resultados
       # st.write("Por favor, complete todos los campos antes de consultar.")
