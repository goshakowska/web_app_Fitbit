import React, { useState, useEffect } from 'react';
import { useLocation } from "react-router-dom";
import getTrainersList from '../functions/TrainersList';
import getClassesList from '../functions/ClassesList';
import '../styles/tablesStyle.css';

function FitnessClubDetails () {
    const location = useLocation();
    const club_id = location.state.clubId;
    const club_name = location.state.clubName;
    const [clubTrainers, setClubTrainers] = useState([])
    const [clubClasses, setClubClasses] = useState([])

    const getTrainers = async (event, club_id) => {
        const trainers = await getTrainersList(event, club_id);
        setClubTrainers(trainers);
    }

    const getClasses = async (event, club_id) => {
        const classes = await getClassesList(event, club_id);
        setClubClasses(classes);
    }

    useEffect((e) => {getTrainers(e, club_id)}, []);
    useEffect((e) => {getClasses(e, club_id)}, []);


    return (
        <div className='gridDesign'>
            <div>
            {clubTrainers.length > 0 && clubTrainers.map((trainer, index) => (
                <p key={index}>{trainer[1]} {trainer[2]}</p>
            ))}
        </div>
        <div>
            {clubClasses.length > 0 && clubClasses.map((clubclass, index) => (
                <p key={index}> {clubclass[1]} </p>
            ))}
        </div></div>
    )
}

export default FitnessClubDetails;