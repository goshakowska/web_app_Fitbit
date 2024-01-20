import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Table} from 'reactstrap';
import "../styles/tablesStyle.css";
import getTrainingDetailsList from "../functions/GetTrainingDetails";
import secondsToHHMMSS from "../functions/secondsToHHMMSS";


const TrainingDetails = props => {
  // show client's training details
    const [details, setDetails] = useState([])
    const location = useLocation();
    const training_id = location.state.detailId;
    const training_date = location.state.detailDate

    const getTrainingDetails = async (event) => {
      // get details
            const data = await getTrainingDetailsList(event, training_id);
            setDetails(data.details);
    }

    // get data on site render
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