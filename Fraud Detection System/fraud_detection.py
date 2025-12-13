import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load Model with caching
# ------------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load("fraud_detection_model.pkl")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_model()

st.title("Fraud Detection System")
st.markdown("Enter the transaction details below and click **Predict Fraud**.")
st.divider()

# ------------------------------
# Input UI
# ------------------------------
transaction_type = st.selectbox(
    "Transaction Type",
    options=["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# ------------------------------
# Input Validation
# ------------------------------
if newbalanceOrig > oldbalanceOrg:
    st.warning("Sender's new balance cannot be greater than old balance.")

if st.button("Predict Fraud"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Predict
    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.stop()

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ This transaction is likely **fraud**.")
    else:
        st.success("✅ This transaction looks **legit**.")
