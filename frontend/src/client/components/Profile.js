import React, { useState, useEffect } from 'react';
import clientToken from '../ClientToken.js';
import getClientData from '../functions/ClientProfileData.js';
import '../styles/profileStyles.css'
import moment from 'moment';

function Profile() {
    // shows user profile
    const {userId} = clientToken();
    const [clientData, setClientData] = useState([])

    const clientProfileData = async (event) => {
        // get client data
            const data = await getClientData(event, userId());
            setClientData(data.client_data)
    }
    
    // get data on site render
    useEffect(() => {clientProfileData()}, []);

    return (
        <div className="ticketsShop">
            <h className="textLogin">{clientData["name"]} {clientData["surname"]}</h>
            <div className="gridContainer textStyleProfile">
                <div className='leftColumn '>
                    <p className='text-style'>TWOJE DANE</p>
                    <p>Login: {clientData["login"]}</p>
                    <p>Adres e-mail: {clientData["email"]}</p>
                    <p>Data urodzenia: {moment(clientData["birth_year"]).format('DD.MM.YYYY')}</p>
                    <p>Numer telefonu: {clientData["phone_number"]}</p>
                    {clientData["gender"] === 'K' ? <p bold>Płeć: kobieta</p> : <p>Płeć: mężczyzna</p> }
                    {clientData["current_weight"] ? <p bold>Waga: {clientData["current_weight"]} kg</p> : <p>Waga: - </p> }
                    {clientData["height"] ? <p bold>Wzrost: {clientData["height"]} cm</p> : <p>Wzrost: - </p> }
                    </div>

                    <div className='separator'></div>
                    <div className='rightColumn'>
                        <p className='text-style'>TWOJE CELE</p>
                        {clientData["target_weight"] ? <p>Docelowa waga: {clientData["target_weight"]} kg</p> : <p> - </p> }
                        {clientData["training_goal"] ? <p>Cel treningu: {clientData["training_goal"]}</p> : <p> - </p> }
                        {clientData["advancement"] ? <p>Poziom zaawansowania: {clientData["advancement"]}</p> : <p> - </p> }
                        {clientData["training_frequency"] ? <p>Planowana liczba treningów w tygodniu: {clientData["training_frequency"]}</p> : <p> - </p> }
                        {clientData["training_time"] ? <p>Szacowany czas trwania treningu: {clientData["training_time"]} min</p> : <p> - </p> }
                    </div>
                    </div>
                </div>

    )
}

export default Profile;