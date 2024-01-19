import database_models.models as models

def get_all_clients(gym_id):
    """
    Get a list of all clients currently present in a specific gym.

    Args:
        gym_id (int): The unique identifier of the gym.

    Returns:
        list: A list of lists containing client information [client_id, name, surname].
    """
    gym_visits = models.GymVisit.objects.filter(departure_time=None, gym_gym__gym_id=gym_id)
    clients = []
    for visit in gym_visits:
        client = visit.client_user
        clients.append([client.client_id, client.name, client.surname])
    return clients

def get_all_gyms():
    """
    Get a list of all gyms.

    Returns:
        list: A list of lists containing gym information [gym_id, name].
    """
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name] for gym in gyms]
    return gyms

def get_all_exercises():
    """
    Get a list of all exercises along with their parameters.

    Returns:
        list: A list of dictionaries containing exercise information,
              including exercise ID, name, and a list of parameters with their IDs and names.
    """
    exercises = models.Exercise.objects.all()
    exercises_list = []
    for exercise in exercises:
        item = {
            'id': exercise.exercise_id,
            'name': exercise.name,
            'parameters': []
            }
        parameter_values = models.StandardParameterValue.objects.filter(exercise__exercise_id=exercise.exercise_id)
        if parameter_values:
            parameters = [[parameter.parameter.parameter_id, parameter.parameter.name]for parameter in parameter_values]
            item['parameters'] =  parameters
        exercises_list.append(item)
    return exercises_list

def get_equipments_by_gym_and_exercise(gym_id, exercise_id):
    """
    Get a list of equipments available in a specific gym for a given exercise.

    Args:
        gym_id (int): The unique identifier of the gym.
        exercise_id (int): The unique identifier of the exercise.

    Returns:
        list: A list of lists containing equipment information [gym_equipment_id, equipment_name].
    """
    try:
        equipment_id = models.Exercise.objects.get(exercise_id=exercise_id).equipment.equipment_id
    except Exception:
        return []
    if equipment_id:
        equipments = models.GymEquipment.objects.filter(gym__gym_id=gym_id, equipment_id=equipment_id)
        equipments = [[equipment.gym_equipment_id, equipment.equipment.name] for equipment in equipments]
    return equipments

def insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories):
    """
    Insert exercise history into the database.

    Args:
        exercise_date (datetime): The date of the exercise.
        duration (int): The duration of the exercise in minutes.
        repetitions_number (int): The number of repetitions performed.
        gym_id (int): The unique identifier of the gym.
        exercise_id (int): The unique identifier of the exercise.
        equipment_id (int): The unique identifier of the equipment used.
        client_id (int): The unique identifier of the client.
        calories (float): The calories burned during the exercise.

    Returns:
        int: The unique identifier of the inserted exercise history record.
    """
    new_history_exercise = models.ExerciseHistory(
        exercise_date=exercise_date,
        duration=duration,
        repetitions_number=repetitions_number,
        gym_id=gym_id,
        exercise_id=exercise_id,
        client_id=client_id,
        calories=calories,
        gym_equipment_id=equipment_id
    )
    new_history_exercise.save()
    return new_history_exercise.exercise_history_id

def insert_params_history(exercise_history_id, params):
    """
    Insert parameter values for an exercise history into the database.

    Args:
        exercise_history_id (int): The unique identifier of the exercise history record.
        params (dict): A dictionary containing parameter IDs as keys and their corresponding values.

    Returns:
        None
    """
    for param, value in params.items():
        new_history_param = models.ExerciseHistoryParamValue(
            value=value,
            parameter_id=param,
            exercise_history_id=exercise_history_id
        )
        new_history_param.save()