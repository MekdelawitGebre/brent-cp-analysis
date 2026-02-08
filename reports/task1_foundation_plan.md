# Task 1 – Laying the Foundation for Brent Oil Price Analysis

## Objective
Define the data analysis workflow, understand the model, and prepare for analyzing how major events affect Brent oil prices.

---

## 1. Data Analysis Workflow

### Step 1: Data Loading
- Load historical Brent oil prices from `data/raw/brent_raw.csv`.
- Parse `Date` column and sort chronologically.
- Handle missing values and invalid data.

### Step 2: Exploratory Data Analysis (EDA)
- Visualize raw prices.
- Compute log returns and rolling volatility.
- Conduct stationarity test (ADF).

### Step 3: Event Data Integration
- Use structured dataset: `data/events/external_events.csv`.
- Columns: `Date`, `Short Title`, `Category`, `Description`.
- Map events to Brent prices timeline.

### Step 4: Statistical Modeling Preparation
- Analyze trend, volatility, stationarity.
- Identify potential periods for Bayesian change point modeling.
- Document assumptions.

### Step 5: Reporting & Communication
- Save figures in `reports/`.
- Markdown reports for stakeholders.
- Optional dashboards in Streamlit/Jupyter.

---

## 2. Event Dataset Overview

- `data/events/external_events.csv` contains 15+ key events.
- Columns: Date (YYYY-MM-DD), Short Title, Category, Description.
- Examples: Arab Spring, Libyan Civil War, OPEC decisions, COVID-19, Russia-Ukraine war.

---

## 3. Assumptions & Limitations
- Correlation vs causation: statistical correlation does not prove causality.
- Approximate event dates.
- External factors not included (technology, natural disasters, inventories).
- Stationarity assumed for log returns.
- Data accuracy assumed; missing/incorrect values may impact results.

---

## 4. Communication Plan
- Figures saved in `reports/`.
- Markdown reports for stakeholders.
- GitHub repository contains code, data, and documentation.
- Optional dashboards for interactive exploration.

---

## 5. Change Point Model Understanding
- **Purpose:** Detect structural breaks in Brent prices.
- **Method:** Bayesian change point detection (PyMC):
  - Models segments with different mean/variance.
  - Infers most probable change points.
- **Expected Outputs:** Change point dates, posterior distributions of segment parameters.
- **Limitations:** Detects statistical changes, may not correspond to causal events; sensitive to hyperparameters.

---

## 6. Expected Outputs
- Plots: raw prices and rolling volatility.
- ADF test results.
- Structured events CSV.
- Markdown report.
- Figures in `reports/`.

---

## 7. Next Steps
- Task 2: Bayesian change point modeling.
- Integrate events to interpret detected change points.
- Deeper statistical analysis and preliminary insights.
