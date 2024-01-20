const getTicketDetails = async (event, ticket_id) => {
    // returns details about client's ticket
    try {
        const response = await fetch('http://localhost:8000/client/gym_tickets_details/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ ticket_id: ticket_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getTicketDetails