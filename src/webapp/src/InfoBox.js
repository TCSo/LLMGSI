import React, { useState } from 'react';

const InfoBox = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleInfoBox = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <>
      <div className='infobox-content'>
        <button onClick={toggleInfoBox}>Toggle Credits</button>
      </div>
      <div>
        {isExpanded && (
        <div className='infobox'>
          {/* Your info box content goes here */}
          <p>Created by Eddie Song, Zixun Huang, Tomson Qu, Qingyuan Liu, Eric Li, Yike Wang For CS 196-194.</p>
        </div>
      )}
      </div>
    </>
  );
};



export default InfoBox;
