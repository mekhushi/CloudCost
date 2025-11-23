import streamlit as st

st.title("Cost Saving Suggestions")

if "df" not in st.session_state:
    st.warning("Upload CSV first.")
    st.stop()

df = st.session_state["df"]

suggestions = []

if "GPU_Utilization" in df.columns and df["GPU_Utilization"].mean() < 20:
    suggestions.append("Low GPU utilization detected. Consider stopping idle GPU instances.")

if "CPU_Utilization" in df.columns and df["CPU_Utilization"].mean() < 25:
    suggestions.append("Underutilized CPU detected. Use smaller instance types.")

if "StorageGB" in df.columns and df["StorageGB"].mean() > 300:
    suggestions.append("High storage volumes found. Delete unused disks.")

if "UsageHours" in df.columns and df["UsageHours"].mean() < 10:
    suggestions.append("Low compute usage. Deallocate unused nodes.")

if len(suggestions) == 0:
    st.write("No major leaks detected.")
else:
    for s in suggestions:
        st.write("- " + s)
