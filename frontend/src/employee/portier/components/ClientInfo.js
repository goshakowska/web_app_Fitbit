// import React, { Component, useState } from 'react';
// import '../styles/ClientInfo.css';
// import { Grid } from '@mui/material';
// import { useLocation } from 'react-router-dom';
// import StatusToggle from './StatusToggle';
// import RegisterTrainingPopup from './RegisterTrainingPopup';
// import { Container } from 'react-bootstrap';

// function ClientInfo(props) {
//   const location = useLocation();
//   console.log(props, " props");
//   console.log(location, " useLocation Hook");


//   const client = location.state?.client;

//  return (
//   <div>
//     <Container className='portier-client-info'>
//     <Grid className="profile">
//         <img src={"../user.png"} alt="profile" />
//         <h2 className="name-title-label">  {client.name} {client.surname}</h2>
//     </Grid>
//     <Grid className="all-info"
//           container
//           rowSpacing={3} columnSpacing={{ xs: 1, sm: 2, md: 3 }}
//           alignItems="center" >
//       <Grid className="client-info" spacing={5} item xs={6}>
//         <h3 className="title-label">Dane klienta</h3>
//         <p className="labels">Email: {client.email}</p>
//         <p className="labels">Numer telefonu: {client.phoneNumber}</p>
//         <button className='button-client-info'>Show client's timetable</button>
//       </Grid>
//       <Grid className="client-card" spacing={5} item xs={6}>
//         <h3 className="title-label">Karnet</h3>
//         <p className="labels">Typ: {client.cardType}</p>
//         <p className="labels"><StatusToggle initialStatus={client.cardStatus}/></p>
//       </Grid>
//       <Grid className="training-info" spacing={5} item xs={6}>
//           <p className="labels">Najbliższy trening: {client.nextTraining}</p>
//           <RegisterTrainingPopup/>
//       </Grid>
//       <Grid className="card-dates" spacing={5} item xs={6}>
//         <p className="labels">Data aktywacji: {client.activationDate}</p>
//         <p className="labels">Data ważności: {client.expirationDate}</p>
//       </Grid>
//     </Grid>
//     </Container>
// </div>
//  );
// };



// export default ClientInfo;


import React, { useState, useEffect } from 'react';
import '../styles/ClientInfo.css';
import { Grid, Button, Select, MenuItem } from '@mui/material';
import { useLocation } from 'react-router-dom';
import { Container } from 'react-bootstrap';
import employeeToken from "../../EmployeeToken";

