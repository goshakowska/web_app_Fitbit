import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import getClassDetails from "../functions/ClassDetails";
import getCancelClass from "../functions/CancelClass";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css";


const ClassDetails = () => {
  // shows details site for already bought class
    const [details, setDetails] = useState([]);
    const [error, setError] = useState("")
    const location = useLocation();
    const navigate = useNavigate();
    const class_id = location.state.classId;

    const getDetails = async (event) => {
  // gets displayed class details
      const details = await getClassDetails(event, class_id);
      setDetails(details);
  }

    const handleCancel = async (event, class_id) => {
      // cancels already bought class or displays error if too late to cancel
          const data = await getCancelClass(event, class_id)
          console.log(data)
          if(data.error){setError(data.error)}
          else if(data.result){navigate('/kalendarz_klienta')}
      }

      // get data on site render
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
<Button className="deleteStyle" onClick={e => handleCancel(e, class_id)} disabled={error}> Anuluj zajęcia </Button>
<label className="errorLabel">{error}</label></div>
</div>
</div>
  );

}

export default ClassDetails;