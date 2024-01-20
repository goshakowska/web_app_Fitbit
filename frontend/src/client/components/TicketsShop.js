import React, { useState, useEffect } from "react";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css"
import clientToken from '../ClientToken.js';
import getDiscountTickets from "../functions/GetDiscountTickets.js";
import getStandardTickets from "../functions/GetStandardTickets.js";
import CartToken from "../CartToken.js";

function TicketsShop()
{
  // shows ticket's shop
    const {userId} = clientToken();
    const {addTicket} = CartToken();
    const [discountTickets, setDiscountTickets] = useState([])
    const [standardTickets, setStandardTickets] = useState([])

    const getDiscountTicketsList = async (event) => {
      // get discount tickets data
            const data = await getDiscountTickets(event);
            setDiscountTickets(data.tickets)
    }

    const getStandardTicketsList = async (event) => {
      // get standard tickets data
      const data = await getStandardTickets(event);
      setStandardTickets(data.tickets)
}

  // get data on site render
    useEffect((e) => {getDiscountTicketsList(e)}, []);
    useEffect((e) => {getStandardTicketsList(e)}, []);

    const handleClick = (e, ticket, type) => {
      // handle adding tickets to cart or set error when user not logged in
        if (userId()) {
          if (type === 'disc')
            {addTicket(ticket[3], ticket[8], ticket[2], ticket[4], ticket[5], ticket[6], ticket[7], ticket[1], ticket[0]);
            alert('Dodano do koszyka.')}
          else
            {addTicket('Standardowy', ticket[3], ticket[1], null, null, ticket[2], null, null, ticket[0])
            alert('Dodano do koszyka.')}}
        else
          {window.location.href = '/login'; alert("Aby dodać do koszyka musisz się najpierw zalogować.")}
    }

    return (
        <div className="ticketsShop">
            <h className="textLogin"> Oferta karnetów </h>
        <div className="gridDesign">
      <div className="tablePos">
      <h className="textLogin2"> Karnety promocyjne {JSON.parse(localStorage.getItem('ticketsCart'))} </h>
        <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
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
                        <th scope="row">{ticket[2]}({ticket[8]})</th>
                        <td> {ticket[3]} </td>
                        <td>{ticket[4]}%</td>
                        <td> {ticket[5]}zł </td>
                        <td>{ticket[6]}zł</td>
                        {ticket[7] ? <td>{ticket[7]}</td> : <td> - </td>}
                        <td> <Button type="button" className="cartStyle" onClick={(e) =>{handleClick(e, ticket, 'disc')}}
                        >🛒</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table>
</div>

<div className="tablePos">
      <h className="textLogin2"> Karnety standardowe </h>
<Table bordered hover responsive className="tableDesign tableDesignNarrow" >
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
                        <th scope="row">{ticket[1]}({ticket[3]})</th>
                        <td> Standardowy </td>
                        <td>{ticket[2]}zł</td>
                        <td> <Button type="button" className="cartStyle" onClick={(e) =>{handleClick(e, ticket, 'std')}}
                        >🛒</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> </div>
</div> </div>
    );

}

export default TicketsShop;