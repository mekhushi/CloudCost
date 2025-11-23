import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cloud Cost Leak Analyzer", layout="wide")

st.title("Cloud Cost-Detect. Analyze. Optimize. ")

st.header("Problem Statement")
st.write(
    """
Companies unknowingly lose a huge amount of money due to hidden cloud billing leaks. Misconfigured services, idle GPUs, unused storage volumes, and sudden compute spikes can drastically increase the cloud bill. This tool analyzes cloud billing logs, identifies unusual patterns, and detects potential cost leaks in real time.
"""
)

st.image("./Assets/img.jpg", use_container_width=200)

st.write("""
This application allows you to upload your cloud billing CSV file and automatically  
analyzes the following:

• Cost trends  
• Anomalies in usage  
• Idle resource wastage  
• Service-wise cost breakdown  
• Simple forecasting  
• Smart cost-saving suggestions  

Use the sidebar to navigate through the dashboard.
""")



uploaded_file = st.sidebar.file_uploader("Upload Cloud Billing CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.success("CSV loaded successfully.")
else:
    st.warning("Upload a CSV file to continue.")

