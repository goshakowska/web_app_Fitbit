import React, { useState, useEffect } from 'react';
import { useLocation } from "react-router-dom";
import { Table } from 'reactstrap';
import getTrainersList from '../functions/TrainersList';
import getClassesList from '../functions/ClassesList';
import '../styles/tablesStyle.css';

function FitnessClubDetails () {
    // show workers and classes for a particular fitness club
    const location = useLocation();
    const club_id = location.state.clubId;
    const club_name = location.state.clubName;
    const [clubTrainers, setClubTrainers] = useState([])
    const [clubClasses, setClubClasses] = useState([])

    const getTrainers = async (event, club_id) => {
    // get trainers working at the club
        const trainers = await getTrainersList(event, club_id);
        setClubTrainers(trainers);
    }

    const getClasses = async (event, club_id) => {
    // get classes taking place at the fitness club
        const classes = await getClassesList(event, club_id);
        setClubClasses(classes);
    }

    // get data on site render
    useEffect((e) => {getTrainers(e, club_id)}, []);
    useEffect((e) => {getClasses(e, club_id)}, []);


    return (
        <div className='ticketsShop'>
            <h className='textLogin'>Poznaj ofertę siłowni {club_name}</h>
        <div className='gridDesign'>
            <div>
            <h className="textLogin2"> Nasza załoga </h>
            <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
                <tbody>
            {clubTrainers.length > 0 && clubTrainers.map((trainer, index) => (
                <tr>
                <td  key={index}>{trainer[1]} {trainer[2]}</td></tr>
            ))}</tbody></Table>
        </div>
        <div>
        <h className="textLogin2"> Nasze zajęcia </h>
        <Table bordered hover responsive className="tableDesign tableDesignNarrow" >
                <tbody>
            {clubClasses.length > 0 && clubClasses.map((clubclass, index) => (
                <tr>
                <td key={index}> {clubclass[1]} </td></tr>
            ))}</tbody> </Table>
        </div></div></div>
    )
}

export default FitnessClubDetails;