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

- **Logistic Regression**: Achieved 86.89% accuracy.
- **Random Forest**: Achieved 83.61% accuracy.
- **LightGBM**: Achieved 83.61% accuracy.
- **XGBoost**: Achieved 81.97% accuracy.
- **Gradient Boosting**: Achieved 77.05% accuracy.
- **Support Vector Machine (SVM)**: Achieved 70.49% accuracy.
- **K-Nearest Neighbors (KNN)**: Achieved 68.85% accuracy.

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/sushrutha777/Heart-Disease-Prediction.git
   cd Heart-Disease-Classification

2. Create a new environment and install dependencies:

   ```bash
   conda create --prefix ./env python=3.12.3
   conda activate ./env
   conda install numpy pandas scikit-learn matplotlib seaborn
   ```

### Results

- **Logistic Regression Accuracy**: 88%
- **Other Models**: KNN, Random Forest, Gradient Boosting, SVM, XGBoost, and LightGBM were also tested, but none outperformed Logistic Regression, which gave the highest accuracy after hyperparameter tuning. 
