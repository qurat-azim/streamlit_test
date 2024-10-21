import streamlit as st
import pandas as pd
import numpy as np

st.title('My first app')

st.write("Hello World!!")

penguins = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/penguins.csv')

st.scatter_chart(data=penguins, x='culmen_length_mm', y='body_mass_g', x_label="Culmen Length", y_label="Body Mass")