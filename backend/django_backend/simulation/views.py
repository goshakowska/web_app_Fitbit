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
    print(message)
    return JsonResponse({'message': "We are connected"})