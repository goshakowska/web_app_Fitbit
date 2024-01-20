import React, { useContext } from "react";
import WeekSwitcherContext from "../context/WeekSwitcherContext";



function WeekSwitcher () {
    // create week switcher component for simple week changing in shops & client's classes
    const {weekBoundaries, handleNext, handlePrev} = useContext(WeekSwitcherContext)
    return (
        <div className="weekSwitchLayout">
        <div className="weekSwitch text-style"> {weekBoundaries.startOfWeek.toLocaleDateString()}-{weekBoundaries.endOfWeek.toLocaleDateString()} </div>
        <div>
        <button className="weekSwitch text-style" onClick={handlePrev}>Poprzedni tydzień</button>
        <button className="weekSwitch text-style" onClick={handleNext}>Następny tydzień</button>
        </div></div>
    )
}

export default WeekSwitcher;