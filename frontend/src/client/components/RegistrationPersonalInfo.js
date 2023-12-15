import React, { useContext } from 'react';
import {
  Input,
  InputGroup,
  Button,
  Row,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationPersonalInfo() {
    const {formData, handleChange, handleNext, handlePrev} = useContext(FormContext)

    return(
      <form className="registrationForm">
      <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="imię*" name="name" value={formData.name} onChange={handleChange} required/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="nazwisko*" name="surname" value={formData.surname} onChange={handleChange} required/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' placeholder="numer telefonu" name="phone" value={formData.phone} onChange={handleChange}/>
          </InputGroup>
          <label className='labelsStyle'>Data urodzenia*</label>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type="date" placeholder="data urodzenia*" name="dateOfBirth" value={formData.dateOfBirth} onChange={handleChange}/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="sex" value={formData.sex} onChange={handleChange}>
              <option value={null}> Wybierz płeć* </option>
              <option value="K"> Kobieta </option>
              <option value="M"> Mężczyzna </option> </Input>
          </InputGroup>
          <div>
            <Button className="buttonStyleSwitchPage text-style" type="button" onClick={handlePrev}> COFNIJ </Button>
            <Button className="buttonStyleSwitchPage text-style" type="button" onClick={handleNext}> PRZEJDŹ DALEJ </Button>
            </div>
      </form>
    );
  }
  export default RegistrationPersonalInfo