function ClientInfo(props) {
  const location = useLocation();
  const client = location.state?.client;
  const {userId} = employeeToken();

  const [clientDescription, setClientDescription] = useState([]);
  // const [notActiveTicketsList, setNotActiveTicketsList] = useState([]);
  const [isCurrentlyOnGym, setIsCurrentlyOnGym] = useState(false);


  // const [selectedTicket, setSelectedTicket] = useState('');

  const getClientDescription = async (event) => {
    try {
        console.log(client);
        const response = await fetch('http://localhost:8000/client/describe_client_portier/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: client})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data.description)
        setClientDescription(data.description);

      } catch (error) {
        console.error('Error:', error);
      };
    }

    useEffect((e) => {getClientDescription(e)}, []);

    // const getNotActiveTicketsList = async (event) => {
    //     try {
    //         const response = await fetch('http://localhost:8000/client/not_active_list/', {
    //           method: 'POST',
    //           headers: {
    //             'Content-Type': 'application/json',
    //           },body: JSON.stringify({ client_id: client})});

    //         if (!response.ok) {
    //           throw new Error(`HTTP error! Status: ${response.status}`);
    //         }

    //         const data = await response.json();
    //         console.log(data.tickets)
    //         setNotActiveTicketsList(data.tickets);

    //       } catch (error) {
    //         console.error('Error:', error);
    //       };
    //     }

    //     useEffect((e) => {getNotActiveTicketsList(e)}, []);

        const getIsOnGym = async (event) => {
            try {
                const response = await fetch('http://localhost:8000/client/is_on_gym/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },body: JSON.stringify({ client_id: client})});

                if (!response.ok) {
                  throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                console.log(data.is_on_gym)
                setIsCurrentlyOnGym(data.is_on_gym);

              } catch (error) {
                console.error('Error:', error);
              };
        }

        useEffect((e) => {getIsOnGym(e)}, []);

        const handleTicketActivation = async (event) => {
            try {
                const response = await fetch('http://localhost:8000/client/activate_ticket/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ client_id: client }),
                });

                if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                if (data === false) {
                  alert("Klient nie posiada biletów do aktywowania.");
              } else  {
                  alert("Bilet został pomyślnie aktywowany.");
              }
              getClientDescription();
            } catch (error) {
                console.error('Error:', error);
            }
          };

            const handleRequest = () => {
              // console.log(client_id);
              console.log(client);
              console.log(clientDescription)
              // console.log(notActiveTicketsList);
              console.log(isCurrentlyOnGym)

            };

          //   return (
          //     <div>
          //         <button onClick={handleRequest}></button>
          //     </div>
          //   );
          // }

        const handleStartTraining = async (event) => {
            try {
                const response = await fetch('http://localhost:8000/client/register_entry/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },body: JSON.stringify({ client_id: client, portier_id: userId()})});

                if (!response.ok) {
                  throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                console.log(data.time)
                alert("Trening został rozpoczęty o godzinie: "+ data.time + ".");

              } catch (error) {
                console.error('Error:', error);
              };
            };

        const handleAssignLocker = async (event) => {
          try{
            const response = await fetch('http://localhost:8000/client/assign_locker/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ client_id: client, portier_id: userId()})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.locker)
            alert("Klientowi została przyznana szafka o numerze: "+ data.locker + ".");

          } catch (error) {
            console.error('Error:', error);
          };
          };


        const handleFinishTraining = async (event) => {
          try {
            const response = await fetch('http://localhost:8000/client/register_leave/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ client_id: client, portier_id: userId()})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.time)
            console.log(data.locker)
            alert("Trening został zakończony o godzinie: "+ data.time + ". Zwolniona została szafka nr. " + data.locker);

          } catch (error) {
            console.error('Error:', error);
          };
        };

      return (
        <div>
          <Container className='portier-client-info'>
            <Grid className="profile">
              <img src={"../user.png"} alt="profile" />
              <h2 className="name-title-label"> {clientDescription.name} {clientDescription.surname}</h2>
            </Grid>
            <Grid className="all-info" container rowSpacing={3} columnSpacing={{ xs: 1, sm: 2, md: 3 }} alignItems="center">
              <Grid className="client-info" spacing={5} item xs={6}>
            <h3 className="title-label">Dane klienta</h3>
            <p className="labels">Email: {clientDescription.email}</p>
            <p className="labels">Numer telefonu: {clientDescription.phone}</p>
            <Button onClick={handleRequest}>sprawdź</Button>
              </Grid>
              <Grid className="client-card" spacing={5} item xs={6}>
                {clientDescription.active_ticket ? (
                  <div>
                    <p className="labels">Ticket Type: {clientDescription.ticket_name}</p>
                    {clientDescription.type === 'Dniowy' ? (
                      <div>
                        <p className="labels">Expiration Date: {clientDescription.end_date}</p>
                      </div>
                    ) : (
                      <p className="labels">Entrances Left: {clientDescription.visit_left}</p>
                    )}
                  </div>
                ) : (
                  <div>
                      <p className="labels">Musisz aktywować karnet</p>
                    {/* <Select value={selectedTicket} onChange={handleTicketSelection}>
                      {notActiveTicketsList.map((ticket) => (
                        <MenuItem key={ticket.ticket_id} value={ticket.ticket_name}>
                          {ticket.ticket_name}
                        </MenuItem>
                      ))}
                    </Select> */}
                    <Button onClick={handleTicketActivation}>Aktywuj!</Button>
                  </div>
                )}
              </Grid>
                {clientDescription.active && !isCurrentlyOnGym ? (
                  <div>
                    <Grid className="training-info" spacing={5} item xs={6}>
                    <Button onClick={handleStartTraining} disabled={!clientDescription.isActive}>
                      Rozpocznij trening!
                    </Button>
                    <Button onClick={handleAssignLocker} disabled={!clientDescription.isActive}>
                      Przydziel szafkę.
                    </Button>
                    </Grid>
                  </div>
                ) : isCurrentlyOnGym ? (
                  <div>
                    <Grid className="training-info" spacing={5} item xs={6}>
                    <Button onClick={handleFinishTraining} disabled={!clientDescription.isActive}>
                      Zakończ trening.
                    </Button>
                    </Grid>
                  </div>
                ) : null}
            </Grid>
          </Container>
        </div>
      );
    }

    export default ClientInfo;