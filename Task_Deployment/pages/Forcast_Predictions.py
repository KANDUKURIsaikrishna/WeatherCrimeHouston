import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import warnings

warnings.filterwarnings('ignore')
st.header('Forcast Prediction')
data_dir = "../data/Deployment/"
august_df = pd.read_csv(data_dir + "august_predict_data.csv")
sep_df = pd.read_csv(data_dir + "predicted_september_crime.csv")
model_path = "../model/"

def predict_august(data):
    with open(model_path + "ebm.pkl", "rb") as model_file:
        ebm = pickle.load(model_file)
    predictions = ebm.predict(data)
    return predictions

X_data2308 = august_df.drop('Offense Count', axis=1)

def plot_actual_vs_predicted_august(data, predictions):
    fig, ax = plt.subplots(figsize=(10, 6))

    date = data['date'].to_numpy()
    actual = data['Offense Count'].to_numpy()

    ax.plot(date, actual, label='Actual', marker='o', linestyle='-', markersize=5)
    ax.plot(date, predictions, label='Predicted', marker='o', linestyle='-', markersize=5)
    ax.set_xticklabels(date, rotation=90)
    ax.xaxis.set_major_locator(plt.FixedLocator(np.arange(len(date))))
    ax.set_xlabel('Date')
    ax.set_ylabel('Crime Rate')
    ax.set_title('Actual vs. Predicted Crime Rate (August)')
    ax.grid(True)
    ax.legend()
    return fig

def plot_predicted_september(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    date = data['date'].to_numpy()
    predicted = data['Offense Count'].to_numpy()

    ax.plot(date, predicted, label='Predicted', marker='o', linestyle='-', markersize=5, color='orange')
    ax.set_xticklabels(date, rotation=90)
    ax.xaxis.set_major_locator(plt.FixedLocator(np.arange(len(date))))
    ax.set_xlabel('date')
    ax.set_ylabel('Crime Rate')
    ax.set_title('Predicted Crime Rate (September)')
    ax.grid(True)
    ax.legend()
    return fig

st.markdown(
    """
    # Discovering the Relationship Between Crime Statistics and Weather in the Houston Area
    """
)

selected_month = st.selectbox("Select Month", ['August', 'September'])

if selected_month == 'August':
    predictions = predict_august(X_data2308)
    st.pyplot(plot_actual_vs_predicted_august(august_df, predictions))
    st.dataframe({'Date': X_data2308['date'], 'Predicted': [round(i, 0) for i in predictions]})
else:
    st.pyplot(plot_predicted_september(sep_df))
    st.dataframe({'Date': sep_df['date'], 'Predicted': sep_df['Offense Count']})

