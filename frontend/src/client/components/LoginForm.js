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
    const [userLoginInput, setUserLoginInput] = useState("")
    const [userPassword, setUserPassword] = useState("")
    const [loggingError, setLoggingError] = useState("")
    const {login} = clientToken();

    const errorHandle = () =>
    {
        if ("" === userLoginInput) {
            setLoggingError("Wprowadź swój login.");
            return true
        }
        if ("" === userPassword) {
            setLoggingError("Wprowadź swoje hasło.");
            return true
        }
        return false;
    }

    const Login = async (event) =>
    {
        event.preventDefault();
        try {
            const response = await fetch('http://localhost:8000/client/client_login/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ login: userLoginInput,
                                      password: userPassword}),

            });

            if (response.status === 400) {
                throw new Error('Incorrect user login.');
            }
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            login(data.id, data.name);
            window.location.href = '/'

          } catch (error) {
            if(error.message.includes('Incorrect user login')){
                setLoggingError('Błędne dane logowania.');
            }
            else{
            console.error('Error:', error);
          }}
        };


        const handleLogin = (event) =>{
            if(errorHandle() === true) {return};
            Login(event);
        }


    return(
    <div className="loginForm">
        <h1 className="textLogin">Zaloguj się</h1>
        <form>
            <InputGroup className="inputGroup">
                <Input className='centeredTextInput' placeholder="login" onChange={ev => { setUserLoginInput(ev.target.value); setLoggingError("")}} />
            </InputGroup>
            <InputGroup className="inputGroup">
                <Input className='centeredTextInput' type="password" placeholder="hasło" onChange={ev => {setUserPassword(ev.target.value); setLoggingError("")}}/>
            </InputGroup>
            <label className="errorLabel"> {loggingError} </label>
        </form>
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