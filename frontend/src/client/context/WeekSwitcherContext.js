import React, {createContext, useState} from "react";

const WeekSwitcherContext = createContext({})

export const WeekSwitcherProvider = ({ children }) => {
  // create context for week switcher
    const [weekBoundaries, setWeekBoundaries] = useState(getWeekBoundaries(new Date()));

    function getWeekBoundaries(day) {
        const dayOfWeek = day.getDay();

        const startOfWeek = new Date(day);
        startOfWeek.setDate(day.getDate() - (dayOfWeek));

        const endOfWeek = new Date(day);
        endOfWeek.setDate(day.getDate() + (6 - (dayOfWeek)));

        return {
          startOfWeek,
          endOfWeek
        };
      }

      const handleNext = () => {
        // show next week
        const nextWeekStart = new Date(weekBoundaries.endOfWeek);
        nextWeekStart.setDate(nextWeekStart.getDate() + 1);
        setWeekBoundaries(getWeekBoundaries(nextWeekStart))   }

    const handlePrev = () => {
      // show prevoius week
            const prevWeekEnd = new Date(weekBoundaries.startOfWeek);
            prevWeekEnd.setDate(prevWeekEnd.getDate() - 1);
            setWeekBoundaries(getWeekBoundaries(prevWeekEnd))
    }

    function formatDate(date) {
      // return date in correct format for database
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
      }

    return(
        <WeekSwitcherContext.Provider value={{weekBoundaries, handlePrev, handleNext, formatDate}}>
            {children}
        </WeekSwitcherContext.Provider>
    )
}

export default WeekSwitcherContext;