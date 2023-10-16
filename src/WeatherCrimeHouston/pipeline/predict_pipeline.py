import os
import sys
import pandas as pd
from WeatherCrimeHouston.exception import CustomException
from WeatherCrimeHouston import logger
from WeatherCrimeHouston.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            return model.predict(data_scaled)
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
        
class CustomData:
    def __init__(  self,
        date           : object,
        week           : object,
        sunrise_hour   : int,  
        sunrise_min    : int, 
        sunrise_sec    : int,  
        sunset_hour    : int,
        sunset_min     : int, 
        sunset_sec     : int, 
        season         : object, 
        is_holiday     : int,  
        is_weekend     : int,  
        snow           : float,
        snowdepth      : float,
        temp           : float,
        precip         : float,
        precipprob     : int, 
        preciptype     : object, 
        windgust       : float,
        winddir        : float,
        solarradiation : float,
        moonphase      : float,
        conditions     : object):
        
        self.date           = date          
        self.week           = week          
        self.sunrise_hour   = sunrise_hour  
        self.sunrise_min    = sunrise_min   
        self.sunrise_sec    = sunrise_sec   
        self.sunset_hour    = sunset_hour   
        self.sunset_min     = sunset_min    
        self.sunset_sec     = sunset_sec    
        self.season         = season        
        self.is_holiday     = is_holiday    
        self.is_weekend     = is_weekend    
        self.snow           = snow          
        self.snowdepth      = snowdepth     
        self.temp           = temp          
        self.precip         = precip        
        self.precipprob     = precipprob    
        self.preciptype     = preciptype    
        self.windgust       = windgust      
        self.winddir        = winddir       
        self.solarradiation = solarradiation
        self.moonphase      = moonphase     
        self.conditions     = conditions    


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                
                "date" : [self.date],
                "week" : [self.week],
                "sunrise_hour" : [self.sunrise_hour],
                "sunrise_min" : [self.sunrise_min],
                "sunrise_sec" : [self.sunrise_sec],
                "sunset_hour" : [self.sunset_hour],
                "sunset_min" : [self.sunset_min],
                "sunset_sec" : [self.sunset_sec],
                "season" : [self.season],
                "is_holiday" : [self.is_holiday],
                "is_weekend" : [self.is_weekend],
                "snow" : [self.snow],
                "snowdepth" : [self.snowdepth],
                "temp" : [self.temp],
                "precip" : [self.precip],
                "precipprob" : [self.precipprob],
                "preciptype" : [self.preciptype],
                "windgust" : [self.windgust],
                "winddir" : [self.winddir],
                "solarradiation" : [self.solarradiation],
                "moonphase" : [self.moonphase],
                "conditions" : [self.conditions],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys) from e