import React, { useState, useEffect } from "react";
import { Table } from "reactstrap";

export default function PriceList () {
    const [prices, setPrices] = useState([])

    const getPrices = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/price_list/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              }});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setPrices(data.price_list)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect(() => {getPrices()}, []);

    return (
        <div className="clubsTable">
      <h className="textLogin"> Cennik </h>
      <div>
        <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
  <thead>
    <tr>
      <th>
        Nazwa zajęć
      </th>
      <th>
        Cena
      </th>
    </tr>
  </thead>
  <tbody>
  {prices.length > 0 && prices.map((className, index) => (
                    <tr key={index}>
                        <th scope="row">{className[0]}</th>
                        <td>{className[1]} zł</td>
                    </tr>
                ))}
  </tbody>
</Table> </div></div>
    )
}