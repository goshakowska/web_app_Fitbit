
import React, { useState, useEffect } from 'react';
import '../styles/ClientInfo.css';
import { Grid, Button, Select, MenuItem } from '@mui/material';
import { useLocation } from 'react-router-dom';
import { Container, Row, Col } from 'react-bootstrap';
import employeeToken from "../../EmployeeToken";

function ClientInfo(props) {
  const location = useLocation();
  const client = location.state?.client;
  const {userId} = employeeToken();

  const [clientDescription, setClientDescription] = useState([]);
  const [notActiveTicketsList, setNotActiveTicketsList] = useState([]);
  const [isCurrentlyOnGym, setIsCurrentlyOnGym] = useState(false);
  const [isTraining, setIsTraining] = useState(false);

  const [selectedTicket, setSelectedTicket] = useState(null);

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

    const getNotActiveTicketsList = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/client/not_active_list/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ client_id: client})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.tickets)
            setNotActiveTicketsList(data.tickets);

          } catch (error) {
            console.error('Error:', error);
          };
        }

        useEffect((e) => {getNotActiveTicketsList(e)}, []);

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
          console.log(client)
          console.log(selectedTicket.ticket_id)
            try {
                const response = await fetch('http://localhost:8000/portier/activate_ticket/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ client_id: client, ticket_id: selectedTicket.ticket_id }),
                });

                if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                if (data === false) {
                  alert("Klient nie posiada biletów do aktywowania.");
              } else  {
                  alert("Karnet został pomyślnie aktywowany.");
              }
              window.location.reload(false)
              getClientDescription();
            } catch (error) {
                console.error('Error:', error);
            }
          };

        const handleStartTraining = async (event) => {
            try {
                const response = await fetch('http://localhost:8000/portier/register_entry/', {
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
                setIsTraining(true);
              } catch (error) {
                console.error('Error:', error);
              };
            };

        const handleAssignLocker = async (event) => {
          try {
            if (isTraining) {
              const response = await fetch('http://localhost:8000/portier/assign_locker/', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({ client_id: client, portier_id: userId() }),
              });
        
              if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
              }
        
              const data = await response.json();
              console.log(data.locker);
              alert("Klientowi została przyznana szafka o numerze: " + data.locker + ".");
            } else {
              alert("Najpierw rozpocznij trening, aby przydzielić szafkę.");
            }
          } catch (error) {
            console.error('Error:', error);
          }
        };


        const handleFinishTraining = async (event) => {
          try {
            const response = await fetch('http://localhost:8000/portier/register_leave/', {
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
            if (data.locker === null) {
              alert("Trening został zakończony o godzinie: " + data.time + ". Żadna szafka nie została wcześniej przypisana.");
            } else {
              alert("Trening został zakończony o godzinie: " + data.time + ". Zwolniona została szafka nr. " + data.locker);
            }
            setIsCurrentlyOnGym(false)
            isTraining(false)
            window.location.reload(false)

          } catch (error) {
            console.error('Error:', error);
          };
        };

      return (
        <div>
          <Container className='portier-client-info'>
            <Row className="profile">
              <img src={"../user.png"} alt="profile" />
              <h2 className="name-title-label"> {clientDescription.name} {clientDescription.surname}</h2>
            </Row>

            <Row className="portier-client-info" container rowSpacing={3} alignItems="center">
            <Col xs={6} className="d-flex flex-fill">
                <Grid className="client-info" container item xs={10}>
                <h3 className="title-label">Dane klienta:</h3>
                <p className="labels">Email: {clientDescription.email}</p>
                <p className="labels">Numer telefonu: {clientDescription.phone}</p>
                </Grid>
            </Col>
            <Col xs={6} className="d-flex flex-fill">
                <Grid className="client-card" container item xs={10} >
                <h3 className="title-label">Dane karnetu:</h3>
                  {clientDescription.active ? (
                    <div>
                      <p className="labels">Typ karnetu: {clientDescription.ticket_name}</p>
                      {clientDescription.daily ? (
                        <div>
                          <p className="labels">Data ważności: {clientDescription.end_date}</p>
                        </div>
                      ) : (
                        <p className="labels">Liczba pozostałych wejść: {clientDescription.visit_left}</p>
                      )}
                    </div>
                  ) : (
                    <div>
                        <p className="labels">Musisz aktywować karnet</p>
                  <Select className="select" value={selectedTicket ? selectedTicket.ticket_name : ''} onChange={(e) => setSelectedTicket(notActiveTicketsList.find(ticket => ticket.ticket_name === e.target.value))}>
                    {notActiveTicketsList.map((ticket) => (
                      <MenuItem className="option" key={ticket.ticket_id} value={ticket.ticket_name}>
                        {ticket.ticket_name}
                      </MenuItem>
                    ))}
                  </Select>
                  <Button className="activation-button" onClick={() => handleTicketActivation(selectedTicket)}>Aktywuj karnet: {selectedTicket ? selectedTicket.ticket_name : ''}!</Button>
                    </div>
                  )}
                </Grid>
            </Col>
            </Row>
                {clientDescription.active && !isCurrentlyOnGym ? (
                  <div>
                    <Row className="entrance-info" container rowSpacing={3} alignItems="center">
                      <Row className="justify-content-center">   
                      <Col xs={6} className="text-start">                 
                    <Button className="activation-button" onClick={handleStartTraining} disabled={!clientDescription.active}>
                      Rozpocznij trening!
                    </Button>
                    </Col>
                    <Col xs={6} className="text-end"> 
                    <Button className="activation-button" onClick={handleAssignLocker} disabled={!clientDescription.active && !isTraining}>
                      Przydziel szafkę.
                    </Button>
                    </Col>
                    </Row>

                    <Button className="activation-button" onClick={() => window.location.reload(false)} disabled={!clientDescription.active}>
                      Zamknij.
                    </Button>
                    </Row>
                  </div>
                ) : isCurrentlyOnGym ? (
                  <div>
                    <Row className="entrance-info" container rowSpacing={3} alignItems="center">
                    <Button className="activation-button" onClick={handleFinishTraining} disabled={!isCurrentlyOnGym}>
                      Zakończ trening.
                    </Button>
                    </Row>
                  </div>
                ) : null}
          </Container>
        </div>
      );
    }

    export default ClientInfo;