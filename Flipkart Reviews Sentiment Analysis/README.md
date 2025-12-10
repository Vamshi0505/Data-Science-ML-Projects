This project is a **Sentiment Analysis** classification task performed on a dataset of **Flipkart product reviews** to automatically determine if a review expresses a positive or negative sentiment.


### 1. Project Goal & Data

* **Objective:** To build and compare multiple Machine Learning models to accurately classify Flipkart customer reviews into **Positive (1)** or **Negative (0)** sentiment categories.
* **Dataset:** We used the `flipkart_data.csv` file, which initially contained **9,976** reviews and their corresponding numerical `rating` (1-5).

### 2. Data Preprocessing & Feature Engineering

* **Labeling (Target Variable):** I converted the raw `rating` (1-5) into a binary `sentiment` label:
    * **Positive (1):** Ratings of 4 or 5.
    * **Negative (0):** Ratings of 1, 2, or 3.
* **Data Cleaning:** The dataset was cleaned by removing missing values and **duplicate entries**, reducing the size to **7,868** unique reviews.
* **Text Preprocessing:** I applied a text cleaning pipeline to normalize the review text:
    * Converted all text to **lowercase**.
    * Removed **special characters, numbers, and punctuation**.
    * Removed **English stopwords** (e.g., 'the', 'a', 'is') using the NLTK library.
* **Feature Conversion (Vectorization):** I used **TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer** to convert the cleaned text reviews into a numerical feature matrix (`X`), which is required for machine learning models. I limited the feature space to the **top 3,000 most frequent words** to manage dimensionality.
* **Data Split:** The data was split into a **Training set (80%)** and a **Testing set (20%)** for model evaluation.

### 3. Modeling and Results

* **Models Used:** I trained and evaluated four different classification models to find the best performer for this specific dataset:
    * Logistic Regression
    * Multinomial Naive Bayes
    * Random Forest Classifier
    * Support Vector Classifier (SVC)
* **Evaluation:** The performance was assessed using standard classification metrics (Accuracy, F1-Score, Classification Report, and Confusion Matrix).
* **Key Finding:** The **Logistic Regression** model demonstrated the best performance, achieving a final **accuracy of 91.23%** and an **F1-Score of 94.75%** on the unseen test data.

### Summary of Impact

This project demonstrates proficiency in the full NLP pipeline, from data acquisition and preprocessing (tokenization, stopword removal) to advanced feature engineering (TF-IDF) and comparative machine learning model selection, resulting in a highly accurate model for business insights (e.g., tracking product performance or customer service issues).
