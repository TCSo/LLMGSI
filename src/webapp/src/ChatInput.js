import React, { useState } from 'react';
import './App.css'
import { APIURL } from './constants';

const ChatInput = ({ messages, setMessages, newMessage, setNewMessage }) => {
    const [isLoading, setIsLoading] = useState(false);

    const handleInputChange = (event) => {
        setNewMessage(event.target.value);
    };

    const handleKeyDown = (event) => {
        if (!isLoading && event.key === 'Enter') {
            handleSendMessage(newMessage);
        }
    };

    const handleSendMessage = async () => {
        let tempMessage = messages
        if (newMessage.trim() !== '') {
          tempMessage = [...tempMessage, { text: newMessage, sender: 'user' }]
          setMessages(tempMessage);
          
          const data = {
            input: newMessage,
          };
    
          setIsLoading(true);
          await fetch(APIURL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
          })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);
            if (data.succeed == 1) {
              tempMessage = [...tempMessage, { text: data.data, sender: 'llmgsi' }]
              setMessages(tempMessage);
            }
          })
          .catch(error => console.error('Error:', error));
          setNewMessage('');
          setIsLoading(false);
        }
      };

    return (
        <div>
            <div className="chat-input">
                <input
                    type="text"
                    placeholder="Type your message..."
                    value={newMessage}
                    onKeyDown={handleKeyDown}
                    onChange={handleInputChange}
                    disabled = {(isLoading)? "disabled" : ""}
                />
                {isLoading &&<button className='disabled-button'>Generating</button>}
                {!isLoading && <button onClick={handleSendMessage}>Send</button>}
            </div>
        </div>
    );
};

export default ChatInput;