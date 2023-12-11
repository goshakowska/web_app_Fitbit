import React, { useState } from "react";
import {
    Input,
    InputGroup,
    Button,
    NavLink
  } from 'reactstrap';
  import '../styles/loginStyles.css'

function LoginForm (props)
{
    const [login, setLogin] = useState()
    const [password, setPassword] = useState()

    return(
    <div className="login-form">
        <h1 className="text-style-login">Zaloguj się</h1>
        <div>
            <InputGroup className="input-group">
                <Input className='centered-text-input' placeholder="login" onChange={ev => setLogin(ev.target.value)} />
            </InputGroup>
            <InputGroup className="input-group">
                <Input className='centered-text-input' type="password" placeholder="hasło" onChange={ev => setPassword(ev.target.value)}/>
            </InputGroup>
        </div>
        <div>
            <Button
                className="button-style-login-user text-style"
            >
            ZALOGUJ SIĘ
            </Button>
        </div>
        <div className="link-texts-group">
            <NavLink href="./rejestracja" className="link-texts">Nie masz jeszcze konta? Załóż je tutaj!
            </NavLink>
            <NavLink href="./rejestracja" className="link-texts">Jesteś pracownikiem? Zaloguj się tutaj!
            </NavLink>
        </div>

    </div>
    )

}

export default LoginForm;