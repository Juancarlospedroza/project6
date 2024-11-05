#app en python
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Autos a la venta')
st.write('Aquí puedes encontrar los autos que tenemos disponibles')

# Data frame limpio para usarse
car_data = pd.read_csv('notebooks/vehicles_clean_df.csv')
car_data = car_data[car_data["model_year"] > 1980]

hist_button = st.button('Precios de nuestros autos') # crear un botón
if hist_button: # al hacer clic en el botón
    st.write('Distribución de los precios')
    fig = px.histogram(car_data, nbins=500, x="price")
    fig.update_xaxes(range=[1000, 50000])
    st.plotly_chart(fig, use_container_width=True)

correlacion1 = st.checkbox('Correlación entre precio y odómetro')
if correlacion1:
    st.write("Entre mayor sea el odómetro el precio tiende a bajar")
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

correlacion2 = st.checkbox('Correlación entre precio y año del modelo')
if correlacion2:
    st.write("Entre más nuevo sea el vehículo el precio tiende a subir")
    fig = px.scatter(car_data, x="model_year", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)