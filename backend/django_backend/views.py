from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import Illness, Client

@csrf_exempt  # Ignoruje CSRF dla uproszczenia
def modify_number(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        received_number = data.get('number', 0)
        modified_number = received_number * 2  # Modyfikacja: Podwaja liczbę
        return JsonResponse({'result': modified_number})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def test_message(request):
    data = {
        'id': 1,
        'message': 'Udało się'
    }

    return JsonResponse(data)

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        login = data.get('login', '')
        password_hash = data.get('password_hash', '')
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

        new_client = Client(
            login=login,
            password_hash=password_hash,
            email=email,
            phone_number=phone_number,
            name=name,
            surname=surname,
            gender=gender,
            height=height,
            birth_year=birth_year,
            advancement=advancement,
            target_weight=target_weight,
            training_frequency=training_frequency,
            training_time=training_time,
            training_goal_id=training_goal_id,
            gym_id=gym_id,
        )
        new_client.save()
        return JsonResponse({'login': login})
    else:
        return JsonResponse({'error': 'Invalid request method'})
