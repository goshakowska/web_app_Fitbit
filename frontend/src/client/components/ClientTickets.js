import React, { useState, useEffect} from "react";
import {Button, Table} from 'reactstrap';
import getClientTickets from "../functions/AllClientTickets.js";
import "../styles/tablesStyle.css"
import clientToken from '../ClientToken.js';
import { useNavigate } from "react-router-dom";



function ClientTickets()
{
  // shows all client's tickets in a table
    const {userId} = clientToken();
    const [clientTicketsData, setClientTicketsData] = useState([]);
    let navigate = useNavigate();


    const clientTickets = async (event) => {
  // get all client's tickets
      const data = await getClientTickets(event, userId())
      setClientTicketsData(data.tickets)
    }

    const checkStatus = (status) => {
        if(status === true) {return "aktywny"}
        else if(status === null) {return "nieaktywowany"}
        else {return "wygasły"}
    }

    // get data on site render
    useEffect(() => {clientTickets()}, []);

    const handleClick = (ticket_id) => {
  // redirect to client's ticket details site
      navigate('/szczegoly_karnetu', {
        state: {
          ticketId: ticket_id,
        }
      });
    };

    return (
        <div className="clubsTable">
        <h className="textLogin"> Twoje karnety </h>

        <div className="tablePos">
<Table bordered hover responsive className="tableDesignWide tableDesign" >
  <thead>
    <tr>
      <th>
        Typ
      </th>
      <th>
        Zniżka
      </th>
      <th>
        Cena
      </th>
      <th>
        Status
      </th>
      <th>
        Data ważności
      </th>
      <th>
        Zobacz szczegóły
      </th>
    </tr>
  </thead>
  <tbody>
  {clientTicketsData.length > 0 && clientTicketsData.map((ticket, index) => (
                    <tr key={index}>
                        <th scope="row">{ticket["type"]}({ticket["duration"]})</th>
                        {ticket["discount"] ? <td>{ticket["discount"]}% ({ticket["discount_name"]})</td> : <td> - </td>}
                        <td>{ticket["price"]} zł</td>
                        <td> {checkStatus(ticket["status"])}</td>
                        {ticket["end_date"] ? <td> {ticket["end_date"]}</td> : <td> - </td>}
                        <td> <Button type="button" className="cartStyle text-style" onClick={ (e) => {handleClick(ticket["id"])}}
                        >Szczegóły </Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> </div>
</div>
    );

}

export default ClientTickets;