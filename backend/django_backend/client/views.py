from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
import client.database as database


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        login = data.get('login')
        password_hash = data.get('password_hash')
        password_hash = make_password(password_hash)
        email = data.get('email')
        phone_number = data.get('phone_number')
        name = data.get('name')
        surname = data.get('surname')
        gender = data.get('gender')
        height = data.get('height')
        birth_year = data.get('birth_year')
        advancement = data.get('advancement')
        target_weight = data.get('target_weight')
        training_frequency = data.get('training_frequency')
        training_time = data.get('training_time')
        training_goal_id = data.get('training_goal_id')
        gym_id = data.get('gym_id')
        current_weight = data.get('current_weight')
        database.registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_year, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id, current_weight)
        return JsonResponse({'login': login})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def client_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    id, name = database.user_login(login, password)
    if id:
        return JsonResponse({'id':id, 'name': name})
    else:
        error_message = 'Incorrect user login!'
        return JsonResponse({'error': error_message}, status=400)

@csrf_exempt
def is_busy_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    is_busy = database.is_busy_login(login)
    return JsonResponse({'is_busy': is_busy})

@csrf_exempt
def training_goals(request):
    goals = database.training_goals()
    return JsonResponse({'goals': goals})

@csrf_exempt
def standard_gym_ticket_offer(request):
    tickets = database.standard_gym_ticket_offer()
    return JsonResponse({'tickets': tickets})

@csrf_exempt
def discount_gym_ticket_offer(request):
    tickets = database.gym_ticket_offer_with_discount()
    return JsonResponse({'tickets': tickets})

@csrf_exempt
def gyms_list(request):
    gyms = database.get_gyms_list()
    return JsonResponse({'gyms': gyms})

@csrf_exempt
def change_default_gym_client(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    gym_id = data.get('gym_id')
    database.change_default_gym_client(client_id, gym_id)
    return JsonResponse({'response': 'completed'})

@csrf_exempt
def get_ordered_classes_client(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    start_date = data.get('start_date')
    classes = database.get_ordered_classes_client(client_id, start_date)
    return JsonResponse({'classes': classes})