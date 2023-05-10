import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def visualization():
    data = st.session_state["data"]

    st.title("Data Visualization")
    st.write(data.head())
    # Add a file uploader to the sidebar
     



    columns = data.columns.tolist()
    x_axis = st.selectbox("Choose the X-axis", columns, on_change = visualization)
    y_axis = st.selectbox("Choose the Y-axis", columns, on_change = visualization)


    # Supported plot types
    plot_types = {
        "Scatter plot": sns.scatterplot,
        "Line plot": sns.lineplot,
        "Bar plot": sns.barplot,
        "Box plot": sns.boxplot,
        "Histogram": sns.histplot,
    }

    # Add a plot type selection dropdown to the sidebar
    plot_type = st.selectbox("Choose a plot type", options=list(plot_types.keys()), on_change=visualization)


    
    plot_function = plot_types[plot_type]
    plt.figure(figsize=(12, 6))
    plot_function(data=data, x=x_axis, y=y_axis)
    st.pyplot(plt.gcf())



