const bookCart = async (event, client_id, cartClasses) => {
    try {
        const response = await fetch('http://localhost:8000/client/reserve_gym_classes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: client_id, gym_classes: cartClasses} )});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data;

      } catch (error) {
        console.error('Error:', error);
      };
}

export default bookCart