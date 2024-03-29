import React, { useState, useContext, useRef, useEffect } from "react";
import clientToken from '../ClientToken.js';
import { Table, Input, InputGroup, Button } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import getGymsList from "../functions/GymsList.js";
import getTrainersList from "../functions/TrainersList.js";
import getIndvClasses from "../functions/IndvClassesShopData.js";
import { useNavigate } from "react-router-dom";


function IndvClassesShop () {
  // shows individual classes shop
    const {userId} = clientToken();
    const [classes, setClasses] = useState([]);
    const [gymId, setGymId] = useState();
    const [trainerId, setTrainerId] = useState();
    const [gyms, setGyms] = useState([]);
    const [clubTrainers, setClubTrainers] = useState([])
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const stateRef = useRef();
    const navigate = useNavigate();

    const indvClasses = async (e) => {
      // gets classes data for given trainer, week and user
            const data = await getIndvClasses(e, trainerId, formatDate(stateRef.current), userId())
            setClasses(data.trainings)
        };

        const getGyms = async (event) => {
      // get gyms for dropdown menu
            const gyms = await getGymsList(event);
            setGyms(gyms);
        }

        const getTrainers = async (event, club_id) => {
      // get trainers for given gym for dropdown menu
            const trainers = await getTrainersList(event, club_id);
            setClubTrainers(trainers);
        }

        stateRef.current = weekBoundaries.startOfWeek;

      // get data on site render
        useEffect((e) => {getGyms(e)}, []);
      // get updated data on every change in gym value
        useEffect((e) => {getTrainers(e, gymId)}, [gymId]);
      // get updated data on every change in trainer & data value
        useEffect(() => {
            indvClasses();
          }, [stateRef.current, trainerId]);

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
            <h className="smallHeader"> Oferta zajęć indywidualnych</h>
            <div className="labelsStyle marginBottom">Wybierz swoją siłownię:</div>
                  <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="gymId" value={gymId} onChange={e => setGymId(e.target.value)}>
                    <option value={null} >Wybierz siłownię</option>
                    {gyms.map((gym, index) => (
                    <option key={index} value={gym[0]}>
                    {gym[1]}
                    </option>
                ))} </Input>
          </InputGroup>
          <div className="labelsStyle marginBottom">Wybierz swojego trenera:</div>
          <InputGroup className="inputGroup">
              <Input className='centeredTextInput' type= "select" name="trainerId" value={trainerId} onChange={e => setTrainerId(e.target.value)}>
                    <option value={null} >Wybierz trenera</option>
                    {clubTrainers.map((trainer, index) => (
                    <option key={index} value={trainer[0]}>
                    {trainer[1]} {trainer[2]}
                    </option>
                ))} </Input>
          </InputGroup>
          {gymId && trainerId ? <>
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
                    Dostępność
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
                                    {clientClass[7] !== 0 ? <td>Termin dostępny</td> : <td>Termin zajęty</td>}
                                    <td>{clientClass[8]} zł</td>
                                    <td> <Button type="button" className="cartStyle text-style" onClick={(e) => {handleClick(clientClass[0], clientClass[4], clientClass[6], clientClass[7], clientClass[8])}}
                        >Szczegóły</Button> </td>
                                </tr>
                            ))}
              </tbody>
            </Table> : <p className='errorLabel'>W tym tygodniu podany trener nie prowadzi żadnych zajęć.</p>} </div></> : <p className='errorLabel'>Aby wyświetlić zajęcia, wybierz siłownię oraz trenera.</p>}</div>
            </div>);


}

export default IndvClassesShop