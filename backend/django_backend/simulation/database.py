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

def get_trainers_by_gym(gym_id):
    trainers = models.Employee.objects.filter(type='trener', gym__gym_id=gym_id)
    trainers = [[trainer.employee_id, trainer.name, trainer.surname]for trainer in trainers]
    return trainers

def insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, trainer_id, client_id, calories):
    new_history_exercise = models.ExerciseHistory(
        exercise_date=exercise_date,
        duration=duration,
        repetitions_number=repetitions_number,
        gym_id=gym_id,
        exercise_id=exercise_id,
        trainer_id=trainer_id,
        client_id=client_id,
        calories=calories
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