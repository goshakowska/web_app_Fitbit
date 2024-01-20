
const getCancelClass = async (event, class_id) => {
    // cancels already ordered class
        try {
            const response = await fetch('http://localhost:8000/client/cancel_ordered_gym_classe/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },body: JSON.stringify({ ordered_gym_classe_id: class_id})});

            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            return data

          } catch (error) {
            console.error('Error:', error);
          };
    }

export default getCancelClass