import React from 'react';
import './App.css';
import InfoBox from './InfoBox';

const Header = () => {
  return (
    <header className='header'>
      <p>LLMGSI</p>
      <InfoBox/>
    </header>
  );
};

export default Header;
