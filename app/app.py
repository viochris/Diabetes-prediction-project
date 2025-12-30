"""
Project: Diabetes Prediction Web App
Author: Silvio Christian, Joe
Description: 
    The main Streamlit application entry point. It renders the user interface, 
    captures patient data via a form, and displays prediction results 
    by calling the backend logic.
"""

import streamlit as st
import numpy as np
from model import load_model, predict
from preprocess import preprocess_input

# ==========================================
# 1. Load Resources
# ==========================================
# Initialize the model and scaler once when the script runs
scaler, model_rf = load_model()

# ==========================================
# 2. UI Layout - Header
# ==========================================
st.header("🩺 Diabetes Prediction App")
st.write("Enter patient details below to predict the likelihood of diabetes.")

# ==========================================
# 3. UI Layout - Input Form
# ==========================================
# Using a form ensures the prediction runs only when the button is clicked
with st.form("prediction_form"):
  name = st.text_input("👤 Patient Name", value="Susy")

  # Numeric inputs for health metrics
  pregnancies = st.number_input("🤰 Number of Pregnancies", min_value=0.0, step=1.0, value=6.0)
  glucose = st.number_input("🍬 Glucose Level", min_value=0.0, value=148.0, step=1.0)
  blood_pressure = st.number_input("🩸 Blood Pressure", min_value=0.0, value=72.0, step=1.0)
  skin_thickness = st.number_input("📏 Skin Thickness", min_value=0.0, value=35.0, step=1.0)
  insulin = st.number_input("💉 Insulin Level", min_value=0.0, value=168.0, step=1.0)
  bmi = st.number_input("⚖️ Body Mass Index (BMI)", min_value=0.0, value=43.1)
  dpf = st.number_input("🧬 Diabetes Pedigree Function (DPF)", min_value=0.0, value=2.288)
  age = st.number_input("📅 Age", min_value=0.0, max_value=120.0, value=33.0, step=1.0)

  # Submit button
  submitted = st.form_submit_button("🚀 Predict")

# ==========================================
# 4. Prediction Logic
# ==========================================
if submitted:
  # Preprocess the raw input data into a list
  input_value = preprocess_input(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)
  
  # Run inference
  prediction = predict(model_rf, scaler, input_value)
  
  # Interpret the result
  result, conf = "🟥 Diabetic" if prediction == 1 else "🟩 Non-Diabetic"

  # ==========================================
  # 5. Display Results
  # ==========================================
  st.markdown("---")
  st.subheader("🔎 Prediction Result")
  st.write(f"**Name:** {name if name else 'N/A'}")
    
  # Display dynamic feedback based on the diagnosis:
  # - Class 1 (Diabetes): Use RED (st.error) to indicate health risk/alert.
  # - Class 0 (Healthy): Use GREEN (st.success) to indicate normal condition.
  if prediction == 1:
      st.error(f"**Prediction:** {result}, Confidence: {conf[0]:.2%}")
  else:
      st.success(f"**Prediction:** {result}, Confidence: {conf[0]:.2%}")
