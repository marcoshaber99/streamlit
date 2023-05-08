import streamlit as st
import pandas as pd
from test import test
from data_visualization import visualization
import util

#data = pd.DataFrame()
# from data_visualization import visualization
st.sidebar.header("Upload your dataset")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    # Read the uploaded file and store it in a DataFrame
if uploaded_file is not None:
    util.data = pd.read_csv(uploaded_file)

# button_style = "background-color:inherit; border: none; color: white; font-size: 1.5rem; margin-top: 2rem;"

# st.markdown(button_style, unsafe_allow_html=True)


if len(util.data) != 0:
    # visualization(data, uploaded_file)
    if(st.sidebar.button("Data Visualization")):
        visualization(data, uploaded_file)

    
    if(st.sidebar.button("Data Prediction")):
        pass

    if(st.sidebar.button("Data Organization")):
        pass
