import React, { useState, useEffect} from "react";
import {Button, Table} from 'reactstrap';
import "../styles/tablesStyle.css"
import clientToken from '../ClientToken.js';
import { useNavigate } from "react-router-dom";



function ClientTickets()
{
    const {userId} = clientToken();
    const [clientTickets, setClientTickets] = useState([]);
    let navigate = useNavigate();


    const getClientTickets = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/gym_tickets_history/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ client_id: userId()})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.tickets)
            setClientTickets(data.tickets)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    const checkStatus = (status) => {
        if(status === true) {return "aktywny"}
        else if(status === null) {return "nieaktywowany"}
        else {return "wygasły"}
    }

    useEffect(() => {getClientTickets()}, []);

    const handleClick = (ticket_id) => {
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
  {clientTickets.length > 0 && clientTickets.map((ticket, index) => (
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