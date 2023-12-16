from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import portier.database as database


@csrf_exempt
def list_clients(request):
    clients = database.get_clients()
    return JsonResponse({'clients': clients})


@csrf_exempt
def find_client_by_name_surname(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    surname = data.get('surname')
    clients = database.find_name_surname(name, surname)

    if clients:
        return JsonResponse({'clients': clients})
    else:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)