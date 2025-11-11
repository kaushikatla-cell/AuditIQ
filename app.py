import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data, summarize_data
from fraud_detection import detect_anomalies

st.set_page_config(page_title="AuditIQ", page_icon="💼", layout="wide")
st.title("💼 AuditIQ — AI-Powered Fraud Detection")
st.caption("Upload a CSV with columns: Date, Description, Category, Amount")

with st.sidebar:
    st.header("⚙️ Settings")
    contamination = st.slider(
        "Anomaly sensitivity (contamination %)",
        min_value=1, max_value=20, value=5, step=1,
        help="Higher = flags more transactions as anomalies"
    ) / 100.0

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
use_sample = st.checkbox("Use included sample_data.csv")

df = None
if uploaded_file:
    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Could not read your CSV: {e}")
elif use_sample:
    try:
        df = load_data("sample_data.csv")
        st.info("Loaded sample_data.csv")
    except Exception as e:
        st.error(f"Sample data missing or unreadable: {e}")

if df is None:
    st.stop()

st.subheader("📄 Data Preview")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("📊 Summary Statistics")
summary = summarize_data(df)
st.write(summary)

st.subheader("🤖 Anomaly Detection")
df_flagged = detect_anomalies(df, contamination=contamination)
anomalies = df_flagged[df_flagged["RiskFlag"] == "Suspicious"]

st.success(f"Detected {len(anomalies)} suspicious transactions out of {len(df_flagged)} total.")
st.dataframe(anomalies.sort_values("AnomalyScore").head(50), use_container_width=True)

# Charts
st.subheader("💡 Spending Overview")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Spending by Category (sum)**")
    cat = df_flagged.groupby("Category", as_index=False)["Amount"].sum().sort_values("Amount", ascending=False)
    plt.figure(figsize=(6, 3))
    sns.barplot(data=cat, x="Category", y="Amount")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt.gcf())

with col2:
    st.markdown("**Amounts (Anomalies highlighted)**")
    plt.figure(figsize=(6, 3))
    sns.scatterplot(
        data=df_flagged,
        x="Date", y="Amount",
        hue="RiskFlag"
    )
    plt.tight_layout()
    st.pyplot(plt.gcf())

# Download
st.subheader("📥 Download Audit Report")
csv_bytes = df_flagged.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV with Risk Flags",
    data=csv_bytes,
    file_name="AuditIQ_Report.csv",
    mime="text/csv"
)

st.caption("Tip: Adjust sensitivity in the sidebar. Lower scores in 'AnomalyScore' indicate more anomalous records.")
