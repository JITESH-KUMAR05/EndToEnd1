#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import (
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import os

# Add src to path
sys.path.append('/home/jitesh/Desktop/Programing/Python/EndToEnd1')
from src.utlis import evaluate_models, load_object

def test_model_selection():
    try:
        # Load the actual data used for training
        train_df = pd.read_csv('artifacts/train.csv')
        X = train_df.drop('math_score', axis=1)
        y = train_df['math_score']
        
        # Load preprocessor and transform data
        preprocessor = load_object('artifacts/preprocessor.pkl')
        X_transformed = preprocessor.transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_transformed, y, test_size=0.2, random_state=42
        )
        
        # Define models (simplified - without CatBoost and XGBoost for now)
        models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest": RandomForestRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "AdaBoost": AdaBoostRegressor(),
            "K-Neighbors": KNeighborsRegressor()
        }
        
        # Simple parameters for quick testing
        params = {
            "Linear Regression": {},
            "Decision Tree": {'max_depth': [5, 10]},
            "Random Forest": {'n_estimators': [50, 100]},
            "Gradient Boosting": {'n_estimators': [50, 100]},
            "AdaBoost": {'n_estimators': [50, 100]},
            "K-Neighbors": {'n_neighbors': [5, 7]}
        }
        
        print("🔍 Testing models...")
        
        # Evaluate models
        model_report = evaluate_models(X_train, y_train, X_test, y_test, models, params)
        
        print("\n📊 Model Performance Results:")
        print("-" * 40)
        sorted_models = sorted(model_report.items(), key=lambda x: x[1], reverse=True)
        
        for name, score in sorted_models:
            print(f"{name:<20}: {score:.4f}")
        
        best_model_name = sorted_models[0][0]
        best_score = sorted_models[0][1]
        
        print(f"\n🏆 Best Model: {best_model_name}")
        print(f"🎯 Best R² Score: {best_score:.4f}")
        
        # Check what model is actually saved
        try:
            saved_model = load_object('artifacts/model.pkl')
            print(f"\n💾 Currently saved model: {type(saved_model).__name__}")
        except:
            print("\n❌ No saved model found")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_model_selection()
