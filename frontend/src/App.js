import React, { useState, useEffect } from "react";
import './styles.css';
import {BrowserRouter, Routes, Route } from 'react-router-dom';
import RegistrationForm1 from "./components/RegistrationForm/RegistrationForm1";
import StartPage from "./components/StartPage"
import Header from "./components/Header";


  /*
  const [text, setText] = useState([]);
  const [originalNumber] = useState(6);
  const [modifiedNumber, setModifiedNumber] = useState(null);

/*  useEffect(() => {
    fetch(' http://localhost:8000/test1').then(res => res.json()).then(data => {
        setText(data.message);
      });
    }, []);


    const handleSendNumber = async () => {
      try {
        const response = await fetch('http://localhost:8000/client_login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ id: 1 }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setModifiedNumber(data.login);
      } catch (error) {
        console.error('Error:', error);
      }
    };


  return (
    <div className="font-bold justify-center p-2">

      <div className="font-bold text-6xl justify-center p-6">
      Hello World :) Status django {text}
      </div>

      <div className="p-4 text-xl">
        <p>React: Moja liczba to {originalNumber} pomnóż ją razy 4 proszę</p>
          {modifiedNumber && <p>Django: Oto twój wynik {modifiedNumber} :)</p>}
      </div>

    </div>
  );
}
*/
function App() {
  return(
      <div className="App">
            <BrowserRouter>
              <Header />

              <Routes>
              <Route exact path="/start" element={<StartPage />} />
              </Routes>

            </BrowserRouter>
      </div>
);


}
export default App;
