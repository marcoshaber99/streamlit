import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


def visualization():
    def save_plot_as_pdf(fig):
        pdf_bytes = io.BytesIO()
        fig.savefig(pdf_bytes, format="pdf", bbox_inches="tight")
        plt.close(fig)
        pdf_bytes.seek(0)
        return pdf_bytes

    data = st.session_state["data"]

    st.title("Data Visualization")
    st.write(data.head())

    columns = data.columns.tolist()
    x_axis = st.selectbox("Choose the X-axis", columns, key="x-axis")
    y_axis = st.selectbox("Choose the Y-axis", columns, key="y-axis")

    # Supported plot types
    plot_types = {
        "Scatter plot": sns.scatterplot,
        "Line plot": sns.lineplot,
        "Bar plot": sns.barplot,
        "Box plot": sns.boxplot,
        "Histogram": sns.histplot,
    }

    # Add a plot type selection dropdown to the sidebar
    plot_type = st.selectbox(
        "Choose a plot type", options=list(plot_types.keys()), key="plot"
    )

    plot_function = plot_types[plot_type]
    fig, ax = plt.subplots(figsize=(12, 8))
    plot_function(data=data, x=x_axis, y=y_axis)
    st.pyplot(plt.gcf())

    pdf_bytes = save_plot_as_pdf(fig)
    st.download_button(
        label="Download Plot as PDF",
        data=pdf_bytes,
        file_name="visualizations.pdf",
        mime="application/pdf",
    )
