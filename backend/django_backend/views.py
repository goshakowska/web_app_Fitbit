from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
# import database
# import user_errors


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

