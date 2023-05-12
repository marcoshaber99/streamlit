import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import numpy as np
import sklearn.metrics as matrix
from sklearn.metrics import mean_squared_error


def predictions():
    data = st.session_state["data"]

    def create_plot(x_test, y_predictions, algo_name):
        real_x = data[x_axis].to_numpy()
        real_y = data[y_axis].to_numpy()

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
        # Scatter and line plot together
        axes.scatter(x_test, y_predictions, color="red", label="Sine")
        axes.plot(real_x, real_y, color="green", label="Tangent")
        axes.set_xlabel(x_axis)
        axes.set_ylabel(y_axis)
        axes.set_title(algo_name)
        axes.legend()

        # Remove empty subplot
        # fig.delaxes(axes[1, 1])
        # Adjust spacing between subplots
        # fig.tight_layout()
        st.pyplot(plt.gcf())

    def generate_predictions():
        algo_predictions = pd.DataFrame()

        x_train, x_test, y_train, y_test = train_test_split(
            data[x_axis].to_numpy().reshape(-1, 1),
            data[y_axis].to_numpy(),
            test_size=0.2,
        )

        for option in selected_options:
            model = algorithm_type[option]
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            print(y_pred)
            print(y_test)

            score = matrix.mean_squared_error(y_test, y_pred)

            # print(score)
            algo_predictions = pd.concat(
                [
                    algo_predictions,
                    pd.DataFrame({"Algorithm": [option], "Error Offset": [str(score)]}),
                ],
                ignore_index=True,
            )
            create_plot(x_test, y_test, option)

        st.write("Accuracy score")
        st.write(algo_predictions)

    st.title("Data Predictions")

    columns = data.columns.tolist()
    x_axis = st.selectbox("Choose Input Column", columns, on_change=predictions)
    y_axis = st.selectbox("Choose Output Column", columns, on_change=predictions)

    options = [
        "K-Nearest Neighbors",
        "Linear Regression",
        "Random Forests",
        "Support Vector Machines",
    ]
    default_option = options[0]
    selected_options = st.multiselect(
        "Select Options",
        options,
        default=default_option,
        on_change=predictions,
    )

    algorithm_type = {
        "K-Nearest Neighbors": KNeighborsRegressor(),
        "Linear Regression": LinearRegression(),
        "Random Forests": RandomForestRegressor(),
        "Support Vector Machines": SVR(),
    }

    if len(selected_options) > 0:
        generate_predictions()
