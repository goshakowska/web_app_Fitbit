import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import getTicketDetails from "../functions/ticketDetails";
import deleteTicket from "../functions/DeleteTicket";
import {Table, Button} from 'reactstrap';
import "../styles/tablesStyle.css";



const ClientTicketDetails = props => {
  // shows details about client's ordered ticket
    const [details, setDetails] = useState([])
    const location = useLocation();
    const navigate = useNavigate();
    const ticket_id = location.state.ticketId;


    const ticketDetails = async (event) => {
      // shows ticket's details
          const data = await getTicketDetails(event, ticket_id)
          console.log(data)
          setDetails(data.details)
      }

      const handleDeleteTicket = async (event, ticket_id) => {
  // deletes unactivated client's ticket
        deleteTicket(event, ticket_id);
        navigate('/karnety_klienta');
      }

      // get data on site render
    useEffect((e) => {ticketDetails(e, ticket_id)}, []);

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
        <Button className="deleteStyle text-style" onClick={(e) => {handleDeleteTicket(e, ticket_id)}}> Anuluj zakup karnetu </Button> : <></>}
        </div> </div>
</div>
  );

}

export default ClientTicketDetails;