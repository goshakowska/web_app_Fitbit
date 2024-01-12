import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Table} from 'reactstrap';
import "../styles/tablesStyle.css";
import secondsToHHMMSS from "../functions/secondsToHHMMSS";
import moment from 'moment';


const ClassDetails = props => {
    const [details, setDetails] = useState([])
    const location = useLocation();
    const class_id = location.state.classId;

    const getClassDetails = async (event, class_id) => {
        try {
            const response = await fetch('http://localhost:8000/client/ordered_classe_details/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ classe_id: class_id})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.details[0])
            setDetails(data.details);

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect((e) => {getClassDetails(e, class_id)}, []);

    return(
      <div className="clubsTable">
      <h className="textLogin"> Szczegóły Twoich zajęć</h>

      <div className="tablePos">
<Table bordered hover responsive className="tableDesign tableDesignWide" >
<thead>
  <tr>
    <th>
      Nazwa
    </th>
    <th>
      Prowadzący
    </th>
    <th>
      Adres
    </th>
    <th>
      Termin
    </th>
  </tr>
</thead>
<tbody>
    <tr>
        <td>{details[0]}</td>
        <td> {details[1]} {details[2]} </td>
        <td>{details[3]}, {details[4]} {details[5]}</td>
        <td>{details[6]}, {details[7]}, {details[8]}</td>
    </tr>

</tbody>
</Table> </div>
</div>
  );

}

export default ClassDetails;