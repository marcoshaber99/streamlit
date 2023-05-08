import streamlit as st
import pandas as pd
from test import test
from data_visualization import visualization

data = pd.DataFrame()
# from data_visualization import visualization
test()
st.sidebar.header("Upload your dataset")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    # Read the uploaded file and store it in a DataFrame
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

visualization(data,uploaded_file)