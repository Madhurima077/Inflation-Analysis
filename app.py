import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIG ---
st.set_page_config(page_title="Inflation Dashboard", layout="wide")

# --- LOAD MODEL ---
model = pickle.load(open("model/inflation_model.pkl", "rb"))

# --- HEADER ---
st.markdown(
    "<h1 style='text-align: center;'>Inflation Prediction Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>Estimate inflation using macroeconomic indicators</p>",
    unsafe_allow_html=True
)

# --- SIDEBAR INPUTS ---
st.sidebar.header("Input Parameters")

petrol = st.sidebar.number_input("Petrol Price", value=130.0)
diesel = st.sidebar.number_input("Diesel Price", value=135.0)
interest = st.sidebar.number_input("Interest Rate (%)", value=4.0)
unemployment = st.sidebar.number_input("Unemployment Rate (%)", value=5.0)

# --- FEATURE ENGINEERING ---
fuel = 0.6 * petrol + 0.4 * diesel

# --- MAIN LAYOUT ---
col1, col2 = st.columns(2)

# --- PREDICTION ---
with col1:
    st.subheader("Prediction")

    if st.button("Predict Inflation"):
        input_data = pd.DataFrame({
    "Fuel_Price": [fuel],
    "Interest_Rate": [interest],
    "Unemployment": [unemployment]
})

        prediction = model.predict(input_data)
        st.success(f"Estimated Inflation: {prediction[0]:.2f}%")

# --- CHART ---
with col2:
    st.subheader("Input Overview")

    data = pd.DataFrame({
        "Feature": ["Fuel Price", "Interest Rate", "Unemployment"],
        "Value": [fuel, interest, unemployment]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Feature"], data["Value"])
    ax.set_ylabel("Values")
    ax.set_title("Input Features")

    st.pyplot(fig)

# --- FEATURE IMPORTANCE ---
st.subheader("Feature Importance")
st.caption("Relative importance of each feature in predicting inflation")

importance = model.feature_importances_

features = ["Fuel_Price", "Interest_Rate", "Unemployment"]

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

st.bar_chart(importance_df.set_index("Feature"))

# --- MODEL EXPLANATION ---
st.markdown("---")
st.subheader("Model Insights")

st.write("""
This model estimates inflation based on:

- Fuel Prices (weighted petrol & diesel)
- Interest Rates
- Unemployment Levels

Note:
- Predictions represent trends, not exact values.
- Inflation is influenced by many external factors not included in this model.
""")

st.info("Fuel prices have the strongest influence in this model. Other variables may have limited impact based on available data.")



# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Developed by <b>Madhurima Majumdar</b> | Inflation Prediction System
    </div>
    """,
    unsafe_allow_html=True
)


