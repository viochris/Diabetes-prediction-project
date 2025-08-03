# 🩺 Diabetes Prediction App

A complete machine learning project to predict diabetes in patients based on medical features. This project demonstrates a full ML pipeline, including model training, preprocessing, evaluation, and deployment via an interactive Streamlit dashboard.

---
## 📁 Project Structure
<pre> ## 📁 Project Structure ``` 📦 diabetes-prediction-project/ ├── 📁 app/ │ ├── app.py ← Streamlit dashboard │ ├── model.py ← Model loading & prediction │ └── preprocessing.py ← Input preprocessing functions ├── 📁 models/ │ ├── model_rf.joblib ← Trained Random Forest model │ └── scaler.joblib ← MinMaxScaler for input scaling ├── 📁 notebooks/ │ └── ml-prediction-diabetic-code.ipynb ← EDA, training & evaluation ├── 📄 requirements.txt └── 📄 README.md ``` </pre>

---
## 🧠 Features
- 🔍 Exploratory Data Analysis (EDA)
- 🧼 Preprocessing using MinMaxScaler
- 🧠 Model training with RandomForestClassifier
- 🎯 Evaluation with Confusion Matrix & Classification Report
- 📊 Feature importance visualization
- 💾 Model & Scaler saved via joblib
- 🖥️ Real-time prediction using Streamlit UI

---
## 🧪 Input Features

| Feature                  | Description                                      |
|--------------------------|--------------------------------------------------|
| Pregnancies              | Number of times pregnant                         |
| Glucose                  | Plasma glucose concentration                     |
| Blood Pressure           | Diastolic blood pressure (mm Hg)                 |
| Skin Thickness           | Triceps skin fold thickness (mm)                 |
| Insulin                  | 2-hour serum insulin (mu U/ml)                   |
| BMI                      | Body mass index (weight in kg / height in m^2)   |
| Diabetes Pedigree Func.  | Diabetes likelihood based on family history      |
| Age                      | Age in years                                     |

---
## 🚀 How to Run

# 1. Clone the repository
git clone https://github.com/your-username/diabetes-prediction-project.git
cd diabetes-prediction-project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app/app.py

---
## 📚 Dataset

Pima Indians Diabetes Dataset  
Source: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

---
## 📒 Kaggle Notebook

Curious about the full training code, EDA, and modeling steps?  
Check out the full notebook on Kaggle:  
🔗 https://www.kaggle.com/code/viochristian/ml-prediction-diabetic-code

---
## 👨‍💻 Authors
- 🧋 Silvio Christian — Machine Learning Developer & Streamlit Enthusiast  

---
## 💖 Special Notes

This project is for educational purposes only and meant to demonstrate:

- End-to-end machine learning pipeline
- Model deployment with Streamlit
- Clean project structure and reproducibility

---

Built with 💖, Python, and too much caffeine ☕
