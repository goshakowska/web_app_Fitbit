import { useState } from "react";

function StartPage()
{
    const [cliLogin, setcliLogin] = useState(null);

    const handleDBcon = async () => {
        try {
          const response = await fetch('http://localhost:8000/client/client_login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login: 'krol_wro', password: '123' }),
          });

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          setcliLogin(data.id);
          alert('Z bazy pobrano login: '+ data.id);
        } catch (error) {
          alert('Wykryto błąd');
          console.error('Error:', error);
        }
      };

      //<button type='submit' onClick={handleDBcon} className="mt-4 px-4 py-2 bg-orange-500 text-black rounded hover:bg-orange-600">Przetestuj połączenie z bazą</button>
    return (
        <div className="loginForm">
        <h className='startPageText1'> FitBit </h>
        <h className='startPageText2'> HEALTH. STRENGTH. POWER. </h>
      </div>
    );

}

export default StartPage;