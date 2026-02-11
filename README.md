# Brent Oil Price Change-Point Analysis

---

## Overview

This repository provides a **comprehensive analysis of Brent oil price fluctuations** using historical data, Bayesian change point modeling, and major political, economic, and policy events. The goal is to identify structural changes in price trends and help stakeholders visualize how external events correlate with Brent oil prices.

The project is divided into three tasks:

1. **Task 1 – Laying the Foundation**: Data preparation, exploratory analysis, and event dataset creation.
2. **Task 2 – Change Point Modeling**: Detecting structural breaks using Bayesian change point models.
3. **Task 3 – Interactive Dashboard**: React-based dashboard integrating price, events, and change points.

---

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Task 1 – Data Analysis Foundation](#task-1---data-analysis-foundation)
3. [Task 2 – Change Point Modeling](#task-2---change-point-modeling)
4. [Task 3 – Interactive Dashboard](#task-3---interactive-dashboard)
5. [Setup Instructions](#setup-instructions)
6. [How to Run](#how-to-run)
7. [Key Features](#key-features)
8. [Assumptions & Limitations](#assumptions--limitations)

---

## Repository Structure

```
brent-cp-analysis/
├── backend/
│   ├── app.py                   # Flask API
│   ├── data/
│   │   ├── raw/                 # Raw price & event CSVs
│   │   ├── events/              # Structured events CSV
│   │   └── processed/           # Change points CSV
│   └── data_loader.py           # Data preprocessing
├── frontend/
│   ├── src/
│   │   ├── components/          # React components: PriceChart, EventPanel
│   │   ├── App.jsx              # Main React app
│   │   └── styles/App.css       # Dashboard styling
│   ├── package.json
│   └── vite.config.js
├── notebooks/                   # Jupyter notebooks for EDA & modeling
├── reports/                     # Figures & markdown reports
├── requirements.txt
└── README.md
```

---

## Task 1 – Data Analysis Foundation

**Objective:** Prepare and explore historical Brent price data, integrate events dataset, and plan analysis workflow.

**Key Steps:**

* Load raw Brent price data (`data/raw/brent_raw.csv`).
* Parse and sort dates; handle missing/invalid values.
* Conduct **EDA**: price trends, log returns, rolling volatility, stationarity tests (ADF).
* Integrate **structured events dataset** (`data/events/external_events.csv`) with columns: `Date`, `Short Title`, `Category`, `Description`.
* Save visualizations and markdown report in `reports/`.

**Output Examples:**

* `reports/fig_brent_price.png` – Historical price trend
* `reports/02_rolling_vol.png` – Rolling volatility
* `reports/task1_foundation_plan.md` – Analysis workflow documentation

---

## Task 2 – Change Point Modeling

**Objective:** Detect structural breaks in Brent oil prices using Bayesian change point analysis.

**Method:**

* PyMC-based Bayesian change point modeling
* Estimates mean/variance segments
* Infers probable change points

**Example Output:**

| Parameter | Mean  | 95% HDI Lower | 95% HDI Upper |
| --------- | ----- | ------------- | ------------- |
| μ₁        | 2.980 | 2.973         | 2.988         |
| μ₂        | 4.241 | 4.231         | 4.251         |
| σ₁        | 0.266 | 0.261         | 0.272         |
| σ₂        | 0.364 | 0.357         | 0.371         |

**Detected Change Point:**

* Date: 2004-04-27
* Mean price change: +253% (from ~$19.69 to ~$69.49)
* Events within ±30 days: None in current dataset

**Output Files:**

* `reports/02_changepoint_summary.csv`
* Figures: `02_piecewise_means.png`, `02_trace_plot.png`, etc.

---

## Task 3 – Interactive Dashboard

**Objective:** Provide a React-based dashboard to visualize price trends, events, and change points interactively.

**Key Features:**

* **Interactive price chart** with markers for events and change points
* **Event highlight & drill-down panel**
* **Date range filters** and **category filters**
* **Responsive design** for desktop, tablet, and mobile
* Real-time data fetching from Flask API (`/api/historical`, `/api/events`, `/api/changepoints`)

**Frontend Tech:** React, Recharts, Axios
**Backend Tech:** Flask, Pandas, Flask-CORS

**Screenshots:**

* Price chart with colored event markers
* Event panel showing event details on click

---

## Setup Instructions

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

* Runs backend at `http://127.0.0.1:5000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

* Runs dashboard at `http://localhost:5173`

---

## How to Run End-to-End

1. Start **backend Flask API** first
2. Start **frontend React app**
3. Open browser at `http://localhost:5173`
4. Select **date range** and **event category** to explore correlations
5. Click on event markers to view details in the side panel

---

## Key Features

* Historical Brent price visualization
* Bayesian change point detection integration
* Event highlighting (conflict, policy, sanction, economic, disaster)
* Drill-down panels for event details
* Filters for date ranges and event categories
* Responsive layout for all devices

---

## Assumptions & Limitations

* Correlation ≠ causation; events may not directly cause price shifts
* Event dates approximate
* Only major political/economic/policy events considered
* Model sensitive to hyperparameters
* Data quality assumed for historical price dataset

---

