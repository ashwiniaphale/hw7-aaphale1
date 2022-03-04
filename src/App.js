import './App.css';
import { useState } from 'react';

function App() {

  const [fact, setFact] = useState('')

  function handleClick() {
    fetch('/fun_fact').then(response => response.json()).then(data => {
      setFact(data) //grabbing data and passing it through setFact within the useState hook
    })

  }
  return (
    <div>
      <center>
        <p>{fact}</p>
        <button onClick={handleClick}>Click for a fun fact!</button>
      </center>
    </div>
  );
}

export default App;
