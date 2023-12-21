import React, { useState } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import 'moment/locale/en-gb';
import events from "./SampleEvents";
import "react-big-calendar/lib/css/react-big-calendar.css";
import "../styles/scheduler.css";

moment.locale("en-GB");
const localizer = momentLocalizer(moment);

export default function ReactBigCalendar() {
  const [eventsData, setEventsData] = useState(events);

  const handleSelect = ({ start, end }) => {
    console.log(start);
    console.log(end);
    const title = window.prompt("Dodaj nowy trening do kalendarza");
    if (title)
      setEventsData([
        ...eventsData,
        {
          start,
          end,
          title
        }
      ]);
  };
  return (
    <div className="Calendar">
      <Calendar className="trainer-calendar"
        views={["day", "agenda", "week", "month"]}
        selectable
        localizer={localizer}
        defaultDate={new Date()}
        min={new Date(0, 0, 0, 8, 0, 0)} // 8 am
        max={new Date(0, 0, 0, 21, 0, 0)} // 9 pm
        defaultView="week"
        events={eventsData}
        style={{ height: "100vh" }}
        onSelectEvent={(event) => alert(event.title)}
        onSelectSlot={handleSelect}
      />
    </div>
  );
}