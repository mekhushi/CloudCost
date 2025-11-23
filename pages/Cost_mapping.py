import streamlit as st
import plotly.express as px

st.title("Cost Mapping")

if "df" not in st.session_state:
    st.warning("Upload CSV first.")
    st.stop()

df = st.session_state["df"]

if "Service" not in df.columns or "CostUSD" not in df.columns:
    st.error("CSV must contain 'Service' and 'CostUSD'.")
    st.stop()

service_cost = df.groupby("Service")["CostUSD"].sum().reset_index()

chart_type = st.selectbox("Chart Type", ["Bar", "Pie"])

if chart_type == "Bar":
    fig = px.bar(service_cost, x="Service", y="CostUSD")
else:
    fig = px.pie(service_cost, names="Service", values="CostUSD")

st.plotly_chart(fig, use_container_width=True)
