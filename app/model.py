"""
Module: Model Loader & Inference
Author: Silvio Christian, Joe
Description: 
    This module handles the loading of pre-trained machine learning models 
    (Scaler and Random Forest) and provides a function to generate predictions.
"""

from sklearn.preprocessing import MinMaxScaler
import joblib

def load_model():
    """
    Loads the pre-trained scaler and machine learning model from disk.
    
    Returns:
        scaler: The fitted MinMaxScaler object.
        model_rf: The trained Random Forest Classifier.
    """
    # Load the serialized scaler and model
    scaler = joblib.load("models/scaler.joblib")
    model_rf = joblib.load("models/model_rf.joblib")
    return scaler, model_rf

def predict(model, scaler, input_data):
    """
    Prepares input data and generates a prediction using the loaded model.
    
    Args:
        model: The trained machine learning model.
        scaler: The fitted scaler for normalization.
        input_data (list): A list of feature values [pregnancies, glucose, ...].
        
    Returns:
        int: The predicted class (0 for Non-Diabetic, 1 for Diabetic).
    """
    # Scale the input data using the same scaler used during training
    input_scaled = scaler.transform([input_data])
    
    # Predict the class label (0 or 1).
    # [0] extracts the single integer result from the array.
    result = model.predict(input_scaled)[0]

    # Calculate the confidence score of the WINNING class.
    # LOGIC: We use .max() because we want to know how sure the model is about its decision.
    # - If it predicts 0 (Healthy), we want the probability of 0.
    # - If it predicts 1 (Diabetes), we want the probability of 1.
    # Example: If Probs are [0.8, 0.2] -> It predicts 0, and Confidence is 0.8 (80%).
    conf = model.predict_proba(input_scaled).max(axis=1)
    
    return result, conf
