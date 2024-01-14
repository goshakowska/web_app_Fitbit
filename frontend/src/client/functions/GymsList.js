const getGymsList = async (event) => {
    try {
        const response = await fetch('http://localhost:8000/client/gyms_list/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          }});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.gyms

      } catch (error) {
        console.error('Error:', error);
      };
}

export default getGymsList