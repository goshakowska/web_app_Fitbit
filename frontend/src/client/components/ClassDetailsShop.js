import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Button, Table} from 'reactstrap';
import getClassDetails from "../functions/ClassDetails";
import "../styles/tablesStyle.css";

export default function ClassDetailsShop() {
    const [collisionDetails, setCollisionDetails] = useState([])
    const location = useLocation();
    const classId = 1// location.state.classId;
    const date = '2024-01-13' //location.state.date;
    const collisionId = null// location.state.collisionId;

    const getCollisionDetails = async (event, collisionId) => {
        const details = await getClassDetails(event, collisionId);
        setCollisionDetails(details);
    }

    useEffect((e) => {if (collisionId) getCollisionDetails(e, collisionId)}, []);

    return(
        <div>
            {collisionId &&
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
        <td>{collisionDetails[0]}</td>
        <td> {collisionDetails[1]} {collisionDetails[2]} </td>
        <td>{collisionDetails[3]}, {collisionDetails[4]} {collisionDetails[5]}</td>
        <td>{collisionDetails[6]}, {collisionDetails[7]}, {collisionDetails[8]}</td>
    </tr>

</tbody>
</Table>
</div>
</div>}</div>
  );

}