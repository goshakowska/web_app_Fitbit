from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import simulation.database as database

# Create your views here.

@csrf_exempt
def clients_list(request):
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    clients = database.get_all_clients(gym_id)
    return JsonResponse({'clients': clients})

@csrf_exempt
def gyms_list(request):
    gyms = database.get_all_gyms()
    return JsonResponse({'gyms': gyms})

@csrf_exempt
def exercises_list(request):
    exercises = database.get_all_exercises()
    return JsonResponse({'exercises': exercises})

@csrf_exempt
def equipments_list(request):
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    exercise_id = data.get('exercise_id')
    equipments = database.get_equipments_by_gym_and_exercise(gym_id, exercise_id)
    return JsonResponse({'equipments': equipments})

@csrf_exempt
def insert_exercise_history(request):
    data = json.loads(request.body.decode('utf-8'))
    exercise_date = data.get('exercise_date')
    duration = data.get('duration')
    repetitions_number = data.get('repetitions_number')
    gym_id = data.get('gym_id')
    exercise_id = data.get('exercise_id')
    equipment_id = data.get('equipment_id')
    client_id = data.get('client_id')
    calories = data.get('calories')
    params = data.get('params')
    exercise_history_id = database.insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories)
    if params:
        database.insert_params_history(exercise_history_id, params)
    return JsonResponse({'message': "Insert successful"})