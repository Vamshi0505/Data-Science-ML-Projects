# Gender -> ! Female 0 Male
# churn -> 1 Yes 0 No
# Scaler is exported as scaler,pkl
# model is exported as best_model.pkl
# order of the X -> 'Age','Gender','Tenure','MonthlyCharges'

import streamlit as st
import joblib
import numpy as np

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Churn Prediction")

st.divider()

st.write("please provide the following details to predict if the customer will churn or not:")

st.divider()

age = st.number_input("Age",min_value=10,max_value=100,value=30)

tenure = st.number_input("Tenure (in months)",min_value=0,max_value=130,value=12)

monthlycharges = st.number_input("Monthly Charges",min_value=30.0,max_value=150.0)

gender = st.selectbox("Gender",["Female","Male"])

st.divider()

predictbutton = st.button("Predict")

if predictbutton:
    gender_selected = 1 if gender == "Female" else 0

    X = [age,gender_selected,tenure,monthlycharges]
    X1 = np.array(X).reshape(1,-1)
    prediction = model.predict(scaler.transform(X1))
    if prediction[0] == 1:
        st.error("The customer is likely to churn")
    else:
        st.success("The customer is not likely to churn")

else:
    st.write("Please provide the details and click on Predict button")
