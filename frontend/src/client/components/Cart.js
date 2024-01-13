import CartToken from "../CartToken";
import React, { useState, useEffect, useContext } from "react";
import {Button, Table} from 'reactstrap';
import { useNavigate } from "react-router-dom";


function Cart () {
    const {getCart, deleteTicket, deleteTraining} = CartToken();
    const [st, stst] = useState(true);
    const navigate = useNavigate();

    const handleClick = (class_id, date, collision_id) => {
      navigate('/szczegoly_sklep', {
        state: {
          classId: class_id,
          date: date,
          collisionId: null
        }
      });
    };

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
  {getCart()[1].length > 0 && getCart()[1].map((training, index) => (
                    <tr key={index}>
                        <th scope="row">{training["name"]}</th>
                        <td> {training["price"]} </td>
                        <td>{training['scheduleDate']}, {training['hour']} </td>
                        <td> <Button type="button" className="cartStyle" onClick={(e) => {handleClick(training["weekScheduleId"], training["scheduleDate"])}}
                        >Szczegóły</Button> </td>
                        <td> <Button type="button" className="deleteStyle" onClick={(e) =>{deleteTraining(index); stst(!st)}}
                        >Usuń z koszyka</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table>
</div></div></div>
)

}

export default Cart