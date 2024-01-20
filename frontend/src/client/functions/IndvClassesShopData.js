const getIndvClasses = async (e, trainer_id, date, user_id) => {
    // returns individual classes for given trainer and week & returns collisions with client's ordered classes
    try {
        const response = await fetch('http://localhost:8000/client/free_trainings/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({  trainer_id: trainer_id,
                                  start_date: date,
                                  client_id: user_id,
                                  }),
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

    export default getIndvClasses