import React, { useState, useContext, useRef, useEffect } from "react";
import clientToken from '../ClientToken.js';
import { Table, Input, InputGroup } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import getGymsList from "../functions/GymsList.js";
import getTrainersList from "../functions/TrainersList.js";



function IndvClassesShop () {
    const {userId} = clientToken();
    const [classes, setClasses] = useState([]);
    const [gymId, setGymId] = useState();
    const [trainerId, setTrainerId] = useState();
    const [gyms, setGyms] = useState([]);
    const [clubTrainers, setClubTrainers] = useState([])
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const stateRef = useRef();


    const getIndvClasses = async (e) => {
        try {
            const response = await fetch('http://localhost:8000/client/free_trainings/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({  trainer_id: trainerId,
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

        const getTrainers = async (event, club_id) => {
            const trainers = await getTrainersList(event, club_id);
            setClubTrainers(trainers);
        }

        stateRef.current = weekBoundaries.startOfWeek;


        useEffect(() => {
            getIndvClasses();
          }, [stateRef.current, trainerId]);
          useEffect((e) => {getGyms(e)}, []);
          useEffect((e) => {getTrainers(e, gymId)}, [gymId]);

          return(
            <div className="clubsTable">
                  <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="gymId" value={gymId} onChange={e => setGymId(e.target.value)}>
                    <option value={null} >Wybierz siłownię</option>
                    {gyms.map((gym, index) => (
                    <option key={index} value={gym[0]}>
                    {gym[1]}
                    </option>
                ))} </Input>
          </InputGroup>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="trainerId" value={trainerId} onChange={e => setTrainerId(e.target.value)}>
                    <option value={null} >Wybierz trenera</option>
                    {clubTrainers.map((trainer, index) => (
                    <option key={index} value={trainer[0]}>
                    {trainer[1]} {trainer[2]}
                    </option>
                ))} </Input>
          </InputGroup>
                  <WeekSwitcher />
                  <div>
                    {classes ? <Table bordered hover responsive className="tableDesign" >
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
            </Table> : <p className='errorLabel'>W tym tygodniu nie odbywają się żadne zajęcia grupowe.</p>} </div></div>
                );


}

export default IndvClassesShop