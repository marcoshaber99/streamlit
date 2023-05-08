import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualization(data,uploaded_file):
    # Set up the Streamlit app
    # st.set_page_config(page_title="Interactive Data Visualization App", layout="wide")
    st.title("Interactive Data Visualization App")

    # Add a file uploader to the sidebar
     
    st.write("Data preview:")
    st.write(data.head())

    if uploaded_file is not None:
        columns = data.columns.tolist()
        x_axis = st.selectbox("Choose the X-axis", columns)
        y_axis = st.selectbox("Choose the Y-axis", columns)


    # Supported plot types
    plot_types = {
        "Scatter plot": sns.scatterplot,
        "Line plot": sns.lineplot,
        "Bar plot": sns.barplot,
        "Box plot": sns.boxplot,
        "Histogram": sns.histplot,
    }

    # Add a plot type selection dropdown to the sidebar
    plot_type = st.selectbox("Choose a plot type", options=list(plot_types.keys()))


    if uploaded_file is not None:
        plot_function = plot_types[plot_type]
        plt.figure(figsize=(12, 6))
        plot_function(data=data, x=x_axis, y=y_axis)
        st.pyplot(plt.gcf())


