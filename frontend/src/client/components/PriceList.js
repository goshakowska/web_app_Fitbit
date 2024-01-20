import React, { useState, useEffect } from "react";
import { Table } from "reactstrap";
import getPricesList from "../functions/GetPriceList";

export default function PriceList () {
  // shows classes prices
    const [prices, setPrices] = useState([])

    const getPrices = async (event) => {
        const data = await getPricesList(event);
        setPrices(data.price_list)
    }

   // get data on site render
    useEffect((e) => {getPrices(e)}, []);

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