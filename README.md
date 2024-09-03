# Logistic-regression
## Logistic Regression Model for Predicting Survival Probability
This project involves building and deploying a logistic regression model to predict the probability of survival using a dataset with various features. The analysis covers data exploration, preprocessing, model building, evaluation, and deployment using Streamlit.

### 1. Data Exploration
#### a. Dataset Loading and EDA
- Dataset Loading: Load the dataset into a DataFrame.
- Exploratory Data Analysis (EDA): Perform EDA to understand the structure of the dataset, examine the distribution of features, and identify any patterns or correlations.
#### b. Feature Examination and Summary Statistics
- Feature Types: Analyze the types of features (categorical or numerical) and compute summary statistics (mean, median, standard deviation, etc.) for each feature.
#### c. Data Visualization
- Histograms and Box Plots: Create histograms and box plots to visualize the distributions of numerical features.
- Pair Plots: Generate pair plots to explore relationships between features.
- Correlation Analysis: Investigate correlations among features to identify potential predictors for the target variable.

### 2. Data Preprocessing
#### a. Handling Missing Values
- Imputation: Handle missing values by applying appropriate imputation methods to ensure the dataset is complete and ready for modeling.
#### b. Encoding Categorical Variables
- Categorical Encoding: Convert categorical variables into numerical format using encoding techniques such as one-hot encoding, allowing them to be used in the logistic regression model.

### 3. Model Building
#### a. Logistic Regression Model Implementation
- Model Building: Implement a logistic regression model using Python's scikit-learn library.
- Training the Model: Train the logistic regression model using the training dataset to learn the relationships between features and the target variable.

### 4. Model Evaluation
#### a. Model Performance Evaluation
- Evaluation Metrics: Evaluate the model's performance on the testing dataset using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC score.
- ROC Curve Visualization: Visualize the Receiver Operating Characteristic (ROC) curve to assess the model's ability to distinguish between classes.

### 5. Interpretation
#### a. Coefficient Interpretation
- Logistic Regression Coefficients: Interpret the coefficients of the logistic regression model to understand the impact of each feature on the prediction.
#### b. Feature Significance
- Feature Analysis: Discuss the significance of each feature in predicting the target variable (survival probability), highlighting the most influential predictors.

### 6. Deployment with Streamlit
#### a. Model Deployment
- Streamlit Application: Deploy the trained logistic regression model using Streamlit to create an interactive web application.
- User Input and Prediction: Set up the Streamlit app to accept user inputs and generate predictions for survival probability based on the logistic regression model.
#### b. Deployment Options
- Local or Online Deployment: Deploy the Streamlit app locally or online via Streamlit Share, allowing users to interact with the model and make predictions in real time.
