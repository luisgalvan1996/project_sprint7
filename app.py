import pandas as pd
import plotly.express as px
import streamlit as st

# Header
st.title('Análisis de vehículos usados por Luis Galván')

# Cargar los datos
try:
    car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que este archivo esté en la misma carpeta que el script
    st.write('Datos cargados correctamente.')
except FileNotFoundError:
    st.error("El archivo 'vehicles_us.csv' no se encuentra en la ubicación especificada.")
    car_data = None

if car_data is not None:
    # Botón para histograma
    hist_button = st.button('Construir histograma')

    if hist_button:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig, use_container_width=True)

    # Botón para gráfico de dispersión
    scatter_button = st.button('Construir gráfico de dispersión')

    if scatter_button:
        st.write('Creación de un gráfico de dispersión entre odómetro y precio')
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig, use_container_width=True)
