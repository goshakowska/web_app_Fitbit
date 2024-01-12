import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Table} from 'reactstrap';
import "../styles/tablesStyle.css";
import secondsToHHMMSS from "../functions/secondsToHHMMSS";
import moment from 'moment';


const TrainingDetails = props => {
    const [details, setDetails] = useState([])
    const location = useLocation();
    const training_id = location.state.detailId;
    const training_date = location.state.detailDate

    const getTrainingDetails = async (event, training_id) => {
        try {
            const response = await fetch('http://localhost:8000/client/trening_details/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ training_id: training_id})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setDetails(data.details);

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect((e) => {getTrainingDetails(e, training_id)}, []);

    return(
      <div className="clubsTable">
      <h className="textLogin"> Twoje dane z treningu z dnia {training_date}</h>

      <div className="tablePos">
<Table bordered hover responsive className="tableDesign tableDesignWide" >
<thead>
  <tr>
    <th>
      Nazwa ćwiczenia
    </th>
    <th>
      Godzina startu
    </th>
    <th>
      Czas trwania
    </th>
    <th>
      Liczba powtórzeń
    </th>
    <th>
      Spalone kalorie
    </th>
    <th>
      Dodatkowe informacje
    </th>
  </tr>
</thead>
<tbody>
{details.length > 0 && details.map((details, index) => (
                  <tr key={index}>
                      <td>{details["name"]}</td>
                      <td> {details["start_hour"]} </td>
                      <td>{secondsToHHMMSS(details["duration"])}</td>
                      {details["repetitions_number"] === 0 ? <td> - </td> : <td> {details["repetitions_number"]}</td> }
                      <td>{details["calories"]} kcal</td>
                      {details["parameters"] ? details["parameters"].map((parameters, index) => (
                          <td key={index}>{parameters["name"]}: {parameters["value"]} {parameters["unit"]} </td>
                      )) : <td>-</td>}
                  </tr>
              ))}
</tbody>
</Table> </div>
</div>
  );

}

export default TrainingDetails;