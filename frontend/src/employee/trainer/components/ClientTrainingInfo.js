import React, { useState, useEffect } from 'react';
import '../styles/ClientTrainingInfo.css';
import { Grid } from '@mui/material';
import { useLocation } from 'react-router-dom';
// import StatusToggle from './StatusToggle';
// import RegisterTrainingPopup from './RegisterTrainingPopup';
import { Col, Image, Container, Row, Button } from "react-bootstrap";
import { Link } from 'react-router-dom';
import employeeToken from "../../EmployeeToken";
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import MaleIcon from '@mui/icons-material/Male';
import FemaleIcon from '@mui/icons-material/Female';


function ClientTrainingInfo(props) {
  const location = useLocation();
  console.log(props, " props");
  console.log(location, " useLocation Hook");


  const client_id = location.state?.chosenClient;
  const {userId} = employeeToken();

  const [clientData, setClientData] = useState({});


  const getClientDescription = async (event) => {

    try {
        const response = await fetch('http://localhost:8000/trainer/describe_client/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: client_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data.description);
        setClientData(data.description);

      } catch (error) {
        console.error('Error:', error);
      };
}

useEffect(() => {getClientDescription()}, []);

 return (
  <div>
      <Container>
      <Row className="profile">
        <Image src={"../user.png"} alt="profile" />
        <h2 className="name-title-label" alignItems='center'>  {clientData.name} {clientData.surname}</h2>
      </Row>
      <Row className="all-info"
      container
      rowSpacing={3} columnSpacing={{ xs: 1, sm: 2, md: 2 }}
      alignItems="center" >
        <Col xs={6} className="d-flex flex-fill">
          <Grid className="grid-info" spacing={5} item xs={6}>
            <h3 className="title-label">Dane klienta</h3>
            {clientData.birth_year !== null && clientData.birth_year !== undefined ? (
                <p className="label">Data urodzenia: {clientData.birth_year}</p>
              ) : (
                <p className="label">Klient nie podał swojej daty urodzenia.</p>
              )}
            <p className="label">Płeć:
            {clientData.gender === 'M' ? (
            <MaleIcon sx={{ fontSize: 30 }} disabled/>
            ) : (
            <FemaleIcon sx={{ fontSize: 30 }} disabled/>
            )}
            </p>
            <p className="label">Email: {clientData.email}</p>
            <p className="label">Numer telefonu: {clientData.phone_number}</p>
            {clientData.height !== null && clientData.height !== undefined ? (
                <p className="label">Wzrost: {clientData.height} cm</p>
              ) : (
                <p className="label">
                  Klient nie podał swojego wzrostu.
                </p>
              )}
            {clientData.weight !== null && clientData.weight !== undefined ? (
                <p className="label">Waga: {clientData.weight} kg</p>
              ) : (
                <p className="label">
                  Klient nie podał swojej wagi.
                </p>
              )}
            </Grid>
          </Col>
        <Col xs={6} className="d-flex flex-fill">
          <Grid className="grid-info" spacing={5} item xs={6}>
            <h3 className="title-label">Cele treningowe</h3>
            {clientData.target_goal !== null && clientData.target_goal !== undefined ? (
                <p className="label">Cel: {clientData.target_goal}</p>
              ) : (
                <p className="label">
                  Klient nie podał swojego celu treningowego.
                </p>
              )}
              {clientData.target_weight !== null && clientData.target_weight !== undefined ? (
                <p className="label">
                  Idealna waga: {clientData.target_weight} kg
                </p>
              ) : (
                <p className="label">
                  Klient nie podał swojej wagi docelowej.
                </p>
              )}
              <h3 className="title-label">Preferencje treningowe</h3>
              {clientData.training_time !== null && clientData.training_time !== undefined ? (
                <p className="label">
                  Czas pojedynczej sesji: {clientData.training_time} minut
                </p>
              ) : (
                <p className="label">
                  Klient nie podał preferowanego czasu trwania sesji.
                </p>
              )}
              {clientData.training_frequency !== null && clientData.training_frequency !== undefined ? (
                <p className="label">
                  Tygodniowa częstotliwość treningów:{' '}
                  {clientData.training_frequency}
                </p>
              ) : (
                <p className="label">
                  Klient nie podał preferowanej częstotliwości treningów.
                </p>
              )}
            <Button className='button'>Zaplanuj następny trening<Link className="link-button" to="/trener/planer" state={{client_id}} ><ArrowForwardIcon /></Link></Button>
          </Grid>
          </Col>
          </Row>
          </Container>
</div>
 );
};



export default ClientTrainingInfo;
