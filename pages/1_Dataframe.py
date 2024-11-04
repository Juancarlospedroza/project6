import pandas as pd
import streamlit as st

st.header('Data frame')
st.write('Este es el dataframe ya limpio del cual se generan las gráficas que se muestran en los demás apartados.')

data = pd.read_csv('notebooks/vehicles_clean_df.csv')
st.write(data)