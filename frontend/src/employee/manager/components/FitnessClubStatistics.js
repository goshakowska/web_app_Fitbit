
import React, { useState } from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import employeeToken from '../../EmployeeToken.js';
import '../styles/FitnessClubStatistics.css';

function FitnessClubStatistics()
{
    const {userName} = employeeToken();
    const [chartImage, setChartImage] = useState(null);
    console.log(userName());

    const getChartImage = async (url) => {
        try {
            const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            });

            if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setChartImage(data.plot)
        } catch (error) {
            alert('Wykryto błąd');
            console.log(error);
        }
    }

    return (
    <div>
        <h1 className='welcome-prompt'>Witaj {userName()}, o to aktualne statystyki sieci klubów Fitbit</h1>
        <Row>
        <Col md={{ span: 5, offset: 2 }} >
            <ul className='graph-panel'>
                <p className='title-label'>Dostępne statystyki</p>
                <li className='default'>
                    <button className="label" onClick={() => getChartImage('http://localhost:8000/manager/ticket_popularity_week/')}>
                    Popularność karnetów
                    </button>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => getChartImage('http://localhost:8000/manager/discount_popularity_week/')}>
                    Popularność promocji
                    </button>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => getChartImage('http://localhost:8000/manager/age_range/')}>
                    Przedziały wiekowe klientów
                    </button>
                </li>
                <li className="up-label">
                Częstość przychodzenia klientów
                    <li>
                        <button className="sub-label" /*onClick={() => getChartImage(stat)}*/>
                        1. tygodniowa
                        </button>
                    </li>
                    <li>
                        <button className="sub-label" /*onClick={() => getChartImage(stat)}*/>
                        2. dzienna
                        </button>
                    </li>
                </li>
                <li className='default'>
                    <button className="label" /*onClick={() => getChartImage(stat)}*/>
                    Liczba zamówionych sesji u poszczególnych trenerów
                    </button>
                </li>
                <li className='default'>
                    <button className="label" /*onClick={() => getChartImage(stat)}*/>
                    Obciążenie sprzętu
                    </button>
                </li>
            </ul>
        </Col>
        <Col md={{ span: 5}}>
            <Card bordered hover responsive className='graph'>
                <Card.Img src={`data:image/jpeg;base64,${chartImage}`} alt="W celu wyświetlenia statystyki wybierz ją z listy" />
            </Card>
        </Col>
        </Row>
    </div>
    );
};

export default FitnessClubStatistics;
