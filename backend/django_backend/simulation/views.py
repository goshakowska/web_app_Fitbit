from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import simulation.database as database

# Create your views here.

@csrf_exempt
def clients_list(request):
    clients = database.get_all_clients()
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
def trainers_list(request):
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    trainers = database.get_trainers_by_gym(gym_id)
    return JsonResponse({'trainers': trainers})


@csrf_exempt
def test_connection(request):
    data = json.loads(request.body.decode('utf-8'))
    message = data.get('message')
    return JsonResponse({'message': "We are connected"})

@csrf_exempt
def insert_exercise_history(request):
    data = json.loads(request.body.decode('utf-8'))
    exercise_date = data.get('exercise_date')
    duration = data.get('duration')
    repetitions_number = data.get('repetitions_number')
    gym_id = data.get('gym_id')
    exercise_id = data.get('exercise_id')
    trainer_id = data.get('trainer_id')
    client_id = data.get('client_id')
    calories = data.get('calories')
    params = data.get('params')
    exercise_history_id = database.insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, trainer_id, client_id, calories)
    return JsonResponse({'message': "We are connected"})