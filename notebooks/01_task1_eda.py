import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import os
import sys

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "brent_raw.csv")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORT_DIR, exist_ok=True)

# --- Functions ---
def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path, header=0)
    if df.empty:
        raise ValueError("Data file is empty.")
    try:
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='raise')
        df["Date"] = df["Date"].apply(lambda d: d.replace(year=d.year-100) if d.year > 2022 else d)
    except Exception as e:
        raise ValueError(f"Error parsing dates: {e}")
    return df.sort_values("Date").reset_index(drop=True)

def compute_log_returns(df):
    df["LogPrice"] = np.log(df["Price"])
    df["Return"] = df["LogPrice"].diff()
    return df

def plot_price(df, report_dir):
    plt.figure(figsize=(12,5))
    plt.plot(df["Date"], df["Price"], color="steelblue")
    plt.title("Brent Oil Prices (1987–2022)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD/barrel)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(report_dir, "fig_brent_price.png"))
    plt.close()

def plot_rolling_volatility(df, report_dir, window=90):
    df["RollingVol"] = df["Return"].rolling(window).std()
    plt.figure(figsize=(12,4))
    plt.plot(df["Date"], df["RollingVol"], color="tomato")
    plt.title(f"{window}-Day Rolling Volatility (Log Returns)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(report_dir, "fig_rolling_vol.png"))
    plt.close()

def adf_test(df):
    returns = df["Return"].dropna()
    result = adfuller(returns)
    print(f"ADF Statistic: {result[0]:.4f}, p-value: {result[1]:.4f}")

# --- Main ---
if __name__ == "__main__":
    try:
        df = load_data(DATA_PATH)
        df = compute_log_returns(df)
        plot_price(df, REPORT_DIR)
        plot_rolling_volatility(df, REPORT_DIR)
        adf_test(df)
        print("✅ EDA complete – plots saved in 'reports/'")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)



