"""
Module: Data Preprocessing
Author: Silvio Christian, Joe
Description: 
    Contains utility functions to format user input from the Streamlit frontend 
    into a structure compatible with the model's expected input.
"""

def preprocess_input(preg, glu, bp, skin, ins, bmi, dpf, age):
    """
    Organizes individual input features into a single list structure.
    
    Args:
        preg (float): Number of pregnancies.
        glu (float): Glucose level.
        bp (float): Blood pressure.
        skin (float): Skin thickness.
        ins (float): Insulin level.
        bmi (float): Body Mass Index.
        dpf (float): Diabetes Pedigree Function.
        age (float): Age of the patient.
        
    Returns:
        list: A list containing the ordered features for the model.
    """
    return [preg, glu, bp, skin, ins, bmi, dpf, age]
