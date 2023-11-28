import React, { useEffect, useState } from 'react';
import './App.css';
import ChatInput from './ChatInput';
import Header from './Header';

function App() {
  const url = 'http://127.0.0.1:8080/api/gpt/infer/';

  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [error, setError] = useState(null);

  return (
    <div className="App">
      <Header/>
      <div className="chat-container">
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <ChatInput 
        messages={messages} 
        setMessages={setMessages} 
        newMessage={newMessage}
        setNewMessage={setNewMessage}/>
      </div>
    </div>
  );
}

export default App;
