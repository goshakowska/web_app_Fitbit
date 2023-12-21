const getClassesList = async (event, clubId) => {
    try {
        const response = await fetch('http://localhost:8000/client/gym_classes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ gym_id: clubId})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.classes

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getClassesList;