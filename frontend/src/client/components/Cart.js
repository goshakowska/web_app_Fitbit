import CartToken from "../CartToken";
import React, { useState, useEffect, useContext } from "react";
import {Button, Table} from 'reactstrap';

function Cart () {
    const {getCart, deleteTicket, deleteTraining} = CartToken();
    const [st, stst] = useState(true)

    console.log(getCart()[0])
    return (
        <div className="ticketsShop">
            <h className="textLogin"> Twój koszyk </h>
        <div className="gridDesign">
      <div className="tablePos">
      <h className="textLogin2"> Karnety </h>
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
        Usuń z koszyka
      </th>
    </tr>
  </thead>
  <tbody>
  {getCart()[0].length > 0 && getCart()[0].map((ticket, index) => (
                    <tr key={index}>
                        <th scope="row">{ticket["type"]}({ticket["durability"]})</th>
                        <td> {ticket["name"]} </td>
                        {ticket["discount"] ? <td>{ticket["discount"]}%</td> : <td> - </td>}
                        {ticket["beforeDiscountPrice"] ? <td> {ticket["beforeDiscountPrice"]}zł </td> : <td> - </td>}
                        <td>{ticket['price']}zł</td>
                        {ticket["endOfDiscount"] ? <td>{ticket["endOfDiscount"]}</td> : <td> - </td>}
                        <td> <Button type="button" className="deleteStyle" onClick={(e) =>{deleteTicket(index); stst(!st)}}
                        >Usuń z koszyka</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table>
</div>
<div className="tablePos">
<h className="textLogin2"> Zajęcia </h>
        <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
  <thead>
    <tr>
      <th>
        Nazwa
      </th>
      <th>
        Cena
      </th>
      <th>
        Termin
      </th>
      <th>
        Szczegóły
      </th>
      <th>
        Usuń z koszyka
      </th>
    </tr>
  </thead>
  <tbody>
  {getCart()[1].length > 0 && getCart()[1].map((ticket, index) => (
                    <tr key={index}>
                        <th scope="row">{ticket["name"]}</th>
                        <td> {ticket["price"]} </td>
                        <td>{ticket['scheduleDate']}, {ticket['hour']} </td>
                        <td> <Button type="button" className="deleteStyle" onClick={(e) =>{deleteTicket(index); stst(!st)}}
                        >Usuń z koszyka</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table>
</div></div></div>
)

}

export default Cart