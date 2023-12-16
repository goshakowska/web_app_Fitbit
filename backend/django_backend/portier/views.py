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


@csrf_exempt
def find_client_by_phone_number(request):
    data = json.loads(request.body.decode('utf-8'))
    phone = data.get('phone_number')
    clients = database.find_phone_number(phone)

    if clients:
        return JsonResponse({'clients': clients})
    else:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)


@csrf_exempt
def register_entry(request):
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    portier = data.get('portier_id')
    time = database.entry(client, portier)

    if time:
        return JsonResponse({'time': time})
    else:
        return JsonResponse({'error': "Wrong portier id"}, status=400)


@csrf_exempt
def register_leave(request):
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    portier = data.get('portier_id')
    time = database.leave(client, portier)

    if time:
        return JsonResponse({'time': time})
    else:
        return JsonResponse({'error': "Wrong portier id or no registered entry"}, status=400)
