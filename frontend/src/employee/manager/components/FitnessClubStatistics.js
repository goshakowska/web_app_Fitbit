import React, { useState, useEffect } from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import employeeToken from '../../EmployeeToken.js';
import '../styles/FitnessClubStatistics.css';
import allEquipment from "../functions/allEquipment.js";
import chartImage from "../functions/chartImage.js";
import chartImageWithProvidedData from "../functions/chartImageWithProvidedData.js";
import chartImageWithProvidedDataName from "../functions/chartImageWithProvidedDataName.js";

function FitnessClubStatistics()
{
    const {userName} = employeeToken();
    const {userId} = employeeToken();
    const [chosenChartImage, setChosenChartImage] = useState(null);
    const [selectedEquipment, setSelectedEquipment] = useState('');
    const [allPossibleEquipment, setAllPossibleEquipment] = useState([]);
    console.log(userName());



    const handleAllEquipment = async (manager_id) => {
        const allFetchedEquipment = await allEquipment(manager_id);
        setAllPossibleEquipment(allFetchedEquipment);
    }

    useEffect(() => {handleAllEquipment(userId())}, []);

    const handleChartImage = async (url, manager_id) => {
        const fetchedChartImage = await chartImage(url, manager_id);
        setChosenChartImage(fetchedChartImage)
    }

    const handleChartImageWithProvidedData = async (url, manager_id) => {
        const fetchedChartImage = await chartImageWithProvidedData(url, manager_id);
        setChosenChartImage(fetchedChartImage)
    }

    const handleChartImageWithProvidedDataName = async (url, manager_id, equipment_name) => {
        const fetchedChartImage = await chartImageWithProvidedDataName(url, manager_id, equipment_name);
        setChosenChartImage(fetchedChartImage)
    }

    return (
    <div>
        <h1 className='welcome-prompt'>Witaj {userName()}, o to aktualne statystyki sieci klubów Fitbit</h1>
        <Row>
        <Col md={{ span: 5, offset: 2 }} >
            <ul className='graph-panel'>
                <p className='title-label'>Dostępne statystyki</p>
                <li className='default'>
                    <button className="label" onClick={() => handleChartImage('http://localhost:8000/manager/ticket_popularity_week/')}>
                    Popularność karnetów
                    </button>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => handleChartImage('http://localhost:8000/manager/discount_popularity_week/')}>
                    Popularność promocji
                    </button>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => handleChartImage('http://localhost:8000/manager/age_range/')}>
                    Przedziały wiekowe klientów
                    </button>
                </li>
                <li className="up-label">
                Częstość przychodzenia klientów
                    <li>
                        <button className="sub-label" onClick={() => handleChartImageWithProvidedData('http://localhost:8000/manager/clients_week/', userId())}>
                        1. tygodniowa
                        </button>
                    </li>
                    <li>
                        <button className="sub-label" onClick={() => handleChartImageWithProvidedData('http://localhost:8000/manager/clients_hour/', userId())}>
                        2. dzienna
                        </button>
                    </li>
                </li>
                <li className='default'>
                    <button className="label" onClick={() => handleChartImageWithProvidedData('http://localhost:8000/manager/sessions/', userId())}>
                    Liczba zamówionych sesji u poszczególnych trenerów
                    </button>
                </li>
                <li className='default'>
                <button
                                className="label"
                                onClick={() => handleChartImageWithProvidedDataName('http://localhost:8000/manager/equipment_usage/', userId(), selectedEquipment)}
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
                                {allPossibleEquipment.map((equipment, index) => (
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
                <Card.Img src={`data:image/jpeg;base64,${chosenChartImage}`} alt="W celu wyświetlenia statystyki wybierz ją z listy" />
            </Card>
        </Col>
        </Row>
    </div>
    );
};

export default FitnessClubStatistics;