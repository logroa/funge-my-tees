import logo from './logo.svg';
import './App.css';
import Closet from './components/Closet'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>FungeMyTees.com</h1>
      </header>
      <Closet url='http://localhost:8000/api/shirts/' />
    </div>
  );
}

export default App;
