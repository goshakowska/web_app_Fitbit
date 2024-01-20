const getDiscountTickets = async (event) => {
  // returns all discount tickets
    try {
        const response = await fetch('http://localhost:8000/client/discount_gym_ticket_offer/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          }});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getDiscountTickets