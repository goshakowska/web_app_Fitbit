const checkCartCollision = async (event, week_schedule_id, date, cart) => {
    try {
        const response = await fetch('http://localhost:8000/client/is_collision_in_basket/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ date: date, week_schedule_id: week_schedule_id, basket: cart})});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data)
        return data.is_collision;

      } catch (error) {
        console.error('Error:', error);
      };
}

export default checkCartCollision