#app en python
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Esto está muy macabro')
st.write('presiona el botón si te atreves')

# Data frame limpio para usarse
car_data = pd.read_csv('notebooks/vehicles_clean_df.csv')

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('dale clic')
if build_histogram:
    st.write('Tu suegra está atrás de ti D:')