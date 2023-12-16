import React, { useContext } from 'react';
import {
  Input,
  InputGroup,
  Button,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationPersonalInfo() {
    const {formData, handleChange, handleNext, handlePrev, setFormData} = useContext(FormContext)

    const keysToCheck1 = ['nameState', 'surnameState', 'phoneState']
    const keysToCheck2 = ['sex', 'dateOfBirth']

    const isValid = () => {
      if(keysToCheck1.every(key => formData.validate[key] === "has-success") &&
      keysToCheck2.every(key => formData[key] !== "" && formData[key] !== null)) return true;
      return false;
    }

    const validateName = (e) => {
      const { validate, ...userData} = formData;
      const regex = /^[A-ZŁŚŻ][a-ząćęłńóśźż]+$/;
      if (!(regex.test(e.target.value))) {
        validate.nameState = 'has-danger';
      } else {
        validate.nameState = 'has-success';
      }
      setFormData({validate, ...userData})
    }

    const validateSurname = (e) => {
      const { validate, ...userData} = formData;
      const regex = /^[A-ZŁŚŻ][a-ząćęłńóśźż]+([-][A-ZŁŚŻ][a-ząćęłńóśźż]+)?$/;
      if (!(regex.test(e.target.value))) {
        validate.surnameState = 'has-danger';
      } else {
        validate.surnameState = 'has-success';
      }
      setFormData({validate, ...userData})
    }

    const validatePhone = (e) => {
      const { validate, ...userData} = formData;
      const regex = /^(\d{3}-\d{3}-\d{3}|\d{9})$/;
      if (!(regex.test(e.target.value))) {
        validate.phoneState = 'has-danger';
      } else {
        validate.phoneState = 'has-success';
      }
      setFormData({validate, ...userData})
    }

    return(
      <form className="registrationForm">
      <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type='text' placeholder="imię*" name="name" value={formData.name}
                                          valid={formData.validate.nameState === 'has-success'}
                                          invalid={formData.validate.nameState === 'has-danger'}
                                          onChange={(e) => {
                                            validateName(e);
                                            handleChange(e);}} />
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type='text' placeholder="nazwisko*" name="surname" value={formData.surname}
                                          valid={formData.validate.surnameState === 'has-success'}
                                          invalid={formData.validate.surnameState === 'has-danger'}
                                          onChange={(e) => {
                                            validateSurname(e);
                                            handleChange(e);}}/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= 'number' placeholder="numer telefonu" name="phone" value={formData.phone}
                                          valid={formData.validate.phoneState === 'has-success'}
                                          invalid={formData.validate.phoneState === 'has-danger'}
                                          onChange={(e) => {
                                            validatePhone(e);
                                            handleChange(e);}} />
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
            <Button className="buttonStyleSwitchPage text-style" type="button" onClick={handleNext} disabled={!isValid()}> PRZEJDŹ DALEJ </Button>
            </div>
      </form>
    );
  }
  export default RegistrationPersonalInfo