"""
   run the app : streamlit run app.py 
"""
import streamlit as st
import pandas as pd
import joblib
from src.WeatherCrimeHouston.pipeline.predict_pipeline import CustomData, PredictPipeline  # Replace with the actual module name

# Load your model
model = joblib.load("artifacts/model.pkl")

# Load the preprocessor
preprocessor = joblib.load("artifacts/preprocessor.pkl")

# Define unique values for categorical columns
unique_week = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
unique_season = ['Winter', 'Spring', 'Summer', 'Autumn']
unique_is_holiday = [1, 0]
unique_is_weekend = [0, 1]
unique_snow = [0.0, 0.2]
unique_snowdepth = [0.0, 0.1, 0.7, 2.3, 0.2]
unique_preciptype = ['none', 'rain', 'rain,snow', 'snow']
unique_conditions = ['cloudy', 'clear', 'rain', 'snow']

def main():
    st.title("Crime Rate Prediction App")

    # Create a form for user input
    st.sidebar.header("Input Data")
    date = st.sidebar.date_input("Date")
    week = st.sidebar.selectbox("Week", unique_week)
    sunrise_hour = st.sidebar.number_input("Sunrise Hour")
    sunrise_min = st.sidebar.number_input("Sunrise Minute")
    sunrise_sec = st.sidebar.number_input("Sunrise Second")
    sunset_hour = st.sidebar.number_input("Sunset Hour")
    sunset_min = st.sidebar.number_input("Sunset Minute")
    sunset_sec = st.sidebar.number_input("Sunset Second")
    season = st.sidebar.selectbox("Season", unique_season)
    is_holiday = st.sidebar.selectbox("Is Holiday", unique_is_holiday)
    is_weekend = st.sidebar.selectbox("Is Weekend", unique_is_weekend)
    snow = st.sidebar.number_input("Snow")
    snowdepth = st.sidebar.selectbox("Snow Depth", unique_snowdepth)
    temp = st.sidebar.number_input("Temperature")
    precip = st.sidebar.number_input("Precipitation")
    precipprob = st.sidebar.number_input("Precipitation Probability")
    preciptype = st.sidebar.selectbox("Precipitation Type", unique_preciptype)
    windgust = st.sidebar.number_input("Wind Gust")
    winddir = st.sidebar.number_input("Wind Direction")
    solarradiation = st.sidebar.number_input("Solar Radiation")
    moonphase = st.sidebar.number_input("Moon Phase")
    conditions = st.sidebar.selectbox("Conditions", unique_conditions)

    if st.sidebar.button("Predict Crime Rate"):
        # Create a CustomData object from the user input
        input_data = CustomData(
            date=date,
            week=week,
            sunrise_hour=sunrise_hour,
            sunrise_min=sunrise_min,
            sunrise_sec=sunrise_sec,
            sunset_hour=sunset_hour,
            sunset_min=sunset_min,
            sunset_sec=sunset_sec,
            season=season,
            is_holiday=is_holiday,
            is_weekend=is_weekend,
            snow=snow,
            snowdepth=snowdepth,
            temp=temp,
            precip=precip,
            precipprob=precipprob,
            preciptype=preciptype,
            windgust=windgust,
            winddir=winddir,
            solarradiation=solarradiation,
            moonphase=moonphase,
            conditions=conditions
        )

        pred_df = input_data.get_data_as_data_frame()

        # Apply the preprocessor to the input data
        transformed_data = preprocessor.transform(pred_df)

        # Make predictions using the model
        predicted_crime_rate = model.predict(transformed_data)

        st.write("Predicted Crime Rate (Offense Count):")
        st.write(predicted_crime_rate)

if __name__ == "__main__":
    main()
