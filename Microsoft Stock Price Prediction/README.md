

# ✅ **Microsoft Stock Price Prediction

### **1. Problem Statement**

I built a **time-series forecasting model** to predict Microsoft’s closing stock price using **LSTM**, a deep-learning architecture designed for sequential data.

---

# **2. Dataset**

* Source: Microsoft historical stock data
* Columns included: Date, Open, High, Low, Close, Volume
* Target variable: **Close price**

---

# **3. Data Preprocessing**

The raw data was not directly suitable for LSTM, so I performed:

* Converted `Date` to datetime and set it as index
* Removed unused columns
* Filled missing values using interpolation
* Added technical indicators:

  * SMA, EMA
  * Bollinger Bands
  * RSI
* Scaled data using **MinMaxScaler**
* Created time-series sequences using a **60-day lookback window**
* Split data into **train/test sets**

👉 *This step ensures the LSTM learns from historical patterns effectively.*

---

# **4. Exploratory Data Analysis**

I visualized:

* Price trends
* Volume variations
* Moving averages & volatility bands
* Feature correlations

👉 *This helped identify which features capture meaningful price movement.*

---

# **5. Model Building – LSTM**

I designed a **stacked LSTM model**:

* Multiple LSTM layers
* Dropout layers to prevent overfitting
* Dense output layer for price prediction
* Adam optimizer + MSE loss
* Used EarlyStopping to stop overtraining

👉 *The model learns long-term dependencies, which is essential for stock data.*

---

# **6. Model Evaluation & Results**

Measured performance using:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

Plotted:

* Actual vs predicted prices
* Training vs validation loss

Then generated:

* **30-day future price forecast**

👉 *The model was able to follow the price trend closely, showing strong predictive capability.*

---

# **7. Final Outcome**

I built a complete end-to-end **deep learning pipeline** for stock forecasting:

✔ Cleaned & engineered time-series data
✔ Added technical indicators
✔ Normalized & sequenced data
✔ Built and trained a multi-layer LSTM
✔ Evaluated model using real test data
✔ Generated future stock predictions

The project proves I understand:

* Time-series modeling
* LSTM/DL architectures
* Data engineering
* Model evaluation
* Sequential forecasting workflows

