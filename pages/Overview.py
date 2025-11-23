import streamlit as st
import plotly.express as px

st.title("Overview")

if "df" not in st.session_state:
    st.warning("Upload CSV on Home Page.")
    st.stop()

df = st.session_state["df"]

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.subheader("Basic Info")
st.write(df.describe())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

if len(numeric_cols) > 0:
    st.subheader("Distribution Plot")
    col_to_plot = st.selectbox("Select column", numeric_cols)
    fig = px.histogram(df, x=col_to_plot, nbins=30)
    st.plotly_chart(fig, use_container_width=True)
