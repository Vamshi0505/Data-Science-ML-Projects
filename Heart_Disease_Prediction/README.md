# CHD Prediction Project — Interview Summary**


# **1. Problem Statement**

The goal of the project was to **predict whether a person will develop Coronary Heart Disease (CHD) in the next 10 years** using health, lifestyle, and medical data.

This is a **binary classification** problem.

---

# **2. Dataset Used**

* Framingham Heart Study dataset
* Contains patient data like:

  * Age, cholesterol, blood pressure
  * Smoking habits
  * Diabetes
  * BMI, heart rate
* Target variable: **TenYearCHD (0 = No, 1 = Yes)**

---

# **3. Data Cleaning**

I cleaned the dataset by:

1. **Dropping irrelevant columns** (like *education*).
2. **Renaming columns** for readability.
3. **Removing rows with missing values** (simplest and fastest approach).

After cleaning, the dataset became consistent and ready for modeling.

---

# **4. Feature Preparation**

* **X = all health metrics**
* **y = 10-year CHD risk**
* Split the dataset using **70% training / 30% testing**
* Applied **StandardScaler** so all numerical features have similar scales
  (important for Logistic Regression)

---

# **5. Exploratory Data Analysis (EDA)**

I performed visual analysis to understand patterns:

### **Key findings:**

* The dataset is **imbalanced** → far more people with *no CHD* than CHD
* Strongest correlations with CHD:

  * Age
  * Blood pressure
  * Glucose
  * Cholesterol
* Histograms helped understand feature distributions
* Heatmap highlighted relationships between variables

This step gave intuition about which features matter most.

---

# **6. Model Building**

I used **Logistic Regression** because:

* It’s simple
* Interpretable
* Performs well on structured tabular data
* Works well with scaled features

I trained the model using the scaled training data.

---

# **7. Model Evaluation**

I evaluated performance using multiple metrics:

### ✔️ **Accuracy Score**

Shows overall prediction correctness.

### ✔️ **Confusion Matrix**

Showed how well the model distinguished CHD vs non-CHD.

### ✔️ **Classification Report**

Provided precision, recall, and F1-score.

### ✔️ **ROC-AUC Curve**

Measured overall model performance across all thresholds.

The ROC-AUC score tells how well the model separates the two classes.

---

# **8. Predicting a New Patient**

I created a **new patient sample**, scaled it using the same scaler, and predicted:

* Whether the patient is at risk of CHD
* The probability (confidence level)

This shows the model’s real-world usability.

---

# **9. Conclusion**

The model successfully predicts 10-year CHD risk.

### **Main Takeaways:**

* Logistic Regression provides a solid baseline
* Some features are strong indicators of heart disease
* The model can be improved by:

  * Handling class imbalance (SMOTE)
  * Trying advanced models (Random Forest, XGBoost)
  * Adding feature engineering

---

# 💥 **The One-Line Summary for Interview**

> “I built an end-to-end machine learning model that predicts 10-year heart disease risk using Logistic Regression. I cleaned the data, performed EDA, scaled features, trained the model, evaluated it using metrics like ROC-AUC, and even demonstrated real patient predictions.”

