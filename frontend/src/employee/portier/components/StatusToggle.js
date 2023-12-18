import React, { useState } from 'react';


const StatusToggle = ({ initialStatus }) => {
    const [status, setStatus] = useState(initialStatus);

    const handleActivate = () => {
      if (!status) {
        setStatus(true);
        }
      };
      return (
        <div>
        <p>Status: {status ? 'Aktywny' : 'Nieaktywny'}</p>
        <button onClick={handleActivate} disabled={status}>Activate</button>
        </div>
      );
    };

    export default StatusToggle;