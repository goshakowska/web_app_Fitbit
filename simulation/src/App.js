import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [gyms, setGyms] = useState([]);
  const [clients, setClients] = useState([]);
  const [exercises, setExercises] = useState([]);
  const [equipments, setEquipments] = useState([]);

  const [selectedGym, setSelectedGym] = useState(null);
  const [selectedClient, setSelectedClient] = useState(null);
  const [selectedExercise, setSelectedExercise] = useState(null);
  const [selectedEquipment, setSelectedEquipment] = useState(null);
  const [selectedParams, setSelectedParams] = useState([]);

  const [endTime, setEndTime] = useState(new Date());
  const [duration, setDuration] = useState('');
  const [repetitionsNumber, setRepetitionsNumber] = useState('');
  const [calories, setCalories] = useState('');
  const [weight, setWeight] = useState('');
  const [distance, setDistance] = useState('');
  const [height, setHeight] = useState('');



  useEffect(() => {
    const fetchData = async () => {
      try {
        const gymsResponse = await fetch('http://localhost:8000/simulation/all_gyms/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },

        });

        if (!gymsResponse.ok) {
          throw new Error(`HTTP error! Status: ${gymsResponse.status}`);
        }

        const data = await gymsResponse.json();
        setGyms(data.gyms);

        const exercisesResponse = await fetch('http://localhost:8000/simulation/all_exercises/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },

        });

        if (!exercisesResponse.ok) {
          throw new Error(`HTTP error! Status: ${exercisesResponse.status}`);
        }

        const data2 = await exercisesResponse.json();

        setExercises(data2.exercises);

      } catch (error) {
        console.error('Error:', error);
      };
    };

    fetchData();
  }, []);

  const handleGymClick = async (gymId) => {
    setSelectedGym(gymId);

    try {
      const clientsResponse = await fetch('http://localhost:8000/simulation/all_clients/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ gym_id: gymId}),

        });
      if (!clientsResponse.ok) {
          throw new Error(`HTTP error! Status: ${clientsResponse.status}`);
        }

      const data = await clientsResponse.json();
      setClients(data.clients);

      if (selectedExercise) {
        handleExerciseClick(selectedExercise, selectedParams, gymId)
      }

    } catch (error) {
      console.error('Error fetching clients:', error);
    }
  };

  const handleClientClick = (clientId) => {
    setSelectedClient(clientId);
  };

  const handleExerciseClick = async (exerciseId, params=[], gymId=null) => {

    if(!selectedExercise){
    setSelectedParams([]);
    params.forEach(([id, name]) => {
      setSelectedParams((prevSelectedParams) => [...prevSelectedParams, id]);
    })}
    setSelectedExercise(exerciseId);

    let gym = null
    if (gymId){
      gym = gymId
    }
    else{
      gym = selectedGym
    }

    if (gym){
      try {
        const equipmentsResponse = await fetch('http://localhost:8000/simulation/all_equipments/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ gym_id: gym, exercise_id: exerciseId,}),

        });

        if (!equipmentsResponse.ok) {
          throw new Error(`HTTP error! Status: ${equipmentsResponse.status}`);
        }
        const data = await equipmentsResponse.json();
        setEquipments(data.equipments);

      } catch (error) {
        console.error('Error fetching equipments:', error);
      }
    }
  };

  const handleEquipmentClick = (equipmentId) => {
    setSelectedEquipment(equipmentId);
  };





  const sendToDatabase = () => {
    if (!selectedGym || !selectedClient || !selectedExercise) {
      showDialog('Najpierw wybierz ćwiczenie, klienta i siłownię');
    } else if (equipments.length > 0 && !selectedEquipment) {
      showDialog('Najpierw wybierz urządzenie');
    } else {
      setEndTime(new Date());
      const startTime = new Date(endTime - duration*1000);

      const formattedStartTime = new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false,
      }).format(startTime);
      const [datePart, timePart] = formattedStartTime.split(", ");
      const [month, day, yearTime] = datePart.split("/");
      const formattedDate = `${yearTime}-${month}-${day} ${timePart}`;

      const params = {};
      if (selectedParams.includes(1)) {
        params[1] = weight;
      }
      if (selectedParams.includes(2)) {
        params[2] = distance;
      }
      if (selectedParams.includes(3)) {
        params[3] = height;
      }


      fetch('http://localhost:8000/simulation/insert_exercise_history/', {
        method: 'POST',
        body: JSON.stringify({
          "exercise_date": formattedDate,
          "duration": duration,
          "repetitions_number": repetitionsNumber,
          "gym_id": selectedGym,
          "exercise_id": selectedExercise,
          "equipment_id": selectedEquipment,
          "client_id": selectedClient,
          "calories": calories,
          "params": params
         }),
        headers: { 'Content-Type': 'application/json' }
      })
      console.log("exercise_date", formattedDate)
      console.log("duration", duration)
      console.log("repetitions_number", repetitionsNumber)
      console.log("gym_id", selectedGym)
      console.log("exercise_id", selectedExercise)
      console.log("equipment_id", selectedEquipment)
      console.log("client_id", selectedClient)
      console.log("calories", calories)
      console.log("params", params)

      showDialog('Dodano ćwiczenie');
      clear();
    }
  };



  const showDialog = (message) => {
    alert(message);
  };

  const clear = () => {
    setDuration('');
    setRepetitionsNumber('');
    setCalories('');
    setDistance('');
    setWeight('');
    setHeight('');
    setSelectedGym(null);
    setSelectedClient(null);
    setSelectedExercise(null);
    setSelectedEquipment(null);
    setSelectedParams([]);
    setEquipments([])
    setClients([])
  };



  return (
    <div className='bg-gray-100'>
    <div className="flex flex-wrap  p-8 grid grid-cols-2 gap-4">

      <div className="p-4 border-2 bg-white rounded  w-[40vw]">
        <h2 className="text-2xl font-bold mb-4">Ćwiczenia</h2>
        <ul className="list-decimal overflow-auto h-[30vh]">
          {exercises.map((exercise) => (
            <li className={`pl-4 text-lg cursor-pointer ${exercise.id === selectedExercise ? 'bg-blue-200' : 'hover:bg-gray-200'}`}
              key={exercise.id} onClick={() => handleExerciseClick(exercise.id, exercise.parameters)}
            >
              {exercise.name}{" "}
                {exercise.parameters.length !== 0 && (
                  <>
                    {"("}{" "}
                    {exercise.parameters.map(([id, name]) => {
                      return name;
                    }).join(", ")}
                    {" "}{")"}
                  </>
                )}
            </li>
          ))}
        </ul>
      </div>

      <div className="w-1/2 p-4 bg-white border-2 rounded w-[40vw]">
      <h2 className="text-2xl font-bold mb-4">Siłownie</h2>
        <ul className="list-decimal overflow-auto h-[30vh]">
          {gyms.map((gym) => (
            <li className={`pl-4 text-lg cursor-pointer ${gym[0] === selectedGym ? 'bg-blue-200' : 'hover:bg-gray-200'}`}
              key={gym[0]} onClick={() => handleGymClick(gym[0])}
            >
              {gym[1]}
            </li>
          ))}
        </ul>
      </div>


      <div className="w-1/2 p-4  bg-white border-2 rounded w-[40vw]">
        <h2 className="text-2xl font-bold mb-4">Sprzęty</h2>
        <ul className="list-decimal overflow-auto h-[30vh]">
          {equipments.map((equipment) => (
            <li className={`pl-4 text-lg cursor-pointer ${equipment[0] === selectedEquipment ? 'bg-blue-200' : 'hover:bg-gray-200'}`}
              key={equipment[0]} onClick={() => handleEquipmentClick(equipment[0])}
            >
              {equipment[1]} id: {equipment[0]}
            </li>
          ))}
        </ul>
      </div>


      <div className="w-1/2 p-4 bg-white border-2 rounded w-[40vw]">
        <h2 className="text-2xl font-bold mb-4">Klienci</h2>
        <ul className="list-decimal overflow-auto h-[30vh]">
          {clients.map((client) => (
            <li className={`pl-4 text-lg cursor-pointer ${client[0] === selectedClient ? 'bg-blue-200' : 'hover:bg-gray-200'}`}
              key={client[0]} onClick={() => handleClientClick(client[0])}
            >
              {client[1]} {client[2]}
            </li>
          ))}
        </ul>
      </div>
      </div>

      <div className="flex flex-row w-[70vw] p-10">
        <div className="grid grid-cols-3 gap-4 w-full">
          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Czas trwania w sekundach
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={duration}
              onChange={(e) => {
                if (isNaN(e.target.value)){setDuration(''); return}
                setDuration(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded "
            />
          </div>

          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Liczba powtórzeń
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={repetitionsNumber}
              onChange={(e) => {
                if (isNaN(e.target.value)){setRepetitionsNumber(''); return}
                setRepetitionsNumber(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded"
            />
          </div>

          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Kalorie
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={calories}
              onChange={(e) => {
                if (isNaN(e.target.value)){setCalories(''); return}
                setCalories(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded"
            />
          </div>

          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Dystans w metrach
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={distance}
              onChange={(e) => {
                if (isNaN(e.target.value)){setDistance(''); return}
                setDistance(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded"
            />
          </div>

          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Obciążenie w kilogramach
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={weight}
              onChange={(e) => {
                if (isNaN(e.target.value)){setWeight(''); return}
                setWeight(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded"
            />
          </div>

          <div className='flex flex-col ml-4 mr-4'>
            <label className='mb-2 text-lg'>
              Wysokość w centymetrach
            </label>
            <input
              type="numeric"
              pattern="[0-9]*"
              value={height}
              onChange={(e) =>
                {if (isNaN(e.target.value)){setHeight(''); return}
                setHeight(Number(e.target.value))}}
              className="col-span-1 p-2 border rounded"
            />
          </div>
        </div>

        {/* Przycisk po prawej stronie */}
        <button className="self-center p-4 ml-10 border rounded bg-gray-200 hover:bg-gray-300"
          onClick={() => sendToDatabase()}
        >
          Prześlij dane do bazy
        </button>
      </div>



    </div>







  );
};

export default App;
