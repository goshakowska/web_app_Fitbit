from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import simulation.database as database

# Create your views here.

@csrf_exempt
def clients_list(request):
    """
    Retrieve a list of all clients currently present in a specific gym.

    This view handles a POST request containing the gym_id in the request body.
    It retrieves a list of all clients currently present in the specified gym and returns a JSON response.

    Args:
        request (HttpRequest): The HTTP request containing the gym_id in the request body.

    Returns:
        JsonResponse: A JSON response containing the list of clients in the specified gym.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    clients = database.get_all_clients(gym_id)
    return JsonResponse({'clients': clients})

@csrf_exempt
def gyms_list(request):
    """
    Retrieve a list of all gyms.

    This view handles a POST request with no specific parameters.
    It retrieves a list of all gyms and returns a JSON response.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        JsonResponse: A JSON response containing the list of all gyms.
    """
    gyms = database.get_all_gyms()
    return JsonResponse({'gyms': gyms})

@csrf_exempt
def exercises_list(request):
    """
    Retrieve a list of all exercises along with their parameters.

    This view handles a POST request with no specific parameters.
    It retrieves a list of all exercises and their parameters and returns a JSON response.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        JsonResponse: A JSON response containing the list of all exercises.
    """
    exercises = database.get_all_exercises()
    return JsonResponse({'exercises': exercises})

@csrf_exempt
def equipments_list(request):
    """
    Retrieve a list of equipments available in a specific gym for a given exercise.

    This view handles a POST request containing the gym_id and exercise_id in the request body.
    It retrieves a list of equipments available in the specified gym for the given exercise and returns a JSON response.

    Args:
        request (HttpRequest): The HTTP request containing the gym_id and exercise_id in the request body.

    Returns:
        JsonResponse: A JSON response containing the list of equipments.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    exercise_id = data.get('exercise_id')
    equipments = database.get_equipments_by_gym_and_exercise(gym_id, exercise_id)
    return JsonResponse({'equipments': equipments})

@csrf_exempt
def insert_exercise_history(request):
    """
    Insert exercise history into the database.

    This view handles a POST request containing data about the exercise history.
    It inserts the exercise history into the database and returns a JSON response indicating success.

    Args:
        request (HttpRequest): The HTTP request containing data about the exercise history.

    Returns:
        JsonResponse: A JSON response indicating the success of the insertion.
    """
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