import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer,
} from "recharts";

const PriceChart = ({ startDate, endDate, onEventClick, categoryFilter }) => {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoints, setChangePoints] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:5000/api/historical", {
          params: { start: startDate, end: endDate },
        });
        setData(res.data);

        const ev = await axios.get("http://127.0.0.1:5000/api/events");
        setEvents(ev.data);

        const cp = await axios.get("http://127.0.0.1:5000/api/changepoints");
        setChangePoints(cp.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchData();
  }, [startDate, endDate]);

  const filteredEvents = events.filter(ev => categoryFilter === "All" || ev.category === categoryFilter);

  const chartData = data.map(d => {
    const event = filteredEvents.find(e => e.date === d.date);
    const cp = changePoints.find(c => c.date === d.date);
    return { ...d, event, changePoint: !!cp };
  });

  const CustomDot = ({ cx, cy, payload }) => {
    if (payload.event) {
      return (
        <circle
          cx={cx}
          cy={cy}
          r={6}
          fill={
            payload.event.category === "Conflict" ? "red" :
            payload.event.category === "Policy" ? "green" :
            payload.event.category === "Sanction" ? "orange" : "blue"
          }
          stroke="none"
          onClick={() => onEventClick(payload.event)}
          style={{ cursor: "pointer" }}
        />
      );
    }
    if (payload.changePoint) {
      return <circle cx={cx} cy={cy} r={4} fill="purple" />;
    }
    return null;
  };

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={chartData}>
        <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="price" stroke="#007bff" dot={<CustomDot />} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default PriceChart;

