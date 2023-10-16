import os
import sys
from WeatherCrimeHouston import logger
from WeatherCrimeHouston.exception import CustomException
import pandas as pd

from WeatherCrimeHouston.components.data_ingestion import DataIngestion
from WeatherCrimeHouston.components.data_ingestion import DataIngestionConfig

from WeatherCrimeHouston.components.data_transformation import DataTransformation
from WeatherCrimeHouston.components.data_transformation import DataTransformationConfig

from WeatherCrimeHouston.components.model_trainer import ModelTrainerConfig
from WeatherCrimeHouston.components.model_trainer import ModelTrainer


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))