from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import manager.database as database


@csrf_exempt
def ticket_popularity_week(request):
    data = database.ticket_popularity_week()

    return JsonResponse({'plot':data})

