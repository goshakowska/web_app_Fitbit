import React, { useState, useEffect } from "react";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowDropUpIcon from '@mui/icons-material/ArrowDropUp';
import '../styles/trainingCreator.css';
import employeeToken from "../../EmployeeToken";
import { useLocation } from 'react-router-dom';

export default function TrainingCreator() {

  // const plannedExercises = [
  //   {
  //     exercise_id: 1,
  //     position: 1,
  //     name: "Pompki",
  //     rep: 5,
  //     duration: null,
  //   },
  //   {
  //     exercise_id: 2,
  //     position: 3,
  //     name: "Plank",
  //     rep: null,
  //     duration: 30,
  //   },
  //   {
  //     exercise_id: 3,
  //     position: 2,
  //     name: "Przysiady",
  //     rep: 20,
  //     duration: null,
  //   },
  // ];

  // const allExercises = [
  //   {
  //     exercise_id: 1,
  //     name: "Pompki",
  //     rep: 5,
  //     duration: null,
  //   },
  //   {
  //     exercise_id: 2,
  //     name: "Plank",
  //     rep: null,
  //     duration: 30,
  //   },
  //   {
  //     exercise_id: 3,
  //     name: "Przysiady",
  //     rep: 20,
  //     duration: null,
  //   },
  //   {
  //     exercise_id: 4,
  //     name: "Pull ups",
  //     rep: 20,
  //     duration: null,
  //   },
  // ]


  //
  const {userId} = employeeToken();
  const location = useLocation();
  const client_id = location.state?.client_id;
  const [exercises, setExercises] = useState([]);
  const [allExercises, setAllExercises] = useState([]);

  const getExercisesForTraining = async (event) =>
  {
    console.log(userId());
    console.log(client_id);
    try {
        const response = await fetch('http://localhost:8000/trainer/incoming_training/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },body: JSON.stringify({ trainer_id: userId(), client_id: client_id })});

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data.training_id);
        console.log(data.exercises);
        setExercises(data.exercises);

      } catch (error) {
        console.error('Error:', error);
      };
}

useEffect(() => {getExercisesForTraining()}, []);

const getAllExercises = async (event) =>
{
  try {
      const response = await fetch('http://localhost:8000/trainer/all_exercises/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },body: JSON.stringify()});

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data.exercises);
      setAllExercises(data.exercises);

    } catch (error) {
      console.error('Error:', error);
    };
}

useEffect(() => {getAllExercises()}, []);


const [selectedExerciseId, setSelectedExerciseId] = useState(null);
const [repInput, setRepInput] = useState("");
const [durationInput, setDurationInput] = useState("");

const [editingExerciseIndex, setEditingExerciseIndex] = useState(null);
const [editingRepInput, setEditingRepInput] = useState("");
const [editingDurationInput, setEditingDurationInput] = useState("");
const [editingExercise, setEditingExercise] = useState(null);

const addExercise = () => {
  const selectedExercise = allExercises.find((exercise) => exercise.exercise_id === selectedExerciseId);
  if (selectedExercise) {
    if ((repInput && !durationInput) || (!repInput && durationInput)) {
      setExercises((prev) => [
        ...prev,
        {
          exercise_id: selectedExercise.exercise_id,
          position: prev.length + 1,
          name: selectedExercise.name,
          rep: repInput ? parseInt(repInput, 10) : null,
          duration: durationInput ? parseInt(durationInput, 10) : null,
        },
      ].sort((a, b) => a.position - b.position));
      setRepInput("");
      setDurationInput("");
    } else {
      alert("Please provide either reps or duration, not both.");
    }
  }
};

const applyEditExercise = () => {
  const selectedExercise = allExercises.find((exercise) => exercise.exercise_id === selectedExerciseId);

  if (!selectedExercise) {
    alert("Please select a valid exercise.");
    return;
  }

  const { rep, duration } = selectedExercise;

  if ((editingRepInput && !editingDurationInput) || (!editingRepInput && editingDurationInput)) {
    setExercises((prev) => {
      const updatedExercises = [...prev];
      updatedExercises[editingExerciseIndex] = {
        exercise_id: selectedExercise.exercise_id,
        position: updatedExercises[editingExerciseIndex].position,
        name: selectedExercise.name,
        rep: editingRepInput !== "" ? parseInt(editingRepInput, 10) : null,
        duration: editingDurationInput !== "" ? parseInt(editingDurationInput, 10) : null,
      };
      return updatedExercises.sort((a, b) => a.position - b.position);
    });

    setSelectedExerciseId(selectedExercise.exercise_id);
    setEditingExercise(null);
    setEditingExerciseIndex(null);
    setEditingRepInput("");
    setEditingDurationInput("");
  } else {
    alert("Please provide either reps or duration, not both.");
  }
};

const discardEditExercise = () => {
  setEditingExercise(null);
  setEditingExerciseIndex(null);
  setEditingRepInput("");
  setEditingDurationInput("");
  setSelectedExerciseId(null);
};

const deleteExercise = (index) => {
  setExercises((prev) => {
    const updatedExercises = prev.filter((exercise, i) => i !== index).sort((a, b) => a.position - b.position);
    return updatedExercises.map((exercise, i) => ({ ...exercise, position: i + 1 }));
  });
};

const moveExercise = (index, direction) => {
  setExercises((prev) => {
    const updatedExercises = [...prev];
    const [movedExercise] = updatedExercises.splice(index, 1);
    const newIndex = direction === "up" ? index - 1 : index + 1;
    updatedExercises.splice(newIndex, 0, movedExercise);
    return updatedExercises.map((exercise, i) => ({ ...exercise, position: i + 1 }));
  });
};

useEffect(() => {
  setExercises((prev) => prev.map((exercise, i) => ({ ...exercise, position: i + 1 })));
}, []);

return (
  <div>
    <h1 className="big-title" >Zaplanuj trening</h1>
    <table className="table">
      <thead>
        <tr>
          <th className="column-name">Nr.</th>
          <th className="column-name">Ćwiczenie</th>
          <th className="column-name">Powtórzenia</th>
          <th className="column-name">Czas</th>
          <th className="column-name">Akcje</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td className="table-data"></td>
          <td className="table-data">
            <select className="select"
              onChange={(e) => setSelectedExerciseId(parseInt(e.target.value, 10))}
              value={selectedExerciseId || ""}>
              <option className="option" value="" disabled>
                Wybierz ćwiczenie
              </option>
              {allExercises.map((ex) => (
                <option className="option-to-choose" key={ex.exercise_id} value={ex.exercise_id} disabled={!ex.rep && !ex.duration}>
                  {ex.name}
                </option>
              ))}
            </select>
          </td>
          <td className="table-data">
            <input className="input"
              type="text-input"
              onChange={(e) => setRepInput(e.target.value)}
              value={repInput}
              disabled={selectedExerciseId !== null && allExercises.find((ex) => ex.exercise_id === selectedExerciseId)?.rep === null}
            />
          </td>
          <td className="table-data">
            <input className="input"
              type="text-input"
              onChange={(e) => setDurationInput(e.target.value)}
              value={durationInput}
              disabled={selectedExerciseId !== null && allExercises.find((ex) => ex.exercise_id === selectedExerciseId)?.duration === null}
            />
          </td>
          <td className="table-data">
            <button className="button-modifier" onClick={addExercise}>Dodaj</button>
          </td>
        </tr>
        {exercises.map((exercise, index) => (
          <tr key={index}>
            <td className="table-data">{exercise.position}</td>
            <td className="table-data">
              {editingExerciseIndex === index ? (
                <select className="select"
                  value={selectedExerciseId || ""}
                  onChange={(e) => {
                    const newExerciseId = parseInt(e.target.value, 10);
                    setSelectedExerciseId(newExerciseId);

                    const newExercise = allExercises.find((ex) => ex.exercise_id === newExerciseId);
                    setEditingExercise(newExercise);

                    setEditingRepInput("");
                    setEditingDurationInput("");
                  }}
                >
                  <option className="option" value="" disabled>
                    Wybierz ćwiczenie
                  </option>
                  {allExercises.map((ex) => (
                    <option className="option-to-choose" key={ex.exercise_id} value={ex.exercise_id} disabled={!ex.rep && !ex.duration}>
                      {ex.name}
                    </option>
                  ))}
                </select>
              ) : (
                exercise.name
              )}
            </td>
            <td className="table-data">
              {editingExerciseIndex === index ? (
                <input className="input"
                  type="text"
                  onChange={(e) => setEditingRepInput(e.target.value)}
                  value={editingRepInput}
                  disabled={editingExercise !== null && editingExercise.rep === null}
                />
              ) : (
                exercise.rep
              )}
            </td>
            <td className="table-data">
              {editingExerciseIndex === index ? (
                <input className="input"
                  type="text"
                  onChange={(e) => setEditingDurationInput(e.target.value)}
                  value={editingDurationInput}
                  disabled={editingExercise !== null && editingExercise.duration === null}
                />
              ) : (
                exercise.duration
              )}
            </td>
            <td className="table-data">
              {editingExerciseIndex === index ? (
                <>
                  <button className="button-modifier" onClick={applyEditExercise}>Zastosuj</button>
                  <button className="button-modifier" onClick={discardEditExercise}>Odrzuć</button>
                </>
              ) : (
                <>
                  <button className="button-modifier" onClick={() => setEditingExerciseIndex(index)}>Edytuj</button>
                  <button className="button-modifier" onClick={() => deleteExercise(index)}>Usuń</button>
                  <ArrowDropUpIcon className="arrow" onClick={() => moveExercise(index, "up")} disabled={index === 0} />
                  <ArrowDropDownIcon className="arrow" onClick={() => moveExercise(index, "down")} disabled={index === exercises.length - 1} />
                </>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);
}