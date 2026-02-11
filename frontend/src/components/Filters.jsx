import React from "react";

const Filters = ({ startDate, endDate, onDateChange }) => {
  return (
    <div style={{ margin: "1rem 0" }}>
      <label>
        Start Date: 
        <input 
          type="date" 
          value={startDate} 
          onChange={e => onDateChange("start", e.target.value)} 
        />
      </label>
      <label style={{ marginLeft: "1rem" }}>
        End Date: 
        <input 
          type="date" 
          value={endDate} 
          onChange={e => onDateChange("end", e.target.value)} 
        />
      </label>
    </div>
  );
};

export default Filters;
