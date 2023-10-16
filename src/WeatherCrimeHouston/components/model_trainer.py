import os
import sys
from dataclasses import dataclass

from sklearn.metrics import r2_score
from xgboost import XGBRegressor

from WeatherCrimeHouston.exception import CustomException
from WeatherCrimeHouston import logger

from WeatherCrimeHouston.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logger.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "XGBRegressor": XGBRegressor(),

            }
            params={
                "XGBRegressor":{
                    'subsample': [0.9],
                    'reg_lambda': [0.1],
                    'reg_alpha': [0.1],
                    'random_state': [100],
                    'objective': ["reg:squarederror"],
                    'n_estimators': [200],
                    'max_depth': [3],
                    'learning_rate': [0.1],
                    'gamma': [0.2],
                    'colsample_bytree' : [0.8],
                },
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logger.info("Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            return r2_score(y_test, predicted)
        except Exception as e:
            raise CustomException(e,sys) from e