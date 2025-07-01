import os
import sys

from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor,
    
)

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error,
    # confusion_matrix
)
from sklearn.neighbors import KNeighborsRegressor

from sklearn.tree import DecisionTreeRegressor

from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utlis import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting taining and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {
            "Decision Tree": DecisionTreeRegressor(),  # ← Moved to first position
            "Random Forest": RandomForestRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "Linear Regression": LinearRegression(),
            "K-Neighbour Regressor": KNeighborsRegressor(),
            "CatBoostRegressor": CatBoostRegressor(verbose=False),
            "Adaboost Regressor": AdaBoostRegressor(),
            "XG Boost Regressor": XGBRegressor()
        }

            params = {
            "Decision Tree": {  # ← Now matches the order in models
                'criterion': ['squared_error', 'friedman_mse', 'absolute_error'],
                'max_depth': [3, 5, 7, 10],
                'min_samples_split': [2, 5, 10]
            },
            "Random Forest": {
                'n_estimators': [8, 16, 32, 64, 128, 256]
            },
            "Gradient Boosting": {
                'learning_rate': [.1, .01, .05, .001],
                'n_estimators': [8, 16, 32, 64, 128, 256]
            },
            "Linear Regression": {},
            "K-Neighbour Regressor": {
                'n_neighbors': [5, 7, 9, 11],
            },
            "CatBoostRegressor": {
                'depth': [6, 8, 10],
                'iterations': [30, 50, 100]
            },
            "Adaboost Regressor": {
                'learning_rate': [.1, .01, 0.5, .001],
                'n_estimators': [8, 16, 32, 64, 128, 256]
            },
            "XG Boost Regressor": {
                'learning_rate': [.1, .01, .05, .001],
                'n_estimators': [8, 16, 32, 64, 128, 256]
            }
        }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models,params=params)

            ## getting the best model score from the dict
            best_model_score=max(sorted(model_report.values()))

            ## getting the best model name from dict
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found",sys)
            logging.info("Best model found on both training and testing data")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_square=r2_score(y_test,predicted)


            return r2_square

        except Exception as e:
            raise CustomException(e,sys)