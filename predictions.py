import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

def predictions(data):
    columns = data.columns.tolist()
    x_axis = st.selectbox("Choose Input Column", columns)
    y_axis = st.selectbox("Choose Output Column", columns)


