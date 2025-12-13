# 🚨 Fraud Detection System

A machine learning–powered Fraud Detection System that predicts whether a financial transaction is **fraudulent or legitimate** based on transaction behavior and balance changes.  
The project includes a trained ML model and an interactive **Streamlit web application** for real-time predictions.

---

## 📌 Features
- Predicts fraudulent transactions using a trained ML model
- Interactive Streamlit UI for real-time inference
- Handles multiple transaction types (PAYMENT, TRANSFER, CASH_OUT, etc.)
- Input validation for balance inconsistencies
- Production-style model loading with caching

---

## 🧠 Machine Learning Pipeline
- Data preprocessing & feature engineering
- Categorical encoding for transaction types
- Model training and evaluation
- Model persistence using `joblib`
- Inference via a web application

---

## 🏗️ Tech Stack
- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **Joblib**

---

## 📂 Project Structure

├── fraud_detection.py # Streamlit application

├── fraud_detection_model.pkl # Trained ML model

├── analysis_Dataset.ipynb # EDA, preprocessing & training

├── README.md


---

## 🚀 How to Run the Project

1. Clone the repository
```bash
git clone <repo-url>
cd fraud-detection-system


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run fraud_detection.py

🔍 Model Inputs

Transaction Type

Amount

Sender old & new balance

Receiver old & new balance

📈 Output

0 → Legit Transaction

1 → Fraudulent Transaction

🎯 Use Cases

Banking & financial institutions

Payment gateways

Risk analysis teams

Fraud monitoring systems
