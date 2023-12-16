import database_models.models as models

def get_all_clients():
    clients = models.Client.objects.all()
    clients = [[client.client_id, client.name, client.surname] for client in clients]
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