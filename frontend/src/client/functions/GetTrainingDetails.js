const getTrainingDetailsList = async (event, training_id) => {
  // returns client's exercises done during given training
    try {
        const response = await fetch('http://localhost:8000/client/trening_details/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ training_id: training_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getTrainingDetailsList