import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


            
def predictions():

    data = st.session_state["data"]
    
    def generate_predictions():
        X_train, X_test, y_train, y_test = train_test_split(data[x_axis].tolist(), data[y_axis].tolist(), test_size=0.2)
        for option in selected_options:
            model=algorithm_type[option]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            print(X_train)
            print(y_train)

        predictions()
    
    
    
    st.title("Data Predictions")
    
    columns = data.columns.tolist()
    x_axis = st.selectbox("Choose Input Column", columns,on_change=predictions)
    y_axis = st.selectbox("Choose Output Column", columns,on_change=predictions)
   
    
    options = ["K-Nearest Neighbors", "Linear Regression", "Random Forests","Support Vector Machines"]
    selected_options = st.multiselect("Select Options", options, on_change=predictions)
    st.button("Generate Prediction", on_click=generate_predictions)
    
    algorithm_type = {
        "K-Nearest Neighbors": KNeighborsRegressor(),
        "Linear Regression": LinearRegression(),
        "Random Forests": RandomForestRegressor(),
        "Support Vector Machines": SVR()
    }


