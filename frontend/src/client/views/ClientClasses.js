import React, {useContext, useEffect, useState, useRef} from 'react';
import { Table, Button } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import clientToken from '../ClientToken.js';
import { useNavigate } from "react-router-dom";


function ClientClasses () {
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const {userId} = clientToken();
    const [clientClasses, setClientClasses] = useState([])
    const stateRef = useRef();
    let navigate = useNavigate();


    const getClientClasses = async (e) => {
        try {
            const response = await fetch('http://localhost:8000/client/ordered_classes/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ client_id: userId(),
                                      start_date: formatDate(stateRef.current)}),

            });

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setClientClasses(data.classes)
            console.log(data.classes)


          } catch (error) {
            console.error('Error:', error);
          }
        };

        stateRef.current = weekBoundaries.startOfWeek;

        const handleClick = (class_id) => {
          navigate('/szczegoly_zajec', {
            state: {
              classId: class_id
            }
          });
        };

        useEffect(() => {
            getClientClasses();
          }, [stateRef.current]);

return(
<div className="clubsTable">
      <h className="textLogin"> Twoje zajęcia </h>
      <WeekSwitcher />
      <div>
        {clientClasses.length > 0 ? <Table bordered hover responsive className="tableDesign" >
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
      <th>
        Zobacz szczegóły
      </th>
    </tr>
  </thead>
  <tbody>
  {clientClasses.map((clientClass, index) => (
                    <tr key={index}>
                        <th scope="row"> {clientClass[3]} </th>
                        <td> {clientClass[1]}, {clientClass[2]} </td>
                        <td> {clientClass[4]} {clientClass[5]} </td>
                        <td> <Button type="button" className="cartStyle" onClick={(e) => {handleClick(clientClass[0])}}
                        >Szczegóły</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> : <p className='errorLabel'>Nie masz w tym tygodniu zarezerwowanych żadnych zajęć.</p>} </div></div>
    );

}

export default ClientClasses