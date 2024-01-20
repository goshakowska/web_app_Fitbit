const deleteTicket = async (event, ticket_id) => {
    // deletes unactivated, ordered client's ticket
    try {
        const response = await fetch('http://localhost:8000/client/delete_gym_ticket/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ gym_ticket_id: ticket_id})});
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

      } catch (error) {
        console.error('Error:', error);
      };
}

export default deleteTicket