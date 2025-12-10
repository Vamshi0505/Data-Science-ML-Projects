# 📰 Fake News Prediction

A straightforward machine learning/NLP pipeline to classify news articles as **REAL** or **FAKE**.

## 🚀 Project Overview

This project processes news text, cleans it, extracts features, and trains ML models to determine whether an article is fake. The notebook includes:

* Data preprocessing
* Text vectorization (TF-IDF)
* Model training & evaluation
* Performance metrics

## 📂 Files

* **Fake_News_Prediction.ipynb** — Main notebook for preprocessing, training, and evaluation.


## 🧠 Features & Techniques

* Text cleaning (lowercasing, punctuation removal, stopword removal)
* Lemmatization
* TF-IDF vectorization
* Machine learning classifiers (Logistic Regression, Naïve Bayes, Random Forest)
* Metrics: Accuracy, F1-Score, Confusion Matrix

## 🔧 Tech Stack

* Python
* Scikit-Learn
* Pandas
* NumPy
* NLTK / spaCy
* Matplotlib / Seaborn

## ▶️ How to Run

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:

   ```bash
   jupyter notebook Fake_News_Prediction.ipynb
   ```

## 📊 Results

Test Loss: 0.6931, Test Accuracy: 0.5051
40/40 ━━━━━━━━━━━━━━━━━━━━ 24s 590ms/step
Precision: 0.7692, Recall: 0.0158, F1-score: 0.0309

## 🛠 Future Improvements

* Deep learning models (LSTM, BERT, RoBERTa)
* Deploy as an API or web app
* Improve dataset balance
* Explainability with SHAP/LIME


