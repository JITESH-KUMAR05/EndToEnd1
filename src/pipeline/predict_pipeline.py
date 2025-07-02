import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utlis import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Try different path approaches
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            
            # Debug: Print current working directory and check file existence
            print(f"Current working directory: {os.getcwd()}")
            print(f"Model file exists: {os.path.exists(model_path)}")
            print(f"Preprocessor file exists: {os.path.exists(preprocessor_path)}")
            
            # List all files in current directory
            print("Files in current directory:")
            for item in os.listdir('.'):
                print(f"  {item}")
            
            # Check if artifacts folder exists
            if os.path.exists('artifacts'):
                print("Contents of artifacts folder:")
                for item in os.listdir('artifacts'):
                    print(f"  artifacts/{item}")
            else:
                print("❌ Artifacts folder does not exist!")
                raise FileNotFoundError("Artifacts folder not found")
            
            # Load the actual trained model and preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            print(f"✅ Model loaded successfully: {type(model)}")
            print(f"✅ Preprocessor loaded successfully: {type(preprocessor)}")
            
            # Make actual prediction using your trained model
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            rounded_preds = [round(pred, 2) for pred in preds]
            
            print(f"✅ Prediction successful: {rounded_preds}")
            return rounded_preds
            
        except Exception as e:
            print(f"🔴 Error in prediction: {str(e)}")
            print(f"🔴 Error type: {type(e).__name__}")
            
            # Only use fallback if absolutely necessary
            print("⚠️  Using fallback prediction - MODEL NOT LOADED!")
            raise CustomException(e, sys)


class CustomData:
    def __init__(
            self,
            gender:str,
            race_ethnicity:str,
            parental_level_of_education:str,
            lunch:str,
            test_preparation_course:str,
            reading_score:int,
            writing_score:int,
    ):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)