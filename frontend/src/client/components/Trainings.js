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
      navigate('/szczegoly', {
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
<Table bordered hover responsive className="tableDesign" >
  <thead>
    <tr>
      <th>
        Start
      </th>
      <th>
        Koniec
      </th>
      <th>
        Czas trwania
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
  {trainings.length > 0 && trainings.map((training, index) => (
                    <tr key={index}>
                        <td>{moment(training[1]).format('DD.MM.YYYY, hh:mm:ss')}</td>
                        <td> {moment(training[2]).format('DD.MM.YYYY, hh:mm:ss')} </td>
                        <td>{secondsToHHMMSS(training[3])}</td>
                        <td>{training[4]} kcal</td>
                        <td> <Button type="button" className="cartStyle text-style" onClick={ (e) => {handleClick(training[0], moment(training[2]).format('DD.MM.YYYY'))}}
                        >Szczegóły </Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> </div>
</div>
    );

}

export default Trainings;