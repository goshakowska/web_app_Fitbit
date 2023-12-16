import React, { useState, useEffect } from "react";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css"
import clientToken from '../ClientToken.js';

function Tickets()
{
    const {userId} = clientToken();
    const [discountTickets, setDiscountTickets] = useState([])
    const [standardTickets, setStandardTickets] = useState([])

    const getDiscountTickets = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/discount_gym_ticket_offer/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              }});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setDiscountTickets(data.tickets)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    const getStandardTickets = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/standard_gym_ticket_offer/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              }});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setStandardTickets(data.tickets)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect(() => {getDiscountTickets()}, []);

    useEffect(() => {getStandardTickets()}, []);

    const handleClick = () => {
        if (userId()) {
         window.location.href = '/silownie'} else
        {window.location.href = '/login'; alert("Aby dodać do koszyka musisz się najpierw zalogować.")}
    }

    return (
        <div className="ticketsShop">
            <h className="textLogin"> Oferta karnetów </h>
        <div className="gridDesign">
      <div className="tablePos">
      <h className="textLogin"> Karnety promocyjne </h>
        <Table bordered hover responsive className="tableDesign" >
  <thead>
    <tr>
      <th>
        Typ
      </th>
      <th>
        Nazwa
      </th>
      <th>
        Zniżka
      </th>
      <th>
        Cena przed zniżką
      </th>
      <th>
        Cena końcowa
      </th>
      <th>
        Termin końca promocji
      </th>
      <th>
        Dodaj do koszyka
      </th>
    </tr>
  </thead>
  <tbody>
  {discountTickets.length > 0 && discountTickets.map((ticket, index) => (
                    <tr key={index}>
                        <th scope="row">{ticket[2]}</th>
                        <td> {ticket[3]} </td>
                        <td>{ticket[4]}%</td>
                        <td> {ticket[5]}zł </td>
                        <td>{ticket[6]}zł</td>
                        {ticket[7] ? <td>{ticket[7]}</td> : <td> - </td>}
                        <td> <Button type="button" className="cartStyle" onClick={handleClick}
                        >🛒</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table>
</div>

<div className="tablePos">
      <h className="textLogin"> Karnety standardowe </h>
<Table bordered hover responsive className="tableDesign" >
  <thead>
    <tr>
      <th>
        Typ
      </th>
      <th>
        Nazwa
      </th>
      <th>
        Cena
      </th>
      <th>
        Dodaj do koszyka
      </th>
    </tr>
  </thead>
  <tbody>
  {discountTickets.length > 0 && standardTickets.map((ticket, index) => (
                    <tr key={index}>
                        <th scope="row">{ticket[1]}</th>
                        <td> Standardowy </td>
                        <td>{ticket[2]}zł</td>
                        <td> <Button type="button" className="cartStyle" onClick={handleClick}
                        >🛒</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> </div>
</div> </div>
    );

}

export default Tickets;