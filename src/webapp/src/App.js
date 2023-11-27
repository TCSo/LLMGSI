import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  const handleInputChange = (event) => {
    setNewMessage(event.target.value);
  };

  const handleSendMessage = () => {
    if (newMessage.trim() !== '') {
      setMessages([...messages, { text: newMessage, sender: 'user' }]);
      // Here you might want to make an API call or handle the response from a chatbot
      // For simplicity, we're just adding the user's message to the state.
      const url = 'http://localhost:8000';
      const data = {
        question: newMessage,
      };

      fetch(url, {
        method: 'POST', // or 'GET' depending on your server
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), // If you're sending JSON data
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        setMessages([...messages, { text: data, sender: 'LLMGSI' }]);
      })
      .catch(error => console.error('Error:', error));

      setNewMessage('');
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            placeholder="Type your message..."
            value={newMessage}
            onChange={handleInputChange}
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
