import pandas as pd
import streamlit as st

st.header('Data frame')
st.write('Este es el dataframe completo de los vehículos.')

data = pd.read_csv('notebooks/vehicles_clean_df.csv')
st.write(data)