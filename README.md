# 🏙️ **Gurgaon Real Estate Price Prediction Model**

### **End to End Machine Learning Project | Web Scraping | EDA | Model Building | Deployment**

This project is a complete end to end machine learning workflow that predicts **property prices in Gurgaon** using **web scraped real estate data from 2023**.
It includes **data cleaning, feature engineering, model training, evaluation, visualization and deployment** through an interactive Streamlit UI hosted on **Hugging Face Spaces**.

This repository contains the **main ML model**, all **preprocessing steps**, and the **Streamlit application code** used for deployment.

---

## 🚀 **Project Overview**

With rapidly growing real estate markets, estimating property prices can be difficult due to varying features like BHK, area, sector, furnishing, amenities and location.
To solve this, we scraped real data from public property listings and built a machine learning pipeline that predicts prices based on multiple factors.

This project includes:

* Web scraped data from 2023
* Data preprocessing and feature engineering
* Price trend visualizations
* Interactive scatter plots that help understand feature relationships
* Geo map to visualize property clusters
* Model training and experiment tracking
* Deployment using Streamlit and Hugging Face
* Multiple ML models optimized for accuracy

---

## 🧠 **Machine Learning Models Used**

After testing several algorithms and optimizing accuracy and MAE, the top three models chosen for deployment are:

### **✨ Random Forest**

A stable ensemble model made of multiple decision trees.

* R² Score: **0.8327**
* MAE: **0.52**
* Accuracy: **83.27%**

### **⚡ XGBoost**

Fast, efficient and highly accurate boosting model that captures complex patterns.

* R² Score: **0.90**
* MAE: **0.45**
* Accuracy: **85.27%**

### **🌲 Extra Trees Classifier**

Works extremely well for non-linear relationships with high speed.

* R² Score: **0.90**
* MAE: **0.4595**
* Accuracy: **85.02%**

All three trained model files are included as `.pkl` files in this repository.

---

## 📊 **Data Analysis & Visualizations**

The notebook includes detailed exploration such as:

* Price distribution across different BHKs
* Scatter plots showing relationships between price and features
* Sector wise word cloud generator
* Geo map showing property clusters in Gurgaon
* Correlation heatmaps
* Distribution analysis of area, furnishing, amenities and more

These insights were crucial for building the correct preprocessing pipeline and selecting the best performing models.

---


## 📁 **Repository Structure**

```
📦 Project Folder  
│  
├── streamlit_app.py         # Main Streamlit UI  
├── model_random_forest.pkl  # Trained Random Forest model  
├── model_xgboost.pkl        # Trained XGBoost model  
├── model_extra_trees.pkl    # Trained Extra Trees model  
├── requirements.txt         # Dependencies  
├── data/                    # Dataset used (CSV/Excel)  
└── README.md                # Documentation
```

For exploratory analysis, refer to the notebook repository below.

---

## 🔧 **Tech Stack**

* Python
* Scikit-learn
* XGBoost
* Pandas & NumPy
* Streamlit
* Matplotlib / Seaborn
* Hugging Face Spaces
* Web Scraping (BeautifulSoup/Selenium)

---
