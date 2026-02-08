import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "brent_raw.csv")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORT_DIR, exist_ok=True)

# --- Load dataset ---
# Assumes CSV has header: Date,Price
df = pd.read_csv(DATA_PATH, header=0)

# --- Parse date ---
# Use dayfirst=True since your CSV is like '20-May-87'
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='raise')

# Fix 2-digit years (e.g., '87' → 1987)
df["Date"] = df["Date"].apply(lambda d: d.replace(year=d.year-100) if d.year > 2022 else d)

# Sort chronologically
df = df.sort_values("Date").reset_index(drop=True)

# --- Plot raw Brent prices ---
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Price"], color="steelblue")
plt.title("Brent Oil Prices (1987–2022)")
plt.xlabel("Date")
plt.ylabel("Price (USD/barrel)")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(REPORT_DIR, "fig_brent_price.png"))
plt.close()

# --- Log returns & stationarity test ---
df["LogPrice"] = np.log(df["Price"])
df["Return"] = df["LogPrice"].diff()

# Drop NaN from first diff
returns = df["Return"].dropna()

adf_result = adfuller(returns)
print(f"ADF Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")

# --- Rolling volatility (90-day window) ---
df["RollingVol"] = returns.rolling(90).std()
plt.figure(figsize=(12,4))
plt.plot(df["Date"], df["RollingVol"], color="tomato")
plt.title("90-Day Rolling Volatility (Log Returns)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(REPORT_DIR, "fig_rolling_vol.png"))
plt.close()

print("✅ EDA complete – plots saved in 'reports/'")

