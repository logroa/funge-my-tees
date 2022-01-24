import './App.css';
import Closet from './components/Closet'

function App() {
  const coin = '/images/pixal-coin.svg';
  return (
    <div className="App">
      <header className="App-header">
        <img src={coin} className="App-logo" alt="logo" />
        <h1>FungeMyTees.com</h1>
      </header>
      <Closet url='http://localhost:8000/api/shirts/' className='following'/>
    </div>
  );
}

export default App;
