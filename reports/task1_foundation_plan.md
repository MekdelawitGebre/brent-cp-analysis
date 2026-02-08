# Task 1 – Laying the Foundation for Brent Oil Price Analysis

## Objective
Define the data analysis workflow, develop understanding of the model, and prepare for analyzing how major events affect Brent oil prices.

---

## 1. Data Analysis Workflow

### Step 1: Data Loading
- Load historical Brent oil prices from `data/raw/brent_raw.csv`.
- Parse the `Date` column correctly (format: `dd-MMM-yy`) and sort chronologically.
- Handle missing values and ensure numeric prices.

### Step 2: Exploratory Data Analysis (EDA)
- Visualize raw prices to identify trends and patterns.
- Compute log returns and rolling volatility.
- Conduct stationarity test (ADF) to guide time series modeling.

### Step 3: Event Data Integration
- Compile a structured dataset of major geopolitical, economic, and policy events affecting oil prices: `data/events/external_events.csv`.
- Include columns: `Date`, `Short Title`, `Category`, `Description`.
- Map events to corresponding time periods in the Brent dataset.

### Step 4: Statistical Modeling Preparation
- Investigate time series properties: trend, volatility, stationarity.
- Identify potential periods for Bayesian change point modeling.
- Document assumptions for subsequent analysis.

### Step 5: Reporting & Communication
- Save visualizations in `reports/`.
- Prepare Markdown reports for stakeholders.
- Optional: future interactive dashboards (Streamlit/Jupyter).

---

## 2. Event Dataset Overview

| Date       | Short Title           | Category  | Description                                           |
|-----------|---------------------|-----------|-------------------------------------------------------|
| 2010-12-17 | Arab Spring          | Conflict  | Regional protests disrupting MENA oil supply |
| 2011-02-15 | Libyan Civil War     | Conflict  | Civil war in Libya disrupts crude exports            |
| 2014-11-28 | OPEC Production Decision | Policy | OPEC chose not to cut production despite price decline |
| 2015-07-14 | Iran Nuclear Deal    | Sanction  | Sanctions relief expected to increase supply  |
| 2016-11-30 | OPEC Cut Agreement   | Policy    | OPEC and non-OPEC production cuts agreed  |
| 2017-06-05 | Qatar Diplomatic Crisis | Political | Gulf states cut ties with Qatar, impacting OPEC unity |
| 2018-05-08 | US Withdrawal from JCPOA | Sanction | Reimposition of sanctions on Iran affecting exports |
| 2018-10-02 | Khashoggi Murder Fallout | Political | Diplomatic tensions affecting Saudi oil relations   |
| 2019-09-14 | Saudi Aramco Attack  | Conflict  | Drone strikes on Abqaiq reduce output temporarily |
| 2020-03-06 | OPEC+ Price War      | Policy    | Breakdown of OPEC+ talks triggers price crash       |
| 2020-03-11 | COVID-19 Pandemic    | Economic  | Global lockdowns sharply reduce demand              |
| 2021-11-26 | Omicron Emergence    | Economic  | New COVID variant renews demand fears              |
| 2022-02-24 | Russia-Ukraine War   | Conflict  | Invasion drives global oil supply fears |
| 2022-03-08 | US Ban on Russian Oil | Sanction | US bans Russian oil imports, tightening supply   |
| 2015-01-01 | China Economic Slowdown | Economic | Reduced Chinese demand contributes to price weakness |

---

## 3. Assumptions & Limitations
- **Correlation vs causation:** Statistical correlation is measured, not causal impact.
- **Approximate event dates:** Some events are not exact to the day.
- **External factors:** Other market dynamics (technology, inventory, natural disasters) are not included.
- **Stationarity:** Log returns are assumed stationary; high volatility may violate assumptions.
- **Data accuracy:** Historical prices are assumed accurate; errors in raw data may affect results.

---

## 4. Communication Plan
- **Visual Reports:** Figures saved in `reports/` folder.
- **Markdown Report:** `task1_foundation_plan.md` for stakeholders.
- **GitHub Repository:** Main branch stores all code, data, and documentation.
- **Optional Dashboards:** Future Streamlit or Jupyter dashboards.

---

## 5. Change Point Model Understanding
- **Purpose:** Identify time points where Brent oil price behavior shifts (structural breaks).
- **Method:** Bayesian change point detection using PyMC:
  - Models data as segments with different statistical properties (mean, variance).
  - Infers most probable points where changes occur.
- **Expected Outputs:**
  - Estimated change point dates.
  - Posterior distributions of segment parameters (mean, volatility).
- **Limitations:**
  - Detects statistical changes, which may not correspond to causal events.
  - Sensitive to hyperparameters and priors.

---

## 6. Expected Outputs
- Time series plots: raw prices and rolling volatility.
- ADF test results confirming log return stationarity.
- Structured CSV of key events.
- Markdown report documenting workflow, assumptions, communication plan, and change point understanding.
- Figures saved in `reports/` folder for stakeholder presentation.

---

## 7. Next Steps
- Implement Bayesian change point detection (Task 2).
- Integrate events dataset to interpret detected change points.
- Perform deeper statistical analysis and generate preliminary insights.
