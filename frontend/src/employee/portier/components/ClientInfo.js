import React, { useState } from 'react';
import '../styles/ClientInfo.css';
import { Grid } from '@mui/material';
import { useLocation } from 'react-router-dom';
import StatusToggle from './StatusToggle';
import RegisterTrainingPopup from './RegisterTrainingPopup';

function ClientInfo(props) {
  const location = useLocation();
  console.log(props, " props");
  console.log(location, " useLocation Hook");


  const client = location.state?.client;

 return (
  <div>
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
        <p className="label">Email: {client.email}</p>
        <p className="label">Numer telefonu: {client.phoneNumber}</p>
        <button>Show client's timetable</button>
      </Grid>
      <Grid className="client-card" spacing={5} item xs={6}>
        <h3 className="title-label">Karnet</h3>
        <p className="label">Typ: {client.cardType}</p>
        <p className="label"><StatusToggle initialStatus={client.cardStatus}/></p>
      </Grid>
      <Grid className="training-info" spacing={5} item xs={6}>
          <p className="label">Najbliższy trening: {client.nextTraining}</p>
          <RegisterTrainingPopup/>
      </Grid>
      <Grid className="card-dates" spacing={5} item xs={6}>
        <p className="label">Data aktywacji: {client.activationDate}</p>
        <p className="label">Data ważności: {client.expirationDate}</p>
      </Grid>
    </Grid>
</div>
 );
};



export default ClientInfo;