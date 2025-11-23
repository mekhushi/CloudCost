import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cost Forecasting")

# Check for uploaded data
if "df" not in st.session_state:
    st.warning("Upload CSV on Home Page.")
    st.stop()

df = st.session_state["df"]

# Ensure required columns exist
required_cols = ["Timestamp", "CostUSD"]
missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"Missing required columns: {missing}")
    st.stop()

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

if df["Timestamp"].isna().sum() > 0:
    st.error("Some dates in 'Timestamp' column are invalid.")
    st.stop()

df = df.sort_values("Timestamp")  # Ensure correct order

# Interactive window selection
window = st.slider("Select Moving Average Window", 2, 30, 7)

# Compute moving average forecast
df["Forecast"] = df["CostUSD"].rolling(window=window).mean()

st.subheader("Forecast vs Actual Cost")

fig = px.line(
    df,
    x="Timestamp",
    y=["CostUSD", "Forecast"],
    labels={"value": "Cost (USD)", "Timestamp": "Date"},
)

st.plotly_chart(fig, use_container_width=True)

st.write("Preview")
st.dataframe(df.tail(20))
