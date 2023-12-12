from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import manager.database as database

@csrf_exempt
def manager_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    id, name = database.manager_validate_login(login, password)
    if id:
        return JsonResponse({'id':id, 'name': name})
    else:
        raise Exception(f'Incorrect manager login or password!')
