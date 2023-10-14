import streamlit as st
from streamlit_shap import st_shap
import shap
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

st.header('Historical pridiction')

with open('E:\Houston\WeatherCrimeHouston\model\ebm.pkl', 'rb') as model1_file:
        model_1 = pickle.load(model1_file)


st.markdown(
    """
    <style>
    .small-font {
        font-size:12px;
        font-style: italic;
        color: #b1a7a6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.title("Streamlit ML App")
    st.sidebar.header("User Input")

def evaluate_model(y_test, pred):
    mae = mean_absolute_error(y_test, pred)
    mse = mean_squared_error(y_test, pred)
    mape = mean_absolute_percentage_error(y_test, pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, pred)

    st.subheader("Model Evaluation:")
    st.write(f"MAE: {mae}")
    st.write(f"MSE: {mse}")
    st.write(f"MAPE: {mape}")
    st.write(f"RMSE: {rmse}")
    st.write(f"R2: {r2}")

def make_predictions(model, X_test):
    pred = model.predict(X_test)
    return pred

y_test = pd.Series([1, 2, 3, 4, 5])
# Replace this with the actual test data
# y_test = load_test_data()

# Make predictions using the loaded model
predictions = make_predictions(model_1, X_test)

# Evaluate the model and display results
evaluate_model(y_test, predictions)
    
if __name__ == "__main__":
    main()

st.markdown(
    '''
    custum text  
    '''  
)
