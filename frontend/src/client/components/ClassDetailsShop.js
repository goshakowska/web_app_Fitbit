import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Button, Table} from 'reactstrap';
import getClassDetails from "../functions/ClassDetails";
import getCalendarClassDetails from "../functions/CalendarClassDetails";
import checkCartCollision from "../functions/CartCollisionCheck.js";
import "../styles/tablesStyle.css";
import CartToken from "../CartToken.js";


export default function ClassDetailsShop() {
    const [details, setDetails] = useState([])
    const [collisionDetails, setCollisionDetails] = useState([])
    const [cartCollisionId, setCartCollisionId] = useState(null)
    const location = useLocation();
    const classId = location.state.classId;
    const date = location.state.date;
    const collisionId = location.state.collisionId;
    const freePlaces = location.state.freePlaces;
    const {addTraining, getCart} = CartToken();

    const getCollisionDetails = async (event, collisionId) => {
        const details = await getClassDetails(event, collisionId);
        setCollisionDetails(details);
    }

    const getDetails = async (event, classId, date) => {
        const details = await getCalendarClassDetails(event, classId, date);
        setDetails(details);
    }

    const checkCollision = async (event, classId, date, cart) => {
        const id = await checkCartCollision(event, classId, date, cart);
        console.log(id)
        setCartCollisionId(id);
    }

    useEffect((e) => {getDetails(e, classId, date)}, [])
    useEffect((e) => {checkCollision(e, classId, date, getCart()[1])}, [])
    useEffect((e) => {if (collisionId) getCollisionDetails(e, collisionId)}, []);
    useEffect((e) => {if (cartCollisionId) getCollisionDetails(e, cartCollisionId)}, []);

    return(
        <div className="layout">
            <div>
      <div className="textLogin"> Szczegóły terminu zajęciowego</div>

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
    <th>
      Liczba wolnych miejsc
    </th>
  </tr>
</thead>
<tbody>
    {details.length > 0 && <tr>
        <td>{details[0]}</td>
        <td> {details[1]} {details[2]} </td>
        <td>{details[3]}, {details[4]} {details[5]}</td>
        <td>{details[6]}, {details[7]}, {details[8]}</td>
        <td>{freePlaces}</td>
    </tr> }

</tbody>
</Table>
</div>
</div>
            {(collisionId || cartCollisionId) ?
      <div>
      <div className="tablePos">
        <label className="errorLabel"> Uwaga! Masz kolizję z poniższym terminem: </label>
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
{collisionId && <label className="errorLabel"> Aby dodać ten termin do koszyka, anuluj swój udział w powyższych zajęciach. </label>}
{cartCollisionId && <label className="errorLabel"> Aby dodać ten termin do koszyka, usuń kolidujący z nim termin z koszyka. </label>}
</div>
</div> : <Button type="button" className="cartStyle text-style" onClick={(e) =>{addTraining(details[0], 100, details[7], details[6], classId, freePlaces)}}
                        >Dodaj zajęcia do koszyka</Button>}</div>
  );

}