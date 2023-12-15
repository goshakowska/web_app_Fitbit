import React, { useEffect, useState, useContext } from 'react';
import {
  Input,
  InputGroup,
  Button,
  Row,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationPreferences() {
    const {formData, handleChange, handlePrev} = useContext(FormContext)
    const [goals, setGoals] = useState([])

    const getGoals = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/training_goals/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              }});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setGoals(data.goals)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          const response = await fetch('http://localhost:8000/client/registration/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login: formData.login,
                                    password_hash: formData.password,
                                    email: formData.email,
                                    phone_number: formData.phone,
                                    name: formData.name,
                                    surname: formData.surname,
                                    gender: formData.sex,
                                    height: formData.height,
                                    birth_year: formData.dateOfBirth,
                                    advancement: formData.advancement,
                                    current_weight: formData.current_weight,
                                    target_weight: formData.target_weight,
                                    training_frequency: formData.training_frequency,
                                    training_time: formData.training_time,
                                    training_goal_id: formData.training_goal_id,
                                    gym_id: null }),
          });

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          alert('Zostałeś pomyślnie zarejestrowany.');
          window.location.href = '/login'
        } catch (error) {
          console.error('Error:', error);
        }
      };

      useEffect(() => {getGoals()}, []);

    return(
      <form className="registrationForm">
          <Row>
          <InputGroup className="inputGroupSmall">
              <Input className='centeredTextInputSmall' type="number" placeholder="waga aktualna (kg)" name="current_weight" value={formData.current_weight} onChange={handleChange}/>
          </InputGroup>
          <InputGroup className="inputGroupSmall">
              <Input className='centeredTextInputSmall' type="number" placeholder="waga docelowa (kg)" name="target_weight" value={formData.target_weight} onChange={handleChange}/>
          </InputGroup>
          <InputGroup className="inputGroupSmall">
              <Input className='centeredTextInputSmall' type="number" placeholder="wzrost (cm)" name="height" value={formData.height} onChange={handleChange}/>
          </InputGroup></Row>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type="number" placeholder="planowana liczba treningów w tygodniu" name="training_frequency" value={formData.training_frequency} onChange={handleChange}/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type="number" placeholder="szacowany czas treningu (w min.)" name="training_time" value={formData.training_time} onChange={handleChange}/>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="advancement" value={formData.advancement} onChange={handleChange}>
              <option value={null}> Wybierz swój poziom zaawansowania </option>
              <option value="zaawansowany"> Początkujący </option>
              <option value="średniozaawansowany"> Średniozaawansowany </option>
              <option value="początkujący"> Zaawansowany </option> </Input>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="training_goal_id" value={formData.training_goal_id} onChange={handleChange}>
                    <option value={null} > Wybierz cel, który chcesz osiągnąć</option>
                    {goals.map((option, index) => (
                    <option key={index} value={option[0]}>
                    {option[1]}
                    </option>
                ))} </Input>
          </InputGroup>
          <Row>
          <Button className="buttonStyleSwitchPage text-style" type="button" onClick={handlePrev}> COFNIJ </Button>
          <Button className="buttonStyleSwitchPage text-style" type="submit" onClick={handleSubmit}> ZAREJESTRUJ SIĘ </Button>
            </Row>

      </form>
    );
  }
  export default RegistrationPreferences