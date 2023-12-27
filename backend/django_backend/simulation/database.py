import database_models.models as models

def get_all_clients(gym_id):
    gym_visits = models.GymVisit.objects.filter(departure_time=None, gym_gym__gym_id=gym_id)
    clients = []
    for visit in gym_visits:
        client = visit.client_user
        clients.append([client.client_id, client.name, client.surname])
    return clients

def get_all_gyms():
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name] for gym in gyms]
    return gyms

def get_all_exercises():
    exercises = models.Exercise.objects.all()
    exercises_list = []
    for exercise in exercises:
        item = {
            'id': exercise.exercise_id,
            'name': exercise.name
            }
        parameter_values = models.StandardParameterValue.objects.filter(exercise__exercise_id=exercise.exercise_id)
        if parameter_values:
            parameters = [[parameter.parameter.parameter_id, parameter.parameter.name]for parameter in parameter_values]
            item.update({'parameters': parameters})
        exercises_list.append(item)
    return exercises_list

def get_equipments_by_gym_and_exercise(gym_id, exercise_id):
    try:
        equipment_id = models.Exercise.objects.get(exercise_id=exercise_id).equipment.equipment_id
    except Exception:
        return []
    if equipment_id:
        equipments = models.GymEquipment.objects.filter(gym__gym_id=gym_id, equipment_id=equipment_id)
        equipments = [[equipment.gym_equipment_id, equipment.equipment.name] for equipment in equipments]
    return equipments

def insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories):
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
    print(params)
    for param, value in params.items():
        new_history_param = models.ExerciseHistoryParamValue(
            value=value,
            parameter_id=param,
            exercise_history_id=exercise_history_id
        )
        new_history_param.save()