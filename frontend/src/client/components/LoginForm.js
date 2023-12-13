import React, { useState } from "react";
import {
    Input,
    InputGroup,
    Button,
    NavLink
  } from 'reactstrap';
  import '../styles/loginStyles.css'
  import clientToken from "../ClientToken";

function LoginForm ()
{
    const [userLoginInput, setUserLoginInput] = useState("") // to co użytkownik wpisuje do zalogowania
    const [userPassword, setUserPassword] = useState("")
    const [loggingError, setLoggingError] = useState("")
    const {login} = clientToken();

    const errorHandle = () =>
    {
        setLoggingError("")
        setLoggingError("")
        if ("" === userLoginInput) {
            setLoggingError("Wprowadź swój login.")
            return
        }
        if ("" === userPassword) {
            setLoggingError("Wprowadź swoje hasło.")
            return
        }
    }

    const handleLogin = async (event) =>
    {
        errorHandle();
        event.preventDefault();
        if(loggingError===""){
        try {
            const response = await fetch('http://localhost:8000/client/client_login/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ login: userLoginInput,
                                      password: userPassword}),

            });
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            login(data.id, data.name);
            window.location.href = '/'

          } catch (error) {if(error.message.includes('Incorrect user login!')){
            setLoggingError('Niepoprawny login lub hasło. Spróbuj ponownie.');
            setUserLoginInput('');
            setUserPassword('');
        } else {
            console.error('Unhandled error:', error);
        }
        }
    }
        };


    return(
    <div className="loginForm">
        <h1 className="textLogin">Zaloguj się</h1>
        <div>
            <InputGroup className="inputGroup">
                <Input className='centeredTextInput' placeholder="login" onChange={ev => setUserLoginInput(ev.target.value)} />
            </InputGroup>
            <InputGroup className="inputGroup">
                <Input className='centeredTextInput' type="password" placeholder="hasło" onChange={ev => setUserPassword(ev.target.value)}/>
            </InputGroup>
            <label className="errorLabel"> {loggingError} </label>
        </div>
        <div>
            <Button
                className="buttonStyleLoginUser text-style" onClick={handleLogin}
            >
            ZALOGUJ SIĘ
            </Button>
        </div>
        <div className="linkTextsGroup">
            <NavLink href="./rejestracja" className="linkTexts">Nie masz jeszcze konta? Załóż je tutaj!
            </NavLink>
            <NavLink href="./rejestracja" className="linkTexts">Jesteś pracownikiem? Zaloguj się tutaj!
            </NavLink>
        </div>

    </div>
    )

}

export default LoginForm;