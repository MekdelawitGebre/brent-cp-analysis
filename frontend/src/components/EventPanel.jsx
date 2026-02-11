import React from "react";
import "../styles/App.css";

const EventPanel = ({ event, onClose }) => {
  if (!event) return null;

  return (
    <div className="event-panel">
      <button className="close-btn" onClick={onClose}>×</button>
      <h3>{event.title}</h3>
      <p><strong>Category:</strong> {event.category}</p>
      <p><strong>Date:</strong> {event.date}</p>
      <p><strong>Description:</strong></p>
      <p>{event.description}</p>
    </div>
  );
};

export default EventPanel;
