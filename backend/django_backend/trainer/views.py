from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import trainer.database as database


@csrf_exempt
def timetable(request):
    data = json.loads(request.body.decode('utf-8'))
    trainer = data.get('trainer_id')
    print(f"trainer_id {trainer}")
    classes = database.get_classes_for_trainer(trainer)
    print(f"classes: {classes}")

    return JsonResponse({'classes':classes})
