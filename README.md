# Heart Disease Prediction Model

## Overview

This project involves building a machine learning model to predict the likelihood of heart disease. Multiple algorithms were tested, including **Logistic Regression**, **K-Nearest Neighbors (KNN)**, and **Random Forest**. The final model with **Logistic Regression** achieved an accuracy of **88%**.

## Dataset

The dataset consists of several attributes related to a patient's health, which are used to predict whether they have heart disease. Some of the key features include:
- **Age**: Age of the patient
- **Sex**: Gender of the patient
- **CP (Chest Pain Type)**: Type of chest pain experienced
- **Trestbps**: Resting blood pressure
- **Chol**: Serum cholesterol level
- **Thalach**: Maximum heart rate achieved
- **Exang**: Exercise induced angina
- **Oldpeak**: Depression induced by exercise relative to rest
- **Slope**: Slope of the peak exercise ST segment
- **Ca**: Number of major vessels colored by fluoroscopy
- **Thal**: Type of thalassemia

### Target
- **0**: No Heart Disease
- **1**: Heart Disease

## Models Used

- **Logistic Regression**: Achieved 88% accuracy.
- **K-Nearest Neighbors (KNN)**: Achieved 63% accuracy 
- **Random Forest**: Achieved 83% accuracy.

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/sushrutha777/Heart-Disease-Classification.git
   cd Heart-Disease-Classification

2. Create a new environment and install dependencies:

   ```bash
   conda create --prefix ./env python=3.12.3
   conda activate ./env
   conda install numpy pandas scikit-learn matplotlib seaborn
   ```

## Model Usage, Results, and Future Work

### Usage

1. **Load the Model**:

   ```python
   import pickle
   with open('gs_log_reg_model.pkl', 'rb') as f:
   model = pickle.load(f)
   ```

## Make Predictions

```python
import pandas as pd

# New patient data (example, replace with actual data)
new_data = [[45, 1, 3, 130, 250, 0, 1, 1, 120, 0, 1, 2, 3]]

# Convert to DataFrame with correct column names
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
           'exang', 'oldpeak', 'slope', 'ca', 'thal']
new_data_df = pd.DataFrame(new_data, columns=columns)

# Make prediction
prediction = model.predict(new_data_df)

if prediction[0] == 1:
    print("Heart Disease")
else:
    print("No Heart Disease")
```
### Results

- **Logistic Regression Accuracy**: 88%
- **Other Models**: KNN and Random Forest were also tested but did not outperform Logistic Regression.

### Future Work

- **Hyperparameter Tuning**:  
  Explore advanced techniques like Bayesian Optimization or Genetic Algorithms.  

- **New Models**:  
  Test SVM, XGBoost, LightGBM, and ensemble methods (e.g., stacking).  

- **Feature Engineering**:  
  Investigate feature interactions or polynomial features.  

- **Cross-Validation**:  
  Use stratified k-fold cross-validation for robust evaluation.  

- **Deployment**:  
  Build a REST API using Flask/Django for real-time predictions.  

- **Interpretability**:  
  Generate feature importance plots with SHAP or LIME.  
