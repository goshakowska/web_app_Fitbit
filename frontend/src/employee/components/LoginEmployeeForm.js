import React, { useState } from "react";
import {
    Input,
    InputGroup,
    Button,
  } from 'reactstrap';
  import '../styles/loginStyles.css'
  import employeeToken from "../EmployeeToken";

function LoginEmployeeForm ()
{
    const [userLoginInput, setUserLoginInput] = useState("")
    const [userPassword, setUserPassword] = useState("")
    const [loggingError, setLoggingError] = useState("")
    const {login} = employeeToken();

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
            const response = await fetch('http://localhost:8000/employee/login/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ login: userLoginInput,
                                      password: userPassword}),

            });

            if (response.status === 400) {
                throw new Error('Incorrect employee login or password');
            }
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            login(data.id, data.name, data.type);
            console.log(data.type);
            window.location.href = '/' + data.type;

          } catch (error) {
            if(error.message.includes('Incorrect employee login or password')){
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
        <h1 className="textLogin">Logowanie pracowników</h1>
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
    </div>
    )

}

export default LoginEmployeeForm;