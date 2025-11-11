import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, contamination=0.05, random_state=42):
    """
    Returns a copy of df with columns:
    - Day (engineered)
    - Anomaly (-1 = anomaly, 1 = normal)
    - RiskFlag ('Suspicious' or 'Normal')
    - AnomalyScore (lower score => more anomalous)
    """
    df = df.copy()
    # Simple feature engineering
    df["Day"] = df["Date"].dt.day
    features = df[["Amount", "Day"]].fillna(0)

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_estimators=200
    )
    model.fit(features)
    preds = model.predict(features)             # -1 anomaly, 1 normal
    scores = model.decision_function(features)  # Lower = more anomalous

    df["Anomaly"] = preds
    df["AnomalyScore"] = scores
    df["RiskFlag"] = df["Anomaly"].apply(lambda x: "Suspicious" if x == -1 else "Normal")
    return df
