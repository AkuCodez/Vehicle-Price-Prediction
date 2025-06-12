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

Try it live on [Streamlit Cloud](https://vehicle-price-prediction-gnxxhwzs2swwfbfq7x3rte.streamlit.app/) 🚀  

---

## 📂 Project Structure

```
Vehicle-Price-Prediction/
│
├── Vehicle_Pred_Proj/
│   ├── app.py                          # Streamlit web app
│   ├── xgboost_vehicle_price_model.pkl  # Trained ML pipeline (model + preprocessing)
│   ├── requirements.txt                # Project dependencies
│   └── README.md                       # Project documentation
```
---

## 📈 Model Training Summary

- Target variable was log-transformed using `np.log1p()`.
- Hyperparameter tuning via `GridSearchCV` on:
  - `n_estimators`, `learning_rate`, `max_depth`, `subsample`
- Final model performance:
  - **R² Score:** ~0.87
  - **RMSE:** ₹~45,000 (approx. depending on dataset)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/AkuCodez/Vehicle-Price-Prediction.git
cd Vehicle-Price-Prediction/Vehicle_Pred_Proj

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows use: venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

# 5. Open in browser (if it doesn't open automatically)
# Visit: http://localhost:8501
```
