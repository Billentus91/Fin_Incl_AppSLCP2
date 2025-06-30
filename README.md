# Financial Inclusion Prediction App

This is a Streamlit web app that predicts whether an individual in East Africa is likely to own a bank account, based on demographic and socioeconomic data.

## 🔍 Dataset
The model was trained on the **Financial Inclusion in Africa** dataset from the Zindi platform. It contains demographic features like:
- Age
- Education level
- Job type
- Marital status
- Location type
- Household size
- Country

## ⚙️ Model
The backend uses an **XGBoost classifier** trained and serialized using `joblib`. Class imbalance was handled using `scale_pos_weight`.

## 🚀 How to Run Locally

1. Clone the repo or download the files.
2. Install dependencies:
pip install streamlit xgboost pandas joblib
3. Run the app:
streamlit run Fin_app.py

## 🌍 Deployment
Deployed via [Streamlit Cloud](https://streamlit.io/cloud). To deploy:
1. Push `app.py` and `xgb_model.pkl` to your GitHub repo.
2. Connect your repo on Streamlit Cloud.
3. Set `app.py` as the main file and deploy.

## 📁 Files
- `Fin_app.py` – Streamlit app interface
- `xgb_model.pkl` – Trained XGBoost model

---
