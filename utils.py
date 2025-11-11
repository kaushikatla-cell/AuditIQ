import pandas as pd

REQUIRED_COLS = ["Date", "Description", "Category", "Amount"]

def load_data(uploaded_file_or_path):
    df = pd.read_csv(uploaded_file_or_path)
    # Basic validation
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"CSV is missing required columns: {missing}")

    # Parse dates and clean
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Amount"])
    return df

def summarize_data(df):
    total = df["Amount"].sum()
    mean_amt = df["Amount"].mean()
    std_amt = df["Amount"].std()
    count = len(df)
    return {
        "Transactions": int(count),
        "Total Amount": round(total, 2),
        "Average Amount": round(mean_amt, 2),
        "Std Dev Amount": round(std_amt, 2)
    }
