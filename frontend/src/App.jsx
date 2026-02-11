import React, { useState } from "react";
import PriceChart from "./components/PriceChart";
import EventPanel from "./components/EventPanel";
import "./styles/App.css";

function App() {
  const [startDate, setStartDate] = useState("2010-01-01");
  const [endDate, setEndDate] = useState("2025-12-31");
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [categoryFilter, setCategoryFilter] = useState("All");

  return (
    <div className="dashboard-container">
      <h1>Brent Oil Price Dashboard</h1>

      <div className="filters">
        <label>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <label>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </label>
        <label>
          Event Category:
          <select value={categoryFilter} onChange={(e) => setCategoryFilter(e.target.value)}>
            <option value="All">All</option>
            <option value="Conflict">Conflict</option>
            <option value="Policy">Policy</option>
            <option value="Sanction">Sanction</option>
            <option value="Economic">Economic</option>
            <option value="Disaster">Disaster</option>
          </select>
        </label>
      </div>

      <div className="chart-and-panel">
        <div className="chart-container">
          <PriceChart
            startDate={startDate}
            endDate={endDate}
            onEventClick={setSelectedEvent}
            categoryFilter={categoryFilter}
          />
        </div>

        {selectedEvent && (
          <EventPanel event={selectedEvent} onClose={() => setSelectedEvent(null)} />
        )}
      </div>
    </div>
  );
}

export default App;
