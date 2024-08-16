import React, { useState } from "react";
import "./App.css";
import axios from "axios";
import Skeleton from '@mui/material/Skeleton';

function App() {
  const [userInput, setUserInput] = useState("");
  const [conversationHistory, setConversationHistory] = useState([]);
  const [loading, setLoading] = useState(false); // Loading state to show the skeleton

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true); // Set loading to true when request is sent

    // Append the user's question to the conversation history
    const newConversationHistory = [
      ...conversationHistory,
      { sender: "User", message: userInput },
    ];

    setConversationHistory(newConversationHistory);

    try {
      // Send the question to the Flask backend (Flask API)
      // const response = await axios.post("http://ec2-34-219-62-77.us-west-2.compute.amazonaws.com:5000/suggestions", {
      //   question: userInput,
      // });

      const response = await axios.post("http://localhost:5000/suggestions", {
        question: userInput,
      });



      // Append the AI's response to the conversation history
      setConversationHistory([
        ...newConversationHistory,
        { sender: "AI", message: response.data.suggestions },
      ]);
    } catch (error) {
      console.error("Error fetching AI response:", error);
    }

    setLoading(false); // Set loading to false after response is received
    setUserInput(""); // Clear the user input after submission
  };

  return (
    <div className="chat-app">
      <h1>Gift Suggestion</h1>
      <div className="chat-history">
        {conversationHistory.map((entry, index) => (
          <div key={index} className={`chat-message ${entry.sender.toLowerCase()}`}>
            {entry.sender === "AI" ? (
              <>
                <div>
                  <img src="/confetti.png" alt="AI Icon" className="ai-icon" />
                </div>
                <div className="ai-message">
                  <span>{entry.message}</span>
                </div>
              </>
            ) : (
            entry.message
            )}
          </div>
        ))}
        
        {/* Show Skeleton while loading */}
        {loading && (
          <div className="chat-message ai">
            <div>
              <img src="/confetti.png" alt="AI Icon" className="ai-icon" />
            </div>
            <div className="ai-message">
              <Skeleton variant="text" width={300} />
              <Skeleton variant="text" width={250} />
              <Skeleton variant="text" width={200} />
            </div>
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="input-form">
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="Ask a gift suggestion..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
