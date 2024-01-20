import React, {useContext, useEffect, useState, useRef} from 'react';
import { Table, Button } from 'reactstrap';
import WeekSwitcher from '../components/WeekSwitcher';
import WeekSwitcherContext from '../context/WeekSwitcherContext.js';
import clientToken from '../ClientToken.js';
import getClientClasses from '../functions/GetClientClasses.js';
import { useNavigate } from "react-router-dom";


function ClientClasses () {
    // shows client's ordered classes
    const {weekBoundaries, formatDate} = useContext(WeekSwitcherContext);
    const {userId} = clientToken();
    const [clientClasses, setClientClasses] = useState([])
    const stateRef = useRef();
    let navigate = useNavigate();


    const getClientClassesList = async (e) => {
        // get client's classes
            const data = await getClientClasses(e, userId(), formatDate(stateRef.current));
            setClientClasses(data.classes)
        };

        stateRef.current = weekBoundaries.startOfWeek;

        const handleClick = (class_id) => {
            // redirect to details
          navigate('/szczegoly_zajec', {
            state: {
              classId: class_id
            }
          });
        };

        // get updated data when date changes
        useEffect(() => {
            getClientClassesList();
          }, [stateRef.current]);

return(
<div className="clubsTable">
      <h className="textLogin"> Twoje zajęcia </h>
      <WeekSwitcher />
      <div>
        {clientClasses.length > 0 ? <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
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
                        <td> <Button type="button" className="cartStyle text-style" onClick={(e) => {handleClick(clientClass[0])}}
                        >Szczegóły</Button> </td>
                    </tr>
                ))}
  </tbody>
</Table> : <p className='errorLabel'>Nie masz w tym tygodniu zarezerwowanych żadnych zajęć.</p>} </div></div>
    );

}

export default ClientClasses