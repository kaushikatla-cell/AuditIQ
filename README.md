# 💼 AuditIQ — AI-Powered Fraud Detection

🚀 **Live Demo:** [https://auditiq1.streamlit.app/](https://auditiq1.streamlit.app/)  
📊 **GitHub Repo:** [github.com/kaushikatla-cell/AuditIQ](https://github.com/kaushikatla-cell/AuditIQ)

---

## 🧠 Overview
**AuditIQ** scans accounting data to automatically detect irregular or high-risk transactions using unsupervised machine-learning models.  
It helps users quickly identify potential fraud or anomalies across their financial data.

Ideal for:
- Students learning accounting or data analytics  
- Auditors or finance interns reviewing transactions  
- Small businesses tracking unusual activity  

---

## ⚙️ Features
✅ Upload CSV data (Date, Description, Category, Amount)  
✅ Detect anomalies using **Isolation Forest ML model**  
✅ Interactive data visualizations (Seaborn + Matplotlib)  
✅ Adjustable anomaly sensitivity  
✅ Downloadable “Audit Report” with risk flags  
✅ Streamlit-powered, no installation required  

---

## 🧩 Tech Stack
- **Python 3.10+**
- **Streamlit** — frontend dashboard  
- **Pandas & NumPy** — data handling  
- **Scikit-learn** — anomaly detection  
- **Matplotlib / Seaborn** — visualization  

---

## 📂 Project Structure


---

## 🧪 How It Works
1. Upload or use the included `sample_data.csv`  
2. AuditIQ processes the dataset and computes anomaly scores  
3. Suspicious transactions are flagged visually and listed in a report  
4. Adjust sensitivity using the sidebar to refine detection results  

---

## 📸 Preview
| Dashboard Preview |
|:--:|
| ![AuditIQ Screenshot](https://i.imgur.com/XN6N3uB.png) |  

*(You can upload your own screenshot to Imgur and replace the link above)*

---

## 🧠 Example Use Case
**Scenario:**  
A freelance accountant uploads a client’s expense data.  
AuditIQ highlights one suspicious “Client Payment - Income - $12,000” transaction — potentially miscoded or fraudulent.  

---

## 🧰 Local Setup
If you want to run it locally:
```bash
git clone https://github.com/kaushikatla-cell/AuditIQ.git
cd AuditIQ
pip install -r requirements.txt
streamlit run app.py

