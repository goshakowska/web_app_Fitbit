import CartToken from "../CartToken";
import React, { useState, useEffect } from "react";
import {Button, Table} from 'reactstrap';
import { useNavigate } from "react-router-dom";
import bookCart from "../functions/CartReservation";
import clientToken from "../ClientToken";
import getCalendarClassDetails from "../functions/CalendarClassDetails";


function Cart () {
  // shows client's cart main view
    const {userId} = clientToken();
    const {getCart, deleteTicket, deleteTraining} = CartToken();
    const [st, stst] = useState(true);
    const navigate = useNavigate();
    const [freePlaces, setFreePlaces] = useState([]);

    const calculateTotal = () => {
  // calculates cost of all items added to cart
    const ticketsTotal = getCart()[0].reduce((sum, {price}) => sum + price, 0);
    const trainingsTotal = getCart()[1].reduce((sum, {price}) => sum + price, 0);
    const total = trainingsTotal + ticketsTotal;
    return total};

    const getDetails = async (event) => {
  // updates number of free places for very class in cart from database
      for(let i=0; i<getCart()[1].length; i++) {
      const details = await getCalendarClassDetails(event, getCart()[1][i]["week_schedule_id"], getCart()[1][i]["schedule_date"]);
      console.log(details)
      setFreePlaces(prevList => [...prevList, details[9]])};
  }


    const handleClick = (class_id, date, collision_id, free_places, price) => {
  // redirect to class details site
      navigate('/szczegoly_sklep', {
        state: {
          classId: class_id,
          date: date,
          collisionId: collision_id,
          freePlaces: free_places,
          price: price
        }
      });
    };

    const handleReservation = async (event, clientId, cartClasses) => {
  // submit cart, add everything to reservation
      const response = await bookCart(event, clientId, cartClasses);
      if (response["reserved_id"]) {
        navigate('/platnosc', {
          state: {
            reservationList: response["reserved_id"]
          }
        })
      }
      else if (response["error"]) {alert('Usuń z koszyka zajęcia, na których nie ma już miejsc.')}

    };
    // render class details on every site render
    useEffect((e) => {getDetails(e)}, [])

    return (
      <div>
        <div className="ticketsShop">
            <h className="textLogin"> Twój koszyk </h>
        <div className="gridDesign">
      <div className="tablePos">
      <h className="textLogin2"> Karnety </h>
      {getCart()[0].length > 0 ?
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
  {getCart()[0].map((ticket, index) => (
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
</Table> : <label className="errorLabel">Nie dodałeś do koszyka żadnych karnetów.</label>}
</div>

<div className="tablePos">
<h className="textLogin2"> Zajęcia </h>
{getCart()[1].length > 0 ?
        <Table bordered responsive className="tableDesign tableDesignNarrow" >
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
        Liczba wolnych miejsc
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
  {getCart()[1].map((training, index) => (
                    <tr key={index} className={freePlaces[index] === 0 && 'table-danger'}>
                        <th scope="row">{training["name"]}</th>
                        <td> {training["price"]} zł</td>
                        <td>{training['schedule_date']}, {training['hour']} </td>
                        {freePlaces[index] !== 0 ? <td> {freePlaces[index]} </td>  : <td>Brak miejsc</td>}
                        <td> <Button type="button" className="cartStyle text-style" onClick={(e) => {handleClick(training["week_schedule_id"], training["schedule_date"], null, freePlaces[index], training["price"])}}
                        >Szczegóły</Button> </td>
                        <td> <Button type="button" className="deleteStyle" onClick={(e) =>{deleteTraining(index); stst(!st)}}
                        >Usuń z koszyka</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> : <label className="errorLabel"> Nie dodałeś do koszyka żadnych zajęć.</label>}
<div className="text-style sumStyle layout marginBottom">Suma: {calculateTotal()} zł</div>
<Button type="button" className="cartStyle text-style" disabled={calculateTotal() === 0} onClick={(e) =>{handleReservation(e, userId(), getCart()[1])}}
                        >Kupuję</Button></div>
</div></div></div>

)

}

export default Cart