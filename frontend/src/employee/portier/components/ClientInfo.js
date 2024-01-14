import React, { Component, useState } from 'react';
import '../styles/ClientInfo.css';
import { Grid } from '@mui/material';
import { useLocation } from 'react-router-dom';
import StatusToggle from './StatusToggle';
import RegisterTrainingPopup from './RegisterTrainingPopup';
import { Container } from 'react-bootstrap';

function ClientInfo(props) {
  const location = useLocation();
  console.log(props, " props");
  console.log(location, " useLocation Hook");


  const client = location.state?.client;

 return (
  <div>
    <Container className='portier-client-info'>
    <Grid className="profile">
        <img src={"../user.png"} alt="profile" />
        <h2 className="name-title-label">  {client.name} {client.surname}</h2>
    </Grid>
    <Grid className="all-info"
          container
          rowSpacing={3} columnSpacing={{ xs: 1, sm: 2, md: 3 }}
          alignItems="center" >
      <Grid className="client-info" spacing={5} item xs={6}>
        <h3 className="title-label">Dane klienta</h3>
        <p className="labels">Email: {client.email}</p>
        <p className="labels">Numer telefonu: {client.phoneNumber}</p>
        <button className='button-client-info'>Show client's timetable</button>
      </Grid>
      <Grid className="client-card" spacing={5} item xs={6}>
        <h3 className="title-label">Karnet</h3>
        <p className="labels">Typ: {client.cardType}</p>
        <p className="labels"><StatusToggle initialStatus={client.cardStatus}/></p>
      </Grid>
      <Grid className="training-info" spacing={5} item xs={6}>
          <p className="labels">Najbliższy trening: {client.nextTraining}</p>
          <RegisterTrainingPopup/>
      </Grid>
      <Grid className="card-dates" spacing={5} item xs={6}>
        <p className="labels">Data aktywacji: {client.activationDate}</p>
        <p className="labels">Data ważności: {client.expirationDate}</p>
      </Grid>
    </Grid>
    </Container>
</div>
 );
};



export default ClientInfo;