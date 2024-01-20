const allEquipment = async (manager_id) => {
    try {
        const response = await fetch('http://localhost:8000/manager/all_equipment/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },body: JSON.stringify({ manager_id: manager_id })});

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          console.log(data.names);
        return data.names

        } catch (error) {
          console.error('Error:', error);
    }
}

export default allEquipment