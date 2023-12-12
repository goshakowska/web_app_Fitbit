from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import trainer.database as database

@csrf_exempt
def trainer_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    id, name = database.trainer_validate_login(login, password)
    if id:
        return JsonResponse({'id':id, 'name': name})
    else:
        raise Exception(f'Incorrect trainer login or password!')

