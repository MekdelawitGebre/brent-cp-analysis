# backend/data_loader.py
import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_RAW = os.path.join(BASE_DIR, "data", "raw", "brent_raw.csv")
EVENTS_CSV = os.path.join(BASE_DIR, "data", "events", "external_events.csv")
CP_SUMMARY = os.path.join(BASE_DIR, "reports", "02_changepoint_summary.csv")

def load_prices():
    df = pd.read_csv(DATA_RAW, header=0)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date").reset_index(drop=True)
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    return df

def load_events():
    df = pd.read_csv(EVENTS_CSV, header=0)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    return df.sort_values("Date").reset_index(drop=True)

def load_cp_summary():
    if os.path.exists(CP_SUMMARY):
        return pd.read_csv(CP_SUMMARY)
    else:
        return pd.DataFrame()
