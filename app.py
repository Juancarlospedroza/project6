#app en python
import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Autos a la venta')
st.write('Aquí puedes encontrar los autos que tenemos disponibles')

# Data frame limpio para usarse
car_data = pd.read_csv('notebooks/vehicles_clean_df.csv')

hist_button = st.button('Precios de nuestros autos') # crear un botón
if hist_button: # al hacer clic en el botón
    st.write('Distribución de los precios')
    fig = px.histogram(car_data, nbins=500, x="price")
    fig.update_xaxes(range=[1000, 50000])
    st.plotly_chart(fig, use_container_width=True)