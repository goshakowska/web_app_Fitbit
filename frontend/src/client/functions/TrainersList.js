const getTrainersList = async (event, clubId) => {
  // returns all trainers who work at given club
    try {
        const response = await fetch('http://localhost:8000/client/gym_trainers/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ gym_id: clubId})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data.trainers)
        return (data.trainers)

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getTrainersList;