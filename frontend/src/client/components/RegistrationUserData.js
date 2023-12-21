import React, { useContext, useState} from 'react';
import {
  Input,
  InputGroup,
  Button,
  Form,
  FormFeedback,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationUserData() {
    const {formData, setFormData, handleChange, handleNext} = useContext(FormContext)
    const [loginError, setLoginError] = useState("")

    const isLoginTaken = async (event, login) => {
      try {
          const response = await fetch('http://localhost:8000/client/is_busy_login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login: login}),

          });

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          return(data.is_busy)


        } catch (error) {
          console.error('Error:', error);
        };
      };

      const keysToCheck = ['loginState', 'emailState', 'passwordState', 'repeatedPasswordState']

      const isValid = () => {
        if(keysToCheck.every(key => formData.validate[key] === "has-success")) return true;
        return false;
      }

      const validateLogin = (e) => {
        const { validate, ...userData} = formData;
        const regex = /^[a-z0-9_]+$/;
        if (!(regex.test(e.target.value))) {
          validate.loginState = 'has-danger';
        } else {
          validate.loginState = 'has-success';
        }
        setFormData({validate, ...userData})
      }

      const validateEmail = (e) => {
        const emailRex =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

        const { validate, ...userData} = formData;

        if (emailRex.test(e.target.value)) {
          validate.emailState = 'has-success';
        } else {
          validate.emailState = 'has-danger';
        }

        setFormData({ validate, ...userData });
            }

      const validatePassword = (e) => {
        const { validate, ...userData } = formData;
        console.log(formData);
        if (
          e.target.value.length >= 8 &&
          /[A-Z]/.test(e.target.value) &&
          /[a-z]/.test(e.target.value) &&
          /[0-9]/.test(e.target.value) &&
          /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(e.target.value)
        ) {
          validate.passwordState = 'has-success';
        } else {
          validate.passwordState = 'has-danger';
        }

        setFormData({ validate, ...userData });
      }

      const validateRepeatedPassword = (e) => {
        console.log(formData);
        const {validate, ...userData } = formData;
        if (e.target.value === formData.password) {
          validate.repeatedPasswordState = 'has-success';
        } else {
          validate.repeatedPasswordState = 'has-danger';
        }

        setFormData({ validate, ...userData });
      }


    return(
      <Form className="registrationForm">
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' label="Imię" placeholder="login*" name="login" value={formData.login}
                            valid={formData.validate.loginState === 'has-success'}
                            invalid={formData.validate.loginState === 'has-danger'}
                            onChange={(e) => {
                              setLoginError("");
                              validateLogin(e);
                              handleChange(e);
                            }}/>
            <FormFeedback>
              Login zawiera niedozwolone znaki.
            </FormFeedback>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="e-mail*" name="email" value={formData.email}
                            valid={formData.validate.emailState === 'has-success'}
                            invalid={formData.validate.emailState === 'has-danger'}  onChange={(e) => {
                              validateEmail(e);
                              handleChange(e);
                            }}/>
            <FormFeedback>
              Wprowadź poprawny adres e-mail.
            </FormFeedback>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="hasło*" type= 'password' name="password" value={formData.password}
                            valid={formData.validate.passwordState === 'has-success'}
                            invalid={formData.validate.passwordState === 'has-danger'}  onChange={(e) => {
                              validatePassword(e);
                              handleChange(e);
                            }}/>
            <FormFeedback>
              Hasło musi zawierać co najmniej 8 znaków, małą i wielką literę, cyfrę oraz znak specjalny.
            </FormFeedback>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="powtórz hasło*" type= 'password' name="repeatedPassword" value={formData.repeatedPassword}
              valid={formData.validate.repeatedPasswordState === 'has-success'}
              invalid={formData.validate.repeatedPasswordState === 'has-danger'}  onChange={(e) => {
                validateRepeatedPassword(e);
                handleChange(e);
              }}/>
            <FormFeedback>
              Wprowadzone hasła nie są identyczne.
            </FormFeedback>
          </InputGroup>
          <label className="errorLabel">
              {loginError}
            </label>
          <div>
            <Button className="buttonStyleSwitchPage text-style" type="button" onClick={async (e) =>
              {let isTaken = await isLoginTaken(e, formData.login);
              if(!isTaken) {handleNext()}
              else {setLoginError("Podany login jest już zajęty.\n\ Wybierz inny.")}}} disabled={!isValid()} > PRZEJDŹ DALEJ </Button>
            </div>
      </Form>
    );
  }
  export default RegistrationUserData