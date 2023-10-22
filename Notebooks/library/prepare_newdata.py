"""
Created on Fri Oct 20, 2023

@author: XQin
"""
import pandas as pd
import holidays

# Create holiday object for Texas, USA for the years 2010 through 2023
us_tx_holidays = holidays.US(years=range(2010, 2024), state='TX')

# Extract only federal holiday dates
fed_holidays = ["New Year's Day", "Independence Day", "Thanksgiving", "Martin Luther King Jr. Day",
                "Washingtons Birthday", "Memorial Day", "Labor Day", "Columbus Day", "Veterans Day",
                "Friday After Thanksgiving", "Christmas Day", "New Year's Day (Observed)", "Independence Day (Observed)",
                "Thanksgiving (Observed)", "Martin Luther King Jr. Day (Observed)", "Washingtons Birthday (Observed)",
                "Memorial Day (Observed)", "Labor Day (Observed)", "Columbus Day (Observed)", "Veterans Day (Observed)",
                "Friday After Thanksgiving (Observed)", "Christmas Day (Observed)"]

holidays_dates = [k for k, v in us_tx_holidays.items() if v in fed_holidays]

def prepare_newdata(df):
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Create a new variable 'is_holiday'
    df['is_holiday'] = [1 if day.date() in holidays_dates else 0 for day in df['datetime']]

    # Create a variable 'is_weekend'
    df['is_weekend'] = [1 if day.isoweekday() > 5 else 0 for day in df['datetime']]
    
    # create columns of 'week', 'month', 'year', 'mon_year', 'season'
    df['week'] = df['datetime'].map(lambda m: m.day_name())
    df['month'] = df['datetime'].map(lambda m: m.month) 
    df['year']= df['datetime'].map(lambda m: m.year)
    df['mon_year'] = df['datetime'].map(lambda m: m.strftime('%b-%Y')) 
    df['season'] = df['datetime'].map(lambda m: (m.month % 12) // 3 + 1)
    df['season'] =df['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'})

    # encode week and season features
    columns = ["week", "season"] # "icon",  "preciptype"
    dummies = pd.get_dummies(df[columns])
    df = pd.concat([df, dummies], axis='columns')
    season_names = ['season_Spring', 'season_Summer', 'season_Autumn', 'season_Winter']
    for season_name in season_names:
        if season_name not in df.columns:
            df[season_name] = False
    
    # encoded weather conditions column
    encoded_column_names = ['Clear', 'Overcast', 'Partially cloudy', 'Rain', 'Snow']
    df[encoded_column_names] = 0
    for name in encoded_column_names:
        row = df['conditions'].str.contains(name)
        df.loc[row, name] =  1
    df.rename(columns={'Partially cloudy': 'Partiallycloudy', 'datetime': 'date'}, inplace=True)
    
    # Calculate the time difference between 'sunset' and 'sunrise'
    # and extract the daytime interval in seconds for numerical analysis
    df['sunset'] = pd.to_datetime(df['sunset']).dt.time 
    df['sunrise'] = pd.to_datetime(df['sunrise']).dt.time 
    df['sunset'] = pd.to_datetime(df['sunset'], format='%H:%M:%S')
    df['sunrise'] = pd.to_datetime(df['sunrise'], format='%H:%M:%S')
   
    df['daytime_interval'] = (df['sunset']- df['sunrise']).dt.total_seconds()

    # columns to drop
    cols = [
        'week',
        'season',
        'icon',
        'mon_year',
        'preciptype',
        'sunrise',
        'sunset',
        'solarenergy',
        'description',
        'stations',
        'snow',
        'snowdepth',
        'precipprob',
        'conditions',
        'name',
        'severerisk'
    ]
    return df.drop(columns=cols, axis=1).set_index('date')
