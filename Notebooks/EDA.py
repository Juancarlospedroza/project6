# -*- coding: utf-8 -*-
"""EDA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gfrefxeYCsVNPlXZYNwFszVgztaqyhFx
"""

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.histogram(car_data, x="odometer", nbins=50) # crear un histograma
fig.show() # crear gráfico de dispersión

fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión