import React from "react";

const EventSlot = ({ event }) => {
    if (!event) {
       return <td />;
    }

    return (
       <td>
         <a href={event.url} target="_blank" rel="noreferrer" className="event-link">
           {event.name}
         </a>
       </td>
    );
   };

export default EventSlot;