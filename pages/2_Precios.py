import pandas as pd
import streamlit as st

st.header('Nuestros autos')
st.write('Encuentra tu auto ideal')

opcion = st.selectbox(
    "Elige el rango de precio de tu auto", 
    ["Menos de 10,000 DLS", "De 10,000 a menos de 20,000 DLS", 
     "De 20,000 a menos de 30,000 DLS", "De 30,000 a menos de 40,000 DLS",
     "Más de 40,000 DLS"]
)

df = pd.read_csv('notebooks/vehicles_clean_df.csv')

if opcion == "Menos de 10,000 DLS":
    st.dataframe(df[df["price"] < 10000].sort_values(by="price").reset_index(drop=True))

if opcion == "De 10,000 a menos de 20,000 DLS":
    st.dataframe(df[(df["price"] >= 10000) & (df["price"] < 20000)].sort_values(by="price").reset_index(drop=True))


if opcion == "Más de 40,000 DLS":
    st.dataframe(df[df["price"] > 40000].sort_values(by="price").reset_index(drop=True))