import React, { useState, useEffect } from "react";

function App() {
  const [text, setText] = useState([]);
  const [originalNumber] = useState(6);
  const [modifiedNumber, setModifiedNumber] = useState(null);

  useEffect(() => {
    fetch(' http://localhost:8000/test1').then(res => res.json()).then(data => {
        setText(data.message);
      });
    }, []);


    const handleSendNumber = async () => {
      try {
        const response = await fetch('http://localhost:8000/modify_number/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ number: originalNumber }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setModifiedNumber(data.result);
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
        <p>React: Moja liczba to {originalNumber} pomnóż ją razy 2 proszę</p>
        <button onClick={handleSendNumber}>Wyślij do Django</button>
          {modifiedNumber && <p>Django: Oto twój wynik {modifiedNumber} :)</p>}
      </div>

    </div>
  );
}

export default App;
