🏠 California House Price Prediction (XGBoost Regressor)
This project uses the California Housing dataset to build a regression model that predicts the median house value in California districts. The model is trained using the XGBoost Regressor, a powerful machine learning algorithm known for its performance in structured data prediction tasks.

📊 Dataset Overview
The dataset used is the built-in fetch_california_housing dataset from scikit-learn.

Characteristic	Value
Number of Instances	20,640
Number of Attributes	8 numeric, predictive features + 1 target variable
Target Variable	MedHouseVal (Median House Value, expressed in hundreds of thousands of dollars - $100,000)
Feature Information:
MedInc: Median income in block group

HouseAge: Median house age in block group

AveRooms: Average number of rooms per household

AveBedrms: Average number of bedrooms per household

Population: Block group population

AveOccup: Average number of household members

Latitude: Block group latitude

Longitude: Block group longitude

🛠️ Technologies and Libraries
Python

Jupyter/Colab Notebook

pandas (for data manipulation)

numpy (for numerical operations)

matplotlib & seaborn (for data visualization and correlation heatmap)

sklearn (for dataset loading, model selection, and metrics)

xgboost (for the regression model)

🚀 Analysis and Model Evaluation
1. Data Preparation
The fetch_california_housing dataset was loaded.

A pandas DataFrame was created using the features (MedInc to Longitude).

The target variable, MedHouseVal (renamed to price in the DataFrame), was added.

No missing values were found in the dataset.

The dataset was split into features (X) and the target (y).

The data was split into Training (80%) and Testing (20%) sets using random_state=2.

2. Correlation Analysis
A heatmap was generated to visualize the correlation between all features and the target variable (price).

Key Takeaway: MedInc (Median Income) shows the strongest positive correlation with the target variable (price), suggesting it is a crucial feature for price prediction.

3. Model Training (XGBoost Regressor)
An XGBoost Regressor was initialized and trained on the training data (X_train, y_train).

4. Model Performance
The model was evaluated using two common regression metrics: R-squared (R 
2
 ) Error and Mean Absolute Error (MAE).

Metric	Training Data Score	Test Data Score
R-squared (R 
2
 ) Error	0.9437	0.8338
Mean Absolute Error (MAE)	0.1934	0.3109
Note on Scores:

The R 
2
  score is very high (0.94) on the training data, indicating the model fits the training data exceptionally well.

The slightly lower, but still strong, R 
2
  score (0.83) on the test data suggests the model generalizes reasonably well to unseen data, although the difference suggests some degree of overfitting occurred during training.

The MAE of 0.3109 on the test set means that, on average, the model's predictions are off by approximately $31,090 (since the target variable is in units of $100,000).

5. Prediction Visualization
Scatter plots comparing the actual prices (y) versus the predicted prices were generated for both the training and test sets. A good model's points should align closely along a diagonal line (y=x).

Training Data: Actual Price vs Predicted Price

Test Data: Actual Price vs Predicted Price

