const getClassDetails = async (event, class_id) => {
    try {
        const response = await fetch('http://localhost:8000/client/ordered_classe_details/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ classe_id: class_id})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.details;

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getClassDetails