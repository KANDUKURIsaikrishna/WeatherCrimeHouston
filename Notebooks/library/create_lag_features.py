"""
Created on Wed Oct  4 11:55:05 2023

@author: XQin
"""

def create_lag_features(df, column_name, lags=7):
  y = df.loc[:, column_name]
  for lag in range(lags):
    df[f"lag_{lag + 1}_{column_name}"] = y.shift(lag + 1)
  return df

