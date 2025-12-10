

# ✅ **Parkinson’s Disease Prediction

### **1. Problem Statement**

I built a machine learning system to **predict whether a person has Parkinson’s Disease** based on **voice features and clinical attributes**.
It’s a **binary classification** problem.

---

# **2. Dataset**

* Dataset: *parkinson_disease.csv*
* Contains **voice measurements** (jitter, shimmer, PPE, DFA, RPDE, harmonicity features) and demographic data.
* Target variable: **class (1 = Parkinson’s, 0 = Healthy)**
* The dataset was **highly imbalanced**.

---

# **3. Data Preprocessing**

### I performed:

* Removed `id` column (not needed).
* Separated **X (features)** and **y (target)**.
* Scaled numerical features using **StandardScaler**.
* Checked for missing or invalid values.
* Identified **class imbalance**.

Since the minority class was very small, I used:

### ✔️ **SMOTE (Synthetic Minority Oversampling Technique)**

to balance the dataset before training.

This step ensures the model doesn’t get biased toward the majority class.

---

# **4. Exploratory Data Analysis (EDA)**

I used histograms, boxplots, and heatmaps to understand patterns:

### Key Findings:

* Some voice features showed clear differences between Parkinson’s and healthy patients.
* Jitter/shimmer values were usually **higher** in Parkinson’s patients.
* Harmonicity values were **lower**, making the voice more unstable.
* PPE, DFA, and RPDE had strong correlations with the target.
* Heatmap showed several important relationships between voice biomarkers and the disease.

---

# **5. Model Training**

I trained four ML models:

1. **Logistic Regression**
2. **Random Forest**
3. **Support Vector Machine (SVM)**
4. **XGBoost**

All models were trained on the resampled (SMOTE) dataset.

---

# **6. Model Evaluation**

I compared the models using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Curve

### Result:

I selected the **best model based on the F1-Score**, because the dataset is imbalanced and F1-Score is the most reliable metric.

---

# **7. Final Outcome**

* The **best model** achieved the strongest balance of precision and recall (Best model → XGBoost)
* ROC-AUC curves were plotted for all models to visualize performance.
* The chosen model was used to predict a **new patient sample** after proper scaling, showing real-world usability.

---

# **8. Key Value of the Project**

This project demonstrates:

✔️ Ability to handle **imbalanced healthcare datasets**
✔️ Understanding of **feature scaling, SMOTE, and preprocessing**
✔️ Ability to compare multiple ML algorithms
✔️ Use of **Logistic Regression, Random Forest, SVM, XGBoost**
✔️ Strong EDA and visualization skills
✔️ Skill in creating a **complete end-to-end ML pipeline**

---

