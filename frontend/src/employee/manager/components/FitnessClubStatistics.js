import React, { useState, useEffect } from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import employeeToken from '../../EmployeeToken.js';
import '../styles/FitnessClubStatistics.css';

function FitnessClubStatistics()
{
    const {userName} = employeeToken();
    const {userId} = employeeToken();
    const [chartImage, setChartImage] = useState(null);
    const [selectedEquipment, setSelectedEquipment] = useState('');
    const [allEquipment, setAllEquipment] = useState([]);
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

    const getChartImageWithProvidedData = async (url) => {
        try {
            const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },body: JSON.stringify({ manager_id: userId() })});

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

    const getChartImageWithProvidedDataName = async (url) => {
        try {
            const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },body: JSON.stringify({ manager_id: userId(), equipment_name: selectedEquipment })});

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

    const getAllEquipment = async (event) => {
        try {
            const response = await fetch('http://localhost:8000/manager/all_equipment/', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                },body: JSON.stringify({ manager_id: userId() })});

              if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
              }

              const data = await response.json();
              console.log(data.names);
              setAllEquipment(data.names);

            } catch (error) {
              console.error('Error:', error);
        }
    }

        useEffect(() => {getAllEquipment()}, []);

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
                        <button className="sub-label" onClick={() => getChartImageWithProvidedData('http://localhost:8000/manager/clients_week/')}>
                        1. tygodniowa
                        </button>
                    </li>
                    <li>
                        <button className="sub-label" onClick={() => getChartImageWithProvidedData('http://localhost:8000/manager/clients_hour/')}>
                        2. dzienna
                        </button>
                    </li>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => getChartImageWithProvidedData('http://localhost:8000/manager/sessions/')}>
                    Liczba zamówionych sesji u poszczególnych trenerów
                    </button>
                </li>
                <li className='default'>
                <button
                                className="label"
                                onClick={() => getChartImageWithProvidedDataName('http://localhost:8000/manager/equipment_usage/')}
                                disabled={!selectedEquipment}
                            >
                                Obciążenie sprzętu
                            </button>
                            <select
                                className="label"
                                onChange={(e) => setSelectedEquipment(e.target.value)}
                                value={selectedEquipment}
                            >
                                <option value="" disabled>
                                    Wybierz sprzęt
                                </option>
                                {allEquipment.map((equipment, index) => (
                                    <option key={index} value={equipment}>
                                        {equipment}
                                    </option>
                                ))}
                            </select>
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