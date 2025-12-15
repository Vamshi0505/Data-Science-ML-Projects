Customer Churn Prediction (End-to-End ML + Deployment)
Overview

This project predicts whether a customer is likely to churn using demographic and billing information. It covers the full machine learning lifecycle: data preprocessing, model training, evaluation, model persistence, and deployment via a Streamlit web application.

The goal is not just accuracy, but production readiness — reproducible preprocessing, saved artifacts, and a simple UI for real-time inference.

Problem Statement

Customer churn directly impacts revenue. The objective is to build a classification model that can proactively identify customers who are likely to leave, enabling targeted retention strategies.

Features Used

The model is trained on the following features (order strictly maintained during inference):

Age (Numeric)

Gender (Binary: Female = 1, Male = 0)

Tenure (Months)

Monthly Charges

Target variable:

Churn → 1 = Yes, 0 = No

Tech Stack

Python

Pandas, NumPy – Data handling

Scikit-learn – Model training & preprocessing

Joblib – Model & scaler persistence

Streamlit – Web application deployment

Project Structure
├── app.py                     # Streamlit application
├── notebook.ipynb             # Data analysis & model training
├── customer_churn_data.csv    # Dataset
├── best_model.pkl             # Trained ML model
├── scaler.pkl                 # Feature scaler
├── README.md
Model Training Summary

Data preprocessing performed in notebook.ipynb

Numerical features scaled using a fitted scaler

Best-performing classification model selected and saved as best_model.pkl

Scaler persisted as scaler.pkl to ensure training–inference consistency

Application Workflow

User enters customer details via Streamlit UI

Input features are ordered and reshaped

Scaler transforms input data

Trained model predicts churn probability

Result displayed as:

"The customer is likely to churn"

"The customer is not likely to churn"

How to Run Locally
1. Clone the repository
git clone <repo-url>
cd customer-churn-prediction
2. Install dependencies
pip install -r requirements.txt
3. Run the Streamlit app
streamlit run app.py
Key Learnings

Importance of saving preprocessing artifacts (scaler)

Feature order consistency between training and inference

Simple ML models can deliver real business value

Deploying ML models is as important as training them

Future Improvements

Add probability scores instead of binary output

Handle class imbalance explicitly

Add more behavioral features

Deploy on cloud (AWS / GCP / Azure)
