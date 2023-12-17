import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css";
import secondsToHHMMSS from "../functions/secondsToHHMMSS";
import moment from 'moment';


const ClientTicketDetails = props => {
    const [details, setDetails] = useState([])
    const location = useLocation();
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
<div> {details["days_to_end"] ?
        <div className="activeTicket text-style"> <p>Karnet aktywny.</p>
        <p>Zostało: {details["days_to_end"]} dni.</p> </div> : <></>} </div>
</div>
  );

}

export default ClientTicketDetails;