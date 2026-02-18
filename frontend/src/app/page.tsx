"use client"; // We need this because we use useEffect

import { useState, useEffect } from "react";

export default function Home() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.TechStack))
      .catch((err) => setMessage("Error while connecting to backend"));
  }, []);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-24 bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-4">MediaTracker</h1>
      <p className="text-xl">
        Backend Status: <span className="text-green-400">{message}</span>
      </p>
    </div>
  );
}