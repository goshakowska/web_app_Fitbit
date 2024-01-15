import React, { useState, useEffect} from "react";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css"
import clientToken from '../ClientToken.js';
import { useNavigate } from "react-router-dom";
import moment from 'moment';
import secondsToHHMMSS from "../functions/secondsToHHMMSS.js";


function Trainings()
{
    const {userId} = clientToken();
    const [trainings, setTrainings] = useState([]);
    let navigate = useNavigate();


    const getTrainings = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/client_trenings/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ client_id: userId()})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.trenings);
            setTrainings(data.trenings)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect(() => {getTrainings()}, []);

    const handleClick = (training_id, date) => {
      navigate('/szczegoly_treningu', {
        state: {
          detailId: training_id,
          detailDate: date,
        }
      });
    };

    return (
        <div className="clubsTable">
        <h className="textLogin"> Twoje dane z treningów </h>

        <div className="tablePos">
        {trainings.length > 0 ? <div>
<Table bordered hover responsive className="tableDesignWide tableDesign" >
  <thead>
    <tr>
      <th>
        Godzina wejścia na siłownię
      </th>
      <th>
        Godzina wyjścia z siłowni
      </th>
      <th>
        Czas trwania treningu
      </th>
      <th>
        Spalone kalorie
      </th>
      <th>
        Zobacz szczegóły
      </th>
    </tr>
  </thead>
  <tbody>
{ trainings.map((training, index) => (
                    <tr key={index}>
                        <td>{training[1]} {training[2]}</td>
                        <td> {training[3]} {training[4]} </td>
                        <td>{secondsToHHMMSS(training[5])}</td>
                        <td>{training[6]} kcal</td>
                        <td> <Button type="button" className="cartStyle text-style" onClick={ (e) => {handleClick(training[0], training[1])}}
                        >Szczegóły </Button> </td>
                    </tr>
                ))}
  </tbody>
</Table></div> : <label className="errorLabel">Nie odbyłeś jeszcze żadnych treningów.</label>} </div>
</div>
    );

}

export default Trainings;