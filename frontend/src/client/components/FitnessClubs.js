import React, { useState, useEffect } from "react";
import {Table} from 'reactstrap';
import "../styles/tablesStyle.css"

function FitnessClubs()
{
    const [gyms, setGyms] = useState([])

    const getGyms = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/gyms_list/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              }});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setGyms(data.gyms)

          } catch (error) {
            console.error('Error:', error);
          };
    }

    useEffect(() => {getGyms()}, []);

    return (
      <div className="clubsTable">
      <h className="textLogin"> Nasze siłownie </h>
      <div>
        <Table bordered hover responsive className="tableDesign" >
  <thead>
    <tr>
      <th>
        Nazwa
      </th>
      <th>
        Adres
      </th>
    </tr>
  </thead>
  <tbody>
  {gyms.length > 0 && gyms.map((gym, index) => (
                    <tr key={index}>
                        <th scope="row">{gym[1]}</th>
                        <td> {gym[2]}, {gym[3]}, {gym[4]}</td>
                    </tr>
                ))}
  </tbody>
</Table> </div></div>
    );

}

export default FitnessClubs;