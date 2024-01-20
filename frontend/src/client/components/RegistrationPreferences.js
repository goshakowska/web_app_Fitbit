import React, { useEffect, useState, useContext } from 'react';
import {
  Input,
  InputGroup,
  Button,
  Row,
} from 'reactstrap';
import FormContext from '../context/RegistrationContext';


function RegistrationPreferences() {
  // 3rd page of registration form: user preferences
    const {formData, handleChange, handlePrev} = useContext(FormContext)
    const [goals, setGoals] = useState([])

    const getGoals = async (event) => {
      // get goals from database
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
      // submit form & finish registration
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

      // get on site render
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
              <Input className='centeredTextInputSmall' type="number" min='100' placeholder="wzrost (cm)" name="height" value={formData.height} onChange={handleChange}/>
          </InputGroup></Row>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type="select" name="training_frequency" value={formData.training_frequency} onChange={handleChange}>
              <option value={null}> planowana liczba treningów w tygodniu </option>
              <option value="1"> 1 </option>
              <option value="2"> 2 </option>
              <option value="3"> 3 </option>
              <option value="4"> 4 </option>
              <option value="5"> 5 </option>
              <option value="6"> 6 </option>
              <option value="7"> 7 </option> </Input>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type="select" name="training_time" value={formData.training_time} onChange={handleChange}>
              <option value={null}> szacowany czas treningu </option>
              <option value="20"> 20 minut </option>
              <option value="30"> 30 minut </option>
              <option value="45"> 45 minut </option>
              <option value="60"> 60 minut </option>
              <option value="75"> 75 minut </option>
              <option value="90"> 90 minut </option>
              <option value="120"> 120 minut </option> </Input>
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
          <Button className="buttonStyleLoginUser text-style" type="submit" onClick={handleSubmit}> ZAREJESTRUJ SIĘ </Button>
            </Row>

      </form>
    );
  }
  export default RegistrationPreferences