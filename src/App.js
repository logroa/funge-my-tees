import React from 'react';
import './App.css';
import Closet from './components/Closet';

function App() {
  const coin = '../src/images/pixal-coin.svg';
  const api_url = "http://localhost:8000/api/shirts/";  //'https://nfteeshirts.herokuapp.com/api/shirts/';

  return (
    <div className="App">
      <header className="App-header">
        <img src={coin} className="App-logo" alt="logo" />
        <h1>FungeMyTees.com</h1>
      </header>
      <Closet url={api_url} className='following'/>
    </div>
  );
}

export default App;
