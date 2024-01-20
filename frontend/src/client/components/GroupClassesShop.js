import React, { useState, useContext, useRef, useEffect } from "react";
import clientToken from '../ClientToken.js';
import { Table, Input, InputGroup, Button } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import getGymsList from "../functions/GymsList.js";
import getGroupClasses from "../functions/GroupClassesShopData.js";
import { useNavigate } from "react-router-dom";


function GroupClassesShop () {
  // shows group classes shop
    const {userId} = clientToken();
    const [classes, setClasses] = useState([]);
    const [gymId, setGymId] = useState(null);
    const [gyms, setGyms] = useState([]);
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const stateRef = useRef();
    const navigate = useNavigate();


    const groupClasses = async (e) => {
    // get classes for given gym, userId and week
            const data = await getGroupClasses(e, gymId, userId(), formatDate(stateRef.current));
            console.log(data)
            setClasses(data.classes)
        };

        const getGyms = async (event) => {
    // get gyms for dropdown menu
            const gyms = await getGymsList(event);
            setGyms(gyms);
        }

        stateRef.current = weekBoundaries.startOfWeek;

        // get data on site render
        useEffect((e) => {getGyms(e)}, []);

        // get updated data on every change in gym & data value
        useEffect(() => {
            groupClasses();
          }, [stateRef.current, gymId]);

          const handleClick = (class_id, date, collision_id, free_places, price) => {
            // redirect to class' details site
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

          return(
            <div>
            <div className="clubsTable">
            <h className="smallHeader"> Oferta zajęć grupowych</h>
            <div className="labelsStyle marginBottom">Wybierz swoją siłownię:</div>
                  <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="gym_id" value={gymId} onChange={e => setGymId(e.target.value)}>
                    <option value={null} >Wybierz siłownię</option>
                    {gyms.map((gym, index) => (
                    <option key={index} value={gym[0]}>
                    {gym[1]}
                    </option>
                ))} </Input>
          </InputGroup>
          {gymId ? <>
                  <div className="marginBottom"><WeekSwitcher /></div>
                  <div>
                    {classes.length > 0 ? <Table bordered responsive className="tableDesign tableDesignWide" >
              <thead>
                <tr>
                  <th>
                    Nazwa
                  </th>
                  <th>
                    Trener
                  </th>
                  <th>
                  Data i godzina rozpoczęcia
                  </th>
                  <th>
                  Dostępne miejsca
                  </th>
                  <th>
                  Cena
                  </th>
                  <th>
                  Szczegóły
                  </th>
                </tr>
              </thead>
              <tbody>
              {classes.map((clientClass, index) => (
                                <tr key={index} className={(clientClass[7] === 0 || clientClass[6]) && 'table-danger'}>
                                    <th scope="row"> {clientClass[1]} </th>
                                    <td> {clientClass[2]} {clientClass[3]} </td>
                                    <td> {clientClass[4]} {clientClass[5]} </td>
                                    {clientClass[7] !== 0 ? <td>{clientClass[7]}</td> : <td>Brak miejsc</td>}
                                    <td>{clientClass[8]} zł</td>
                                    <td> <Button type="button" className="cartStyle text-style" onClick={(e) => {handleClick(clientClass[0], clientClass[4], clientClass[6], clientClass[7], clientClass[8])}}
                        >Szczegóły</Button> </td>
                                </tr>
                            ))}
              </tbody>
            </Table> : <label className='errorLabel'>W tym tygodniu nie odbywają się żadne zajęcia grupowe.</label>} </div></> : <label className='errorLabel'>Aby wyświetlić zajęcia, wybierz siłownię.</label>}</div>
            </div>);


}

export default GroupClassesShop