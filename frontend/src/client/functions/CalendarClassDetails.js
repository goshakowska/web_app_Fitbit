const getCalendarClassDetails = async (event, class_id, date) => {
  // returns details for class in shop
    try {
        const response = await fetch('http://localhost:8000/client/free_gym_classe_details/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ date: date, gym_classe_id: class_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.details;

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getCalendarClassDetails