const getGroupClasses = async (e, gym_id, user_id, date) => {
  // returns group classes for given gym and week & returns collisions with client's ordered classes
    try {
        const response = await fetch('http://localhost:8000/client/free_gym_classes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({  gym_id: gym_id,
                                  client_id: user_id,
                                  start_date: date}),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data

      } catch (error) {
        console.error('Error:', error);
      }
    };

export default getGroupClasses