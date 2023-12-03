from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import Illness

@csrf_exempt  # Ignoruje CSRF dla uproszczenia
def modify_number(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        received_number = data.get('number', 0)
        modified_number = received_number * 2  # Modyfikacja: Podwaja liczbę
        astma_illness = Illness(illness_id=5, name='astma')
        astma_illness.save()
        return JsonResponse({'result': modified_number})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def test_message(request):
    data = {
        'id': 1,
        'message': 'Udało się'
    }

    return JsonResponse(data)
