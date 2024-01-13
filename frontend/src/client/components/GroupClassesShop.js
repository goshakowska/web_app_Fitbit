import React, { useState, useContext, useRef, useEffect } from "react";
import clientToken from '../ClientToken.js';
import { Table, Input, InputGroup, Button } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import getGymsList from "../functions/GymsList.js";
import { useNavigate } from "react-router-dom";


function GroupClassesShop () {
    const {userId} = clientToken();
    const [classes, setClasses] = useState([]);
    const [gymId, setGymId] = useState([]);
    const [gyms, setGyms] = useState([]);
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const stateRef = useRef();
    const navigate = useNavigate();


    const getGroupClasses = async (e) => {
        try {
            const response = await fetch('http://localhost:8000/client/free_gym_classes/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({  gym_id: gymId,
                                      client_id: userId(),
                                      start_date: formatDate(stateRef.current)}),
            });

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setClasses(data.classes)
            console.log(data.classes)


          } catch (error) {
            console.error('Error:', error);
          }
        };

        const getGyms = async (event) => {
            const gyms = await getGymsList(event);
            setGyms(gyms);
        }

        stateRef.current = weekBoundaries.startOfWeek;


        useEffect(() => {
            getGroupClasses();
          }, [stateRef.current, gymId]);
          useEffect((e) => {getGyms(e)}, []);

          const handleClick = (class_id, date, collision_id, free_places) => {
            navigate('/szczegoly_sklep', {
              state: {
                classId: class_id,
                date: date,
                collisionId: collision_id,
                freePlaces: free_places
              }
            });
          };

          return(
            <div className="clubsTable">
                  <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="gym_id" value={gymId} onChange={e => setGymId(e.target.value)}>
                    <option value={null} >Wybierz siłownię</option>
                    {gyms.map((gym, index) => (
                    <option key={index} value={gym[0]}>
                    {gym[1]}
                    </option>
                ))} </Input>
          </InputGroup>
                  <WeekSwitcher />
                  <div>
                    {classes.length > 0 ? <Table bordered hover responsive className="tableDesign" >
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
                  Szczegóły
                  </th>
                </tr>
              </thead>
              <tbody>
              {classes.map((clientClass, index) => (
                                <tr key={index}>
                                    <th scope="row"> {clientClass[1]} </th>
                                    <td> {clientClass[2]} {clientClass[3]} </td>
                                    <td> {clientClass[4]} {clientClass[5]} </td>
                                    <td> {clientClass[7]}</td>
                                    <td> <Button type="button" className="cartStyle" onClick={(e) => {handleClick(clientClass[0], clientClass[4], clientClass[6], clientClass[7])}}
                        >Szczegóły</Button> </td>
                                </tr>
                            ))}
              </tbody>
            </Table> : <p className='errorLabel'>W tym tygodniu nie odbywają się żadne zajęcia grupowe.</p>} </div></div>
                );


}

export default GroupClassesShop