import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

from WeatherCrimeHouston.exception import CustomException
from WeatherCrimeHouston import logger
import os

from WeatherCrimeHouston.utils import save_object

# Custom transformer for the 'date' column
class DateTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        reference_date = pd.to_datetime(X["date"]).min()
        X_transformed = (pd.to_datetime(X["date"]) - reference_date).dt.days
        return X_transformed.values.reshape(-1, 1)

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
         
        try:
            logger.info('Data Transformation initiated')

            numerical_cols   = ["sunrise_hour",
                                "sunrise_min",
                                "sunrise_sec",
                                "sunset_hour",
                                "sunset_min",
                                "sunset_sec",
                                "temp",
                                "precip",
                                "precipprob",
                                "windgust",
                                "winddir",
                                "solarradiation",
                                "moonphase"]
            categorical_cols = ["week",
                                "season",
                                "is_holiday",
                                "is_weekend",
                                "snow",
                                "snowdepth",
                                "preciptype",
                                "conditions"]


            logger.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )
            
            ## Categorical Pipeline
            cat_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]
            )

            return ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_cols),
                    ('cat_pipeline', cat_pipeline, categorical_cols),
                    ("date", DateTransformer(), ["date"]),
                ]
            )
        except Exception as e:

            logger.info("Error in Data Trnasformation")
            raise CustomException(e,sys) from e
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info('Read train and test data completed')
            logger.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logger.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logger.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = 'Offense Count'
            drop_columns = [target_column_name]

            ## features into independent and dependent features

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]


            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]

            ## apply the transformation

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logger.info("Applying preprocessing object on training and testing datasets.")

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            logger.info('Precesssor pickle in created and saved')

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logger.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys) from e