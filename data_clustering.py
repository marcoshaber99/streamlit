import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.cluster import BisectingKMeans
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt
import pandas as pd

import io


def data_clustering():
    def save_plot_as_pdf(fig):
        pdf_bytes = io.BytesIO()
        fig.savefig(pdf_bytes, format="pdf", bbox_inches="tight")
        plt.close(fig)
        pdf_bytes.seek(0)
        return pdf_bytes

    st.title("Data Organization")

    # fetching the data stored in the session state
    data = st.session_state["data"]

    st.write(data.head())

    def train_model():
        if number_of_clusters > 0:
            # instance of the chosen clustering model
            model = algorithm_types[algorithm_type](number_of_clusters)

            clustering_data = data[[input_column_X, input_column_Y]].to_numpy()

            # train model
            model.fit(clustering_data)

            labels = model.labels_

            # Get the coordinates of the cluster centers
            centers = model.cluster_centers_

            fig, ax = plt.subplots(figsize=(12, 8))
            ax.scatter(
                clustering_data[:, 0],
                clustering_data[:, 1],
                c=labels,
                cmap="viridis",
                label="Clusters",
            )
            ax.scatter(
                centers[:, 0],
                centers[:, 1],
                c="red",
                marker="X",
                s=100,
                label="Centroids",
            )
            ax.set_xlabel("Feature 1")
            ax.set_ylabel("Feature 2")
            ax.set_title("Clustering Results")
            ax.legend()

            # Save the plot as a PDF
            pdf_bytes = save_plot_as_pdf(fig)
            st.download_button(
                label="Download Plot as PDF",
                data=pdf_bytes,
                file_name="clustering_results.pdf",
                mime="application/pdf",
            )

            st.pyplot(fig)

    algorithm_types = {
        "K-Means": KMeans,
        "KMedoids": KMedoids,
        "Bisecting Kmeans": BisectingKMeans,
    }

    algorithm_type = st.selectbox(
        "Choose an algorithm",
        options=list(algorithm_types.keys()),
        key="algorithm_type",
    )

    input_column_X = st.selectbox(
        "Choose X Column",
        data.columns,
        key="input_column_X",
    )

    input_column_Y = st.selectbox(
        "Choose Y Column",
        data.columns,
        key="input_column_Y",
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    number_of_clusters = st.number_input(
        "Enter amount of clusters",
        format="%d",
        min_value=1,
        max_value=10,
        key="number_of_clusters",
    )

    number_of_clusters = int(number_of_clusters)

    if st.button("Generate"):
        train_model()
