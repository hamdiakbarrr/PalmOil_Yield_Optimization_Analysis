# 🌴 Palm Oil Yield Prediction Model
📌 Project Overview

Python project for palm oil yield prediction and analysis. This project aims to predict palm oil yield (kg/ha) using a linear regression model based on plantation operational and environmental variables. The goal is to understand key factors influencing production and provide data-driven insights for better decision-making.

## 🎯 Objective
- Predict yield per hectare using regression model
- Identify key factors affecting production
- Produktive and unproductive block clustering
- Provide insights for plantation management

## 📊 Dataset
The dataset contains plantation data with the following variables:
- `umur_tanaman` → trees age
- `populasi_ha` → number of trees per hectare  
- `sex_ratio` → ratio of productive trees  
- `curah_hujan` → rainfall    
- `yield_kg_ha` → production per hectare (target)  

> Note: This repository uses sample data for demonstration purposes.

## ⚙️ Methodology
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Linear Regression Model
- Model Evaluation (MSE, R²)
- K-Means Clustering

## 📈 Model Performance
- Mean Squared Error (MSE): 0.45
- R² Score: 0.99

The model demonstrates a very high level of accuracy, explaining approximately 99% of the variance in yield data.

## 📊 Visualization
<img width="686" height="568" alt="Prediction vs Actual" src="https://github.com/user-attachments/assets/47bb6658-5e34-4ff4-8097-aa2c57c41043" />

The scatter plot shows a strong alignment between predicted and actual values, indicating that the model performs very well with minimal prediction error.

🧾 Key Insights
- The model shows excellent predictive performance with very low error (MSE)
- High R² (0.99) indicates strong relationship between input variables and yield
- Variables such as sex ratio and plant population are likely major contributors to yield performance
- The model can be used as a baseline for further optimization or more advanced machine learning models

## 🚀 How to Run
```git clone https://github.com/username/yield_prediction_model.git cd yield_prediction_model pip install -r requirements.txt jupyter notebook```

## 📁 Project Structure
- ```notebooks/``` → analysis & visualization  
- ```scripts/``` → model training & evaluation  
- ```data/``` → dataset 

## 🛠️ Tools & Libraries
- Python
- Jupyter
- Numpy
- Pandas
- Scikit-learn
- Scipy
- Statsmodels
- Matplotlib / Seaborn

## 👤 Author
Hamdi Akbar Setiawan  
