import React, { useState, useEffect } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import 'moment/locale/en-gb';
import "react-big-calendar/lib/css/react-big-calendar.css";
import "../styles/scheduler.css";
import { Row, Col } from "react-bootstrap";
import employeeToken from "../../EmployeeToken";
import { Link } from 'react-router-dom';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';


moment.locale("en-GB");
const localizer = momentLocalizer(moment);

export default function Scheduler() {

  const {userId} = employeeToken();
  const {userName} = employeeToken();
  const [trainerEvents, setTrainerEvents] = useState([]);
  const [isShown, setIsShown] = useState(false);
  const [chosenTraining, setChosenTrainingId] = useState("");
  const [chosenClient, setChosenClientId] = useState("");
  const [chosenTrainingName, setChosenTrainingName] = useState("");
  const [chosenClientName, setChosenClientName] = useState("");
  // let navigate = useNavigate();

  const getTrainerEvents = async (event) => {
    try {
        const response = await fetch('http://localhost:8000/trainer/timetable/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ trainer_id: userId()})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        const trainings = data.classes.map(training => ({start: new Date(training.start), end: new Date(training.end), title: training.title, data: {training}}),);
        console.log(data.classes);
        setTrainerEvents(trainings);

      } catch (error) {
        console.error('Error:', error);
      };
}

 useEffect(() => {getTrainerEvents()}, []);

  const handleCloseClick = event => {

    setIsShown(false);
    setChosenClientId(null);
  };

  const handleAdditionalComponentClick = event => {

    setIsShown(true);
    setChosenTrainingId(event.data.training.id);
    setChosenTrainingName("")
    console.log(event.data)
    console.log(chosenTraining);
    // setIsShown(true);
    if (event.data.training.title === 'Trening indywidualny') {
      setChosenClientId(event.data.training.client_id);
      setChosenTrainingName(event.data.training.title);
      setChosenClientName(event.data.training.client_name)
      console.log(event.data.training.client_id);
      console.log(chosenTrainingName);
      console.log(chosenClient);
    } else {
      setChosenClientId(null);
      setChosenTrainingId(event.data.training.id);
      setChosenTrainingName(event.data.training.title);
      console.log(chosenClient);
      console.log(chosenTrainingName);
      console.log(chosenTraining);
    }

    console.log(chosenTrainingName);


  };

  return (
    <div className="Calendar">
      <Row className="justify-content-center">
        <header className="welcome-prompt">
          Witaj {userName()}
        </header>
      </Row>
      <Row className="justify-content-center">
        <Col md={{offset: 1 }} className="calendar-column">
          <Calendar className="trainer-calendar"
            views={["day", "agenda", "week", "month"]}
            selectable
            localizer={localizer}
            defaultDate={new Date()}
            min={new Date(0, 0, 0, 8, 0, 0)} // 8 am
            max={new Date(0, 0, 0, 21, 0, 0)} // 9 pm
            defaultView="week"
            events={trainerEvents}
            style={{ height: "75vh", width: "75vh" }}
            onSelectEvent={(event) => handleAdditionalComponentClick(event)}
          />
        </Col>
        {isShown && (
        <Col md={{offset: 1 }} className="button-column">
          {chosenTrainingName === 'Trening indywidualny' ? (
                  <p>
                  <button className="trainer-button">Zobacz szczegóły zajęć indywidualnych z: {chosenClientName}
                    <Link className="link-button" to="/trener/client_info" state={{chosenClient}}>
                      <ArrowForwardIcon />
                    </Link>
                  </button>
                  <button className="trainer-button" onClick={(e) => handleCloseClick()}>
                    Zamknij
                  </button>
                  </p>
                ) : (
                  <p>
                  <button className="trainer-button">Zobacz szczegóły zajęć grupowych: {chosenTrainingName}
                    <Link className="link-button" to="/trener/group_class_info" state={{chosenTraining}}>
                      <ArrowForwardIcon />
                    </Link>
                  </button>
                  <button className="trainer-button" onClick={(e) => handleCloseClick()}>
                  Zamknij
                </button>
                </p>
                )}
            </Col>
          )}
      </Row>
    </div>
  );
}