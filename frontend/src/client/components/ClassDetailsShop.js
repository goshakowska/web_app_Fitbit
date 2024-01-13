import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Button, Table} from 'reactstrap';
import getClassDetails from "../functions/ClassDetails";
import getCalendarClassDetails from "../functions/CalendarClassDetails";
import "../styles/tablesStyle.css";

export default function ClassDetailsShop() {
    const [details, setDetails] = useState([])
    const [collisionDetails, setCollisionDetails] = useState([])
    const location = useLocation();
    const classId = location.state.classId;
    const date = location.state.date;
    const collisionId = location.state.collisionId;

    const getCollisionDetails = async (event, collisionId) => {
        const details = await getClassDetails(event, collisionId);
        setCollisionDetails(details);
    }

    const getDetails = async (event, classId, date) => {
        const details = await getCalendarClassDetails(event, classId, date);
        setDetails(details);
    }

    useEffect((e) => {getDetails(e, classId, date)}, [])
    useEffect((e) => {if (collisionId) getCollisionDetails(e, collisionId)}, []);

    return(
        <div>
            <div>
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
    {details.length > 0 && <tr>
        <td>{details[0]}</td>
        <td> {details[1]} {details[2]} </td>
        <td>{details[3]}, {details[4]} {details[5]}</td>
        <td>{details[6]}, {details[7]}, {details[8]}</td>
    </tr> }

</tbody>
</Table>
</div>
</div>
            {collisionId &&
      <div>
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