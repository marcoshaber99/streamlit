import streamlit as st
import pandas as pd
from data_visualization import visualization
from predictions import predictions
from data_clustering import data_clustering


data = pd.DataFrame()

st.sidebar.header("Upload your dataset")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

routes = {
    "visualization": visualization,
    "predictions": predictions,
    "organazations": data_clustering,
}

# Read the uploaded file and store it in a DataFrame
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    data = data.dropna()
    data = data.drop_duplicates()

    st.session_state["data"] = data


if "data" in st.session_state:
    # visualization(data, uploaded_file)
    if st.sidebar.button("Data Visualization"):
        st.session_state["route"] = "visualization"

    if st.sidebar.button("Data Prediction"):
        st.session_state["route"] = "predictions"

    if st.sidebar.button("Data Organization"):
        st.session_state["route"] = "organazations"

    if "route" in st.session_state:
        st.write(st.session_state["route"])
        routes[st.session_state["route"]]()


def get_data():
    return data
