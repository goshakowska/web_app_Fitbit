const handleSendNumber = async () => {
    try {
      const response = await fetch('http://localhost:8000/registration/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ login: 'originalNumber',
                                password_hash: 'hash',
                                email: 'email',
                                phone_number: '123123123',
                                name: 'Adam',
                                surname: 'Programista',
                                gender: 'M',
                                height: 155,
                                birth_year: '2000-01-01',
                                advancement: 'zaawansowany',
                                target_weight: 55,
                                training_frequency: 1,
                                training_time: 60,
                                training_goal_id: 1,
                                gym_id: 1 }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setModifiedNumber(data.login);
    } catch (error) {
      console.error('Error:', error);
    }
  };