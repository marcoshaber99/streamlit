import streamlit as st
import pandas as pd
from data_visualization import visualization
from predictions import predictions
from data_clustering import data_clustering


data = pd.DataFrame()

st.sidebar.header("Upload your dataset")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")


# Read the uploaded file and store it in a DataFrame
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    data = data.dropna()
    data = data.drop_duplicates()

    st.session_state["data"] = data

# button_style = "background-color:inherit; border: none; color: white; font-size: 1.5rem; margin-top: 2rem;"

# st.markdown(button_style, unsafe_allow_html=True)


if len(data) != 0:
    # visualization(data, uploaded_file)
    if st.sidebar.button("Data Visualization"):
        visualization()

    if st.sidebar.button("Data Prediction"):
        predictions()

    if st.sidebar.button("Data Organization"):
        data_clustering()


def get_data():
    return data
