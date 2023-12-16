from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import portier.database as database


@csrf_exempt
def list_clients(request):
    clients = database.get_clients()
    return JsonResponse({'clients': clients})
