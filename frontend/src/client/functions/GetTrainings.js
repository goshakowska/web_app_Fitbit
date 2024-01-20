const getTrainingsList = async (event, user_id) => {
  // returns all clients trainings
    try {
        const response = await fetch('http://localhost:8000/client/client_trenings/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ client_id: user_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getTrainingsList