from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
import client.database as database
import client.user_errors as user_errors


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        login = data.get('login', '')
        password_hash = data.get('password_hash', '')
        password_hash = make_password(password_hash)
        email = data.get('email', '')
        phone_number = data.get('phone_number', '')
        name = data.get('name', '')
        surname = data.get('surname', '')
        gender = data.get('gender', '')
        height = data.get('height', 0)
        birth_year = data.get('birth_year', 0)
        advancement = data.get('advancement', '')
        target_weight = data.get('target_weight', 0)
        training_frequency = data.get('training_frequency', 0)
        training_time = data.get('training_time', 0)
        training_goal_id = data.get('training_goal_id', 0)
        gym_id = data.get('gym_id', 0)
        database.registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_year, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id)
        return JsonResponse({'login': login})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def client_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    print(login)
    id = database.user_login(login, password)
    if id:
        return JsonResponse({'id':id})
    else:
        raise user_errors.ClientLoginError(f'Incorrect user login!')