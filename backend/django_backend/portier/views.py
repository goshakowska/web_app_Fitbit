from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import portier.database as database

@csrf_exempt
def portier_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    id, name = database.portier_validate_login(login, password)
    if id:
        return JsonResponse({'id':id, 'name': name})
    else:
        raise Exception(f'Incorrect portier login or password!')

