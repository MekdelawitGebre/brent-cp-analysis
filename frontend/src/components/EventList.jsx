import React from "react";

const EventList = ({ events, onSelectEvent }) => {
  return (
    <div style={{ margin: "1rem 0" }}>
      <h3>Events</h3>
      <ul>
        {events.map((event, idx) => (
          <li 
            key={idx} 
            style={{ cursor: "pointer", margin: "0.5rem 0", color: "blue" }}
            onClick={() => onSelectEvent(event)}
          >
            {event}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventList;
