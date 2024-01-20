const getClientClasses = async (e, user_id, date) => {
    try {
        const response = await fetch('http://localhost:8000/client/ordered_classes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ client_id: user_id,
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

    export default getClientClasses