import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {Table} from 'reactstrap';
import getGymsList from "../functions/GymsList.js";
import "../styles/tablesStyle.css"

function FitnessClubs()
{
  // show all gyms and addresses
    const [gyms, setGyms] = useState([]);
    let navigate = useNavigate();

    const getGyms = async (event) => {
      const gyms = await getGymsList(event);
      setGyms(gyms);
  }

  // get data on site render
    useEffect(() => {getGyms()}, []);

    const handleClick = (club_id, club_name) => {
      // redirect to fitness club's details site
      navigate('/szczegoly_silowni', {
        state: {
          clubId: club_id,
          clubName: club_name,
        }
      });
    };

    return (
      <div className="clubsTable">
      <h className="textLogin"> Nasze siłownie </h>
      <div>
        <Table bordered hover responsive className="tableDesign tableDesignWide" >
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
                        <td onClick={ (e) => {handleClick(gym[0], gym[1])}}> {gym[2]}, {gym[3]}, {gym[4]}</td>
                    </tr>
                ))}
  </tbody>
</Table> </div></div>
    );

}

export default FitnessClubs;