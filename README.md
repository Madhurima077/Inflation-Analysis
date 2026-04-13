# 📊 Inflation Prediction Dashboard

A machine learning-powered web application that predicts inflation based on key macroeconomic indicators.

## 🚀 Live App

👉 https://inflation-analysis-depsqydfuzcr8aca9hnqvx.streamlit.app/

---

## 📌 Project Overview

Inflation is influenced by multiple economic factors. This project analyzes and models the relationship between:

* ⛽ Fuel Prices (Petrol & Diesel)
* 📈 Interest Rates
* 👥 Unemployment Rate

The model predicts inflation using these inputs and visualizes insights through an interactive dashboard.

---

## 🧠 Machine Learning Model

* Model Used: Random Forest Regressor
* Features:

  * Fuel Price (weighted from petrol & diesel)
  * Interest Rate
  * Unemployment
* Target:

  * Inflation Rate

---

## 📊 Key Features

* Interactive input controls (sidebar)
* Real-time inflation prediction
* Feature importance visualization
* Clean dashboard UI
* Deployed using Streamlit Cloud

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib

---

## 📁 Project Structure

```
inflation-analysis/
│
├── app.py
├── requirements.txt
├── model/
│   └── inflation_model.pkl
├── notebook/
└── data/
```

---

## 🧠 Insights

* Fuel prices show the strongest correlation with inflation
* Interest rate and unemployment had lower impact due to limited variation
* Demonstrates importance of feature selection in ML models

---

## 👩‍💻 Author

**Madhurima Acharya**

---

## ⚠️ Disclaimer

This model provides estimates based on historical data and does not account for all economic variables.
