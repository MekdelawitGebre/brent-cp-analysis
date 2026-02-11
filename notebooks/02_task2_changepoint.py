"""
Task 2 – Change Point Modeling and Insight Generation
Brent Oil Prices | PyMC Bayesian Change Point Analysis
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
import pymc as pm
from collections import Counter

# --------------------
# Paths
# --------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "brent_raw.csv")
EVENTS_PATH = os.path.join(BASE_DIR, "data", "events", "external_events.csv")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORT_DIR, exist_ok=True)

# --------------------
# 1. Load & Prepare Data
# --------------------
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="raise")
df["Date"] = df["Date"].apply(lambda d: d.replace(year=d.year-100) if d.year > 2022 else d)
df = df.sort_values("Date").reset_index(drop=True)
df["logP"] = np.log(df["Price"])
df["ret"] = df["logP"].diff()
df = df.dropna().reset_index(drop=True)
print(f"✅ Data loaded: {len(df)} rows from {df['Date'].min().date()} to {df['Date'].max().date()}")

# --------------------
# 2. Exploratory Plots
# --------------------
plt.figure(figsize=(12,4))
plt.plot(df["Date"], df["Price"], color="steelblue")
plt.title("Brent Oil Price (USD/barrel)")
plt.xlabel("Date"); plt.ylabel("Price")
plt.tight_layout(); plt.savefig(f"{REPORT_DIR}/02_price_series.png"); plt.close()

plt.figure(figsize=(12,3))
plt.plot(df["Date"], df["ret"], color="orange")
plt.title("Log Returns of Brent Price")
plt.xlabel("Date"); plt.ylabel("Log Return")
plt.tight_layout(); plt.savefig(f"{REPORT_DIR}/02_returns_series.png"); plt.close()

df["rolling_vol90"] = df["ret"].rolling(90).std()
plt.figure(figsize=(12,3))
plt.plot(df["Date"], df["rolling_vol90"], color="tomato")
plt.title("90-Day Rolling Volatility")
plt.tight_layout(); plt.savefig(f"{REPORT_DIR}/02_rolling_vol90.png"); plt.close()

# --------------------
# 3. Load Event Dataset
# --------------------
events = pd.read_csv(EVENTS_PATH, parse_dates=["Date"])
events = events.sort_values("Date").reset_index(drop=True)

# --------------------
# 4. Bayesian Change Point Model (1 CP)
# --------------------
y = df["logP"].values
idx = np.arange(len(y))

with pm.Model() as model:
    tau = pm.DiscreteUniform("tau", lower=0, upper=len(y)-1)
    mu1 = pm.Normal("mu1", mu=y.mean(), sigma=2)
    mu2 = pm.Normal("mu2", mu=y.mean(), sigma=2)
    sigma1 = pm.HalfNormal("sigma1", sigma=1)
    sigma2 = pm.HalfNormal("sigma2", sigma=1)
    mu = pm.math.switch(idx <= tau, mu1, mu2)
    sigma = pm.math.switch(idx <= tau, sigma1, sigma2)
    obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=y)

    trace = pm.sample(1500, tune=1000, target_accept=0.9, return_inferencedata=True)

az.plot_trace(trace, var_names=["mu1", "mu2", "sigma1", "sigma2"])
plt.savefig(f"{REPORT_DIR}/02_trace_plot.png"); plt.close()

summary = az.summary(trace, var_names=["mu1", "mu2", "sigma1", "sigma2", "tau"], round_to=3)
print(summary)

# --------------------
# 5. Posterior of tau
# --------------------
posterior_tau = trace.posterior["tau"].values.flatten()
mode_tau, count = Counter(posterior_tau).most_common(1)[0]
mode_date = df["Date"].iloc[mode_tau]
print(f"📍 Most likely change point: index={mode_tau}, date={mode_date.date()}")

plt.figure(figsize=(10,3))
sns.histplot(posterior_tau, bins=50, stat="probability", color="teal")
plt.title("Posterior Distribution of Change Point (tau)")
plt.xlabel("tau index")
plt.tight_layout(); plt.savefig(f"{REPORT_DIR}/02_posterior_tau_hist.png"); plt.close()

# --------------------
# 6. Quantify Impact
# --------------------
mu1_post = trace.posterior["mu1"].values.flatten().mean()
mu2_post = trace.posterior["mu2"].values.flatten().mean()
mu1_price = np.exp(mu1_post)
mu2_price = np.exp(mu2_post)
pct_change = (mu2_price - mu1_price) / mu1_price * 100
print(f"Mean before=${mu1_price:.2f}, after=${mu2_price:.2f}, change={pct_change:.2f}%")

# Plot with tau line
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["logP"], color="black", alpha=0.7, label="log Price")
plt.axvline(mode_date, color="red", linestyle="--", label=f"Change Point ({mode_date.date()})")
plt.hlines([mu1_post, mu2_post],
           xmin=[df["Date"].iloc[0], mode_date],
           xmax=[mode_date, df["Date"].iloc[-1]],
           colors=["blue", "green"],
           linestyles="--",
           label=[f"mu1={mu1_post:.3f}", f"mu2={mu2_post:.3f}"])
plt.title("Posterior Mean Levels and Change Point")
plt.legend()
plt.tight_layout(); plt.savefig(f"{REPORT_DIR}/02_piecewise_means.png"); plt.close()

# --------------------
# 7. Match to Events
# --------------------
window = pd.Timedelta(days=30)
nearby = events[(events["Date"] >= mode_date - window) & (events["Date"] <= mode_date + window)]
print("\nEvents within ±30 days of detected change point:")
print(nearby[["Date", "Short Title", "Category", "Description"]].to_string(index=False))

summary_out = {
    "tau_index": int(mode_tau),
    "tau_date": str(mode_date.date()),
    "mu1_price": float(mu1_price),
    "mu2_price": float(mu2_price),
    "pct_change": float(pct_change)
}
pd.DataFrame([summary_out]).to_csv(f"{REPORT_DIR}/02_changepoint_summary.csv", index=False)

print(f"\n✅ All outputs saved in {REPORT_DIR}")
