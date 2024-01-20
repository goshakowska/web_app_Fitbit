const buyCart = async (event, client_id, reserved_gym_classes, gym_tickets) => {
    // function buys all items in cart and adds them to the client's classes and the client's tickets
    try {
        const response = await fetch('http://localhost:8000/client/buy_items_from_busket/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: client_id, reserved_gym_classes: reserved_gym_classes, gym_tickets: gym_tickets})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default buyCart