# 🩺 Diabetes Prediction: Research & Deployment System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Academic_Replication-purple)

## 📌 Overview
This repository serves a dual purpose, bridging the gap between academic research replication and practical software deployment:

1.  **Research Phase (`.ipynb`):** A strict replication of a specific medical study on diabetes prediction using **Random Forest**, **SMOTE**, and **Global Scaling**.
2.  **Deployment Phase (`.py`):** A modular web application built with **Streamlit** that serves the trained model to end-users in a user-friendly interface.

> **⚠️ NOTE:** This is the **Academic Replication** version which intentionally contains data leakage to reproduce a paper's results. For the industry-standard, robust version (Leakage-Free & Fine-Tuned), please visit:
> 👉 **[Diabetes Prediction Fine-Tuned Project](https://github.com/viochris/Diabetes-prediction-fine-tuned-project/tree/main)**

---

## ⚠️ Academic Methodology Disclaimer
**Please Read Before Reviewing the Research Notebook:**

To strictly adhere to the cited reference paper's methodology and reproduce their reported metrics, the **Jupyter Notebook (`ml-prediction-diabetic-code.ipynb`)** follows a specific preprocessing workflow:

* **Global Scaling:** `MinMaxScaler` is applied to the *entire dataset* before splitting.
* **Global SMOTE:** Oversampling is applied to the *entire dataset* before splitting.

**Methodology Note:** I am fully aware that applying these techniques before the Train-Test split introduces **Data Leakage** and is not standard industry practice. However, this was done intentionally to reproduce the exact results reported in the academic paper.

---

## 📂 Project Architecture
This project moves beyond a simple notebook by implementing a **Modular Architecture** for deployment. The logic is separated into distinct responsibilities:

```text
├── app/                                   # 💻 APPLICATION SOURCE CODE
│   ├── app.py                             # Main Streamlit application
│   ├── model.py                           # Backend logic & inference
│   └── preprocess.py                      # Utils for input formatting
├── assets/                                # 🖼️ STATIC ASSETS
│   └── diabetes_app_ui.png                # App Screenshot
├── models/                                # 📦 ARTIFACTS (Serialized Objects)
│   ├── scaler.joblib                      # Saved MinMaxScaler
│   └── model_rf.joblib                    # Saved Random Forest Model
├── notebooks/                             # 🔬 RESEARCH & EXPERIMENTATION
│   └── ml-prediction-diabetic-code.ipynb  # Replicated Research Study
└── requirements.txt                       # Dependency list
````

## 🛠️ Tech Stack
  * **Frontend Framework:** Streamlit
  * **Machine Learning Core:** Scikit-Learn (Random Forest Classifier)
  * **Data Handling:** Pandas, NumPy, Joblib
  * **Imbalanced Data:** Imbalanced-learn (SMOTE)
  * **Environment:** Python 3.9+

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/viochris/Diabetes-prediction-project.git
cd Diabetes-prediction-project
```

### 2. Install Dependencies
Make sure you have the required libraries installed:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
Execute the main application file from the root directory:

```bash
streamlit run app/app.py
```

### 4\. Access the Dashboard
Open your browser and navigate to:
`http://localhost:8501`


## 📊 Research Results

Based on the replication study conducted in the notebook (`ml-prediction-diabetic-code.ipynb`) using Random Forest with Global SMOTE:

  * **Algorithm:** Random Forest Classifier
  * **Accuracy:** ~83.67%
  * **Precision:** ~84%
  * **Recall:** ~84%

*(Metrics are inflated due to the intentional data leakage required for paper replication)*

## 📷 Screenshots
### Web Application Interface
User-friendly interface built with Streamlit allowing for real-time patient data input and instant prediction:

![Diabetes App UI](assets/diabetes_app_ui.png)

-----

**Author:** [Silvio Christian, Joe](https://www.linkedin.com/in/silvio-christian-joe)
*"Bridging the gap between Academic Research and Practical Deployment."*
