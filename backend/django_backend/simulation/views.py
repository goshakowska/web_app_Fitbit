from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import simulation.database as database

# Create your views here.

@csrf_exempt
def clients_list(request):
    clients = database.get_all_clients()
    return JsonResponse({'clients': clients})