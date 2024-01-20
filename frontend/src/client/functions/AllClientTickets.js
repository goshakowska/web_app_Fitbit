const getClientTickets = async (event, client_id) => {
  // function returns client's all tickets
    try {
        const response = await fetch('http://localhost:8000/client/gym_tickets_history/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: client_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getClientTickets