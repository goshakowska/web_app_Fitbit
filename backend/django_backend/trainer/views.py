from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import trainer.database as database


@csrf_exempt
def timetable(request):
    data = json.loads(request.body.decode('utf-8'))
    trainer = data.get('trainer_id')
    classes = database.get_classes_for_trainer(trainer)

    return JsonResponse({'classes':classes})


@csrf_exempt
def describe_group_class(request):
    data = json.loads(request.body.decode('utf-8'))
    class_id = data.get('class_id')
    name, description = database.describe_group_class(class_id)
    if name:
        return JsonResponse({'name': name, 'description': description})
    else:
        return JsonResponse({'error': "Wrong class id"}, status=400)


@csrf_exempt
def describe_client(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    description = database.describe_client(client_id)

    if description:
        return JsonResponse({'description': description})
    else:
        return JsonResponse({'error': "Wrong client id"}, status=400)


@csrf_exempt
def incoming_training(request):
    data = json.loads(request.body.decode('utf-8'))
    trainer = data.get('trainer_id')
    client = data.get('client_id')
    exercises, training_id = database.get_exercises_for_training(trainer, client)
    print(exercises)
    print(training_id)
    if training_id:
        return JsonResponse({'exercises':exercises, 'training_id': training_id})
    else:
        return JsonResponse({'error': "No training_plan in database for this class"}, status=400)
