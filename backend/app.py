from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access

# Load historical prices
prices_df = pd.read_csv("data/raw/brent_raw.csv")  # Date,Price
prices_df["Date"] = pd.to_datetime(prices_df["Date"], dayfirst=True)

# Load events
events_df = pd.read_csv("data/events/external_events.csv")  # Date,Short Title,Category,Description
events_df["Date"] = pd.to_datetime(events_df["Date"], dayfirst=True)

# Load change points 
try:
    cp_df = pd.read_csv("data/processed/change_points.csv")  # Date
    cp_df["Date"] = pd.to_datetime(cp_df["Date"], dayfirst=True)
except FileNotFoundError:
    cp_df = pd.DataFrame(columns=["Date"])


@app.route("/api/historical")
def historical():
    start = request.args.get("start")
    end = request.args.get("end")
    df = prices_df.copy()
    if start:
        df = df[df["Date"] >= pd.to_datetime(start)]
    if end:
        df = df[df["Date"] <= pd.to_datetime(end)]
    df = df.sort_values("Date")
    result = [{"date": d.strftime("%Y-%m-%d"), "price": p} for d, p in zip(df["Date"], df["Price"])]
    return jsonify(result)


@app.route("/api/events")
def events():
    df = events_df.copy()
    result = []
    for _, row in df.iterrows():
        result.append({
            "date": row["Date"].strftime("%Y-%m-%d"),
            "title": row["Short Title"],
            "category": row["Category"],
            "description": row["Description"]
        })
    return jsonify(result)


@app.route("/api/changepoints")
def changepoints():
    df = cp_df.copy()
    result = [{"date": d.strftime("%Y-%m-%d")} for d in df["Date"]]
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
