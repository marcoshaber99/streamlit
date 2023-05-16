import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.cluster import BisectingKMeans
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt
import pandas as pd


def data_clustering(callback_func=None):
    st.title("Data Organization")

    def on_generate_handler():
        data_clustering(train_model)

    data = st.session_state["data"]

    def train_model():
        if number_of_clusters > 0:
            model = algorithm_types[algorithm_type](number_of_clusters)
            clustering_data = data[[input_column_X, input_column_Y]].to_numpy()

            model.fit(clustering_data)

            labels = model.labels_

            # Get the coordinates of the cluster centers
            centers = model.cluster_centers_

            plt.figure(figsize=(12, 8))
            plt.scatter(
                clustering_data[:, 0],
                clustering_data[:, 1],
                c=labels,
                cmap="viridis",
                label="Clusters",
            )
            plt.scatter(
                centers[:, 0],
                centers[:, 1],
                c="red",
                marker="X",
                s=100,
                label="Centroids",
            )
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            plt.title("Clustering Results")
            plt.legend()
            st.pyplot(plt)

    algorithm_types = {
        "K-Means": KMeans,
        "KMedoids": KMedoids,
        "Bisecting Kmeans": BisectingKMeans,
    }

    algorithm_type = st.selectbox(
        "Choose an algorithm",
        options=list(algorithm_types.keys()),
        key="algorithm_type",
        on_change=data_clustering,
    )

    input_column_X = st.selectbox(
        "Choose X Column",
        data.columns,
        key="input_column_X",  # Added unique key
        on_change=data_clustering,
    )

    input_column_Y = st.selectbox(
        "Choose Y Column",
        data.columns,
        key="input_column_Y",  # Added unique key
        on_change=data_clustering,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    number_of_clusters = st.number_input(
        "Enter amount of clusters",
        on_change=data_clustering,
        format="%d",
        min_value=1,
        max_value=10,
        key="number_of_clusters",  # Added unique key
    )

    number_of_clusters = int(number_of_clusters)

    print(number_of_clusters)

    st.button("Generate", on_click=on_generate_handler)

    if callback_func != None:
        callback_func()
