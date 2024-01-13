import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import getClassDetails from "../functions/ClassDetails";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css";



const ClassDetails = props => {
    const [details, setDetails] = useState([]);
    const [error, setError] = useState("")
    const location = useLocation();
    const navigate = useNavigate();
    const class_id = location.state.classId;

    const getDetails = async (event) => {
      const details = await getClassDetails(event, class_id);
      setDetails(details);
  }

    const cancelClass = async (event, class_id) => {
      try {
          const response = await fetch('http://localhost:8000/client/cancel_ordered_gym_classe/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },body: JSON.stringify({ ordered_gym_classe_id: class_id})});

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          if(data.error){setError(data.error)}
          if(data.result){navigate('/kalendarz_klienta')}

        } catch (error) {
          console.error('Error:', error);
        };
  }

    useEffect((e) => {getDetails(e, class_id)}, []);

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
</Table>
<div className="layout">
<Button className="deleteStyle" onClick={e => cancelClass(e, class_id)} disabled={error}> Anuluj zajęcia </Button>
<label className="errorLabel">{error}</label></div>
</div>
</div>
  );

}

export default ClassDetails;