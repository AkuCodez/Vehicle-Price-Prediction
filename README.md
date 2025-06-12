# 🚗 Vehicle Price Prediction App

Welcome to the **Vehicle Price Prediction System**!  
This web application predicts the estimated market price of a used vehicle based on key specifications provided by the user.

Built with:
- 🧠 **Machine Learning** (XGBoost + GridSearchCV)
- 📦 **Preprocessing Pipelines** using Scikit-learn
- 🌐 **Streamlit** for web UI
- 💾 **Joblib** for model serialization

---

## 📌 Project Overview

This system helps users estimate the resale value of a vehicle based on features like:
- Make & Model
- Fuel Type & Transmission
- Body Type & Trim
- Mileage, Age, Cylinders, and more

The model was trained using a dataset of used car listings, with **log-transformed prices** for better accuracy and then reverse-transformed for final predictions.

---

## 🛠 Tech Stack

| Layer         | Tools / Libraries                          |
|---------------|--------------------------------------------|
| 💡 ML Model   | `XGBoostRegressor` with `GridSearchCV`     |
| 🔁 Pipeline   | `Pipeline` + `ColumnTransformer` + `OneHotEncoder` |
| 🧠 Backend    | `joblib`, `pandas`, `numpy`, `scikit-learn` |
| 🌐 Frontend   | `Streamlit`                                |
| ☁️ Deployment | [Streamlit Cloud](https://streamlit.io/cloud) |

---

## 🖥 Demo

Try it live on [Streamlit Cloud](https://your-app-link-here) 🚀  
*(Replace with actual URL once deployed)*

---

## 📂 Project Structure

