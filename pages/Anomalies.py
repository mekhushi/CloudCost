import streamlit as st
import plotly.express as px

st.title("Anomaly Detection")

if "df" not in st.session_state:
    st.warning("Upload CSV first.")
    st.stop()

df = st.session_state["df"]

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
col = st.selectbox("Select column to detect anomalies", numeric_cols)

threshold = st.slider("Z-score threshold", 1.0, 4.0, 3.0)

mean = df[col].mean()
std = df[col].std()

df["is_anomaly"] = (df[col] > mean + threshold * std) | (df[col] < mean - threshold * std)

st.subheader("Anomaly Chart")
fig = px.scatter(df, x=df.index, y=col, color="is_anomaly")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Anomaly Records")
st.dataframe(df[df["is_anomaly"] == True])
