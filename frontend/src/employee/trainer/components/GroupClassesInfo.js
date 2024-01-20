import React, { useState, useEffect } from 'react';
import '../styles/groupClassesInfo.css';
import { useLocation } from 'react-router-dom';
import { Carousel, Col, Row } from "react-bootstrap";
import employeeToken from "../../EmployeeToken";
import '../styles/GroupClassesInfo.css';

function GroupClassInfo(props) {
  const location = useLocation();
  console.log(props, " props");
  console.log(location, " useLocation Hook");


  const class_id = location.state?.chosenTraining;

  const {userName} = employeeToken();

  const [groupClassName, setgroupClassName] = useState("");
  const [groupClassDescription, setgroupClassDescription] = useState("");


  const getGroupClassDescription = async (event) => {

    try {
        const response = await fetch('http://localhost:8000/trainer/describe_group_class/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ class_id: class_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        console.log(data.name);
        console.log(data.description);
        setgroupClassName(data.name);
        setgroupClassDescription(data.description);

      } catch (error) {
        console.error('Error:', error);
      };
}

useEffect(() => {getGroupClassDescription()}, []);

 return (
  <div>
    <Row>
        <h1 className="text" >Witaj {userName()}</h1>
    </Row>
    <Row>
    <Col>
    <Carousel className="custom-carousel" style={{ width: "50%", margin: "auto" }}>
      <Carousel.Item>
      <img className="d-block mx-auto" width={900} height={600} src={"../grupowy_trening.jpg"} alt={groupClassName} style={{ margin: 'auto' }} />
        <Carousel.Caption>
          <h3 className="text">{groupClassName}</h3>
          <p className="custom-caption">HEALTH. STRENGTH. POWER.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
      <img className="d-block mx-auto" width={900} height={600} src={"../grupowy_trening_1.jpg"} alt={groupClassName} style={{ margin: 'auto' }}/>
        <Carousel.Caption>
          <h3 className="text">{groupClassName}</h3>
          <p className="custom-caption">HEALTH. STRENGTH. POWER.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
      <img className="d-block mx-auto" width={900} height={600} src={"../grupowy_trening_2.jpg"} alt={groupClassName} style={{ margin: 'auto' }}/>
        <Carousel.Caption>
          <h3 className="text">{groupClassName}</h3>
          <p className="custom-caption">HEALTH. STRENGTH. POWER.</p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
    </Col>
    <Col>
    <h2 className="text">Zajęcia grupowe - {groupClassName}</h2>
    <p>{groupClassDescription}</p>
    <p className="text"></p>
    </Col>
    </Row>
</div>
 );
};



export default GroupClassInfo;