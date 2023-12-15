import React, { useContext } from 'react';
import {
  Input,
  InputGroup,
  Button,
  Row,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationUserData() {
    const {formData, handleChange, handleNext} = useContext(FormContext)

    return(
      <form className="registrationForm">
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' label="Imię" placeholder="login*" name="login" value={formData.login} onChange={handleChange} required/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="e-mail*" name="email" value={formData.email} onChange={handleChange} required/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="hasło*" type= 'password' name="password" value={formData.password} onChange={handleChange} required/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="powtórz hasło*" type= 'password'/>
          </InputGroup>
          <div>
            <Button className="buttonStyleSwitchPage text-style" type="button" onClick={handleNext}> PRZEJDŹ DALEJ </Button>
            </div>
      </form>
    );
  }
  export default RegistrationUserData