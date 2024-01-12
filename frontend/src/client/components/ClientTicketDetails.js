import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import {Table, Button} from 'reactstrap';
import "../styles/tablesStyle.css";



const ClientTicketDetails = props => {
    const [details, setDetails] = useState([])
    const location = useLocation();
    const navigate = useNavigate();
    const ticket_id = location.state.ticketId;

    const getTicketDetails = async (event, ticket_id) => {
        try {
            const response = await fetch('http://localhost:8000/client/gym_tickets_details/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ ticket_id: ticket_id})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.details)
            setDetails(data.details);

          } catch (error) {
            console.error('Error:', error);
          };
    }

    const deleteTicket = async (event, ticket_id) => {
      try {
          const response = await fetch('http://localhost:8000/client/delete_gym_ticket/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },body: JSON.stringify({ gym_ticket_id: ticket_id})});
            navigate('/karnety_klienta')
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

        } catch (error) {
          console.error('Error:', error);
        };
  }

    useEffect((e) => {getTicketDetails(e, ticket_id)}, []);

    return(
      <div className="clubsTable">
      <h className="textLogin"> Szczegóły Twojego karnetu</h>

      <div className="tablePos">
<Table bordered hover responsive className="tableDesign tableDesignWide" >
<thead>
  <tr>
    <th>
      Typ
    </th>
    <th>
      Zniżka
    </th>
    <th>
      Cena bez zniżki
    </th>
    <th>
      Cena końcowa
    </th>
    <th>
      Ważny od
    </th>
    <th>
      Ważny do
    </th>
  </tr>
</thead>
<tbody>

<tr>
    <td>{details["type"]} ({details["duration"]})</td>
    {details["discount"] ? <td>{details["discount"]}% </td> : <td>-</td>}
    <td>{details["price_before"]} zł</td>
    {details["price_after"] ? <td> {details["price_after"]} zł </td> : <td> - </td> }
    {details["activation_date"] ? <td>{details["activation_date"]}</td> : <td> - </td>}
    {details["end_date"] ? <td>{details["end_date"]}</td> : <td> - </td>}
</tr>
</tbody>
</Table>
</div>
<div> {details["visits_to_end"] ?
        <div className="activeTicket text-style">Karnet aktywny. Zostało wejść: {details["visits_to_end"]}. </div> : <></>} </div>

<div> {details["days_to_end"] ?
        <div className="activeTicket text-style">Karnet aktywny. Zostało: {details["days_to_end"]} dni. </div> : <></>} </div>
<div> {details["status"]=== null ?
        <div className="inactiveTicket text-style">Karnet nie został aktywowany </div> : <></>} </div>
<div> {details["status"] === false ?
        <div className="expiredTicket text-style">Karnet wygasł. </div> : <></>}
<div>
{details["status"]=== null ?
        <Button className="deleteStyle text-style" onClick={(e) => {deleteTicket(e, ticket_id)}}> Anuluj zakup karnetu </Button> : <></>}
        </div> </div>
</div>
  );

}

export default ClientTicketDetails;