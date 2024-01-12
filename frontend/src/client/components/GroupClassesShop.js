import React, { useState, useContext, useRef, useEffect } from "react";
import clientToken from '../ClientToken.js';
import { Table, Input, InputGroup } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import getGymsList from "../functions/GymsList.js";


function GroupClassesShop () {
    const {userId} = clientToken();
    const [classes, setClasses] = useState([]);
    const [gymId, setGymId] = useState([]);
    const [gyms, setGyms] = useState([]);
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const stateRef = useRef();


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
                    Data i godzina rozpoczęcia
                  </th>
                  <th>
                    Trener
                  </th>
                </tr>
              </thead>
              <tbody>
              {classes.map((clientClass, index) => (
                                <tr key={index}>
                                    <th scope="row"> {clientClass[3]} </th>
                                    <td> {clientClass[1]}, {clientClass[2]} </td>
                                    <td> {clientClass[4]} {clientClass[5]} </td>
                                </tr>
                            ))}
              </tbody>
            </Table> : <p className='errorLabel'>W tym tygodniu podany trener nie prowadzi żadnych zajęć.</p>} </div></div>
                );


}

export default GroupClassesShop