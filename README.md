# AuditIQ — AI-Powered Fraud Detection

AuditIQ scans accounting data to detect irregular or high-risk transactions using unsupervised machine-learning models.  
Ideal for students, auditors, or small businesses wanting to understand financial anomalies.

---

## 🚀 Features
- Upload CSV of transactions (Date, Description, Category, Amount)
- Detect anomalies using Isolation Forest
- Visualize transactions and flagged outliers
- Download audit report with “Risk Flag” column
- Simple Streamlit web dashboard

---

## 🧰 Tech Stack
Python · Pandas · scikit-learn · Streamlit · Matplotlib

---

## ⚙️ Setup
```bash
git clone https://github.com/YOURUSERNAME/AuditIQ.git
cd AuditIQ
pip install -r requirements.txt
streamlit run app.py
