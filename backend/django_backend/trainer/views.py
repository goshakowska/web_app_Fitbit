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


@csrf_exempt
def describe_group_class(request):
    data = json.loads(request.body.decode('utf-8'))
    class_id = data.get('class_id')
    print(f"class_id {class_id}")
    name, description = database.describe_group_class(class_id)
    print(f"name: {name}, description: {description}")
    if name:
        return JsonResponse({'name': name, 'description': description})
    else:
        return JsonResponse({'error': "Wrong class id"}, status=400)


@csrf_exempt
def describe_client(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    print(f"client_id {client_id}")
    description = database.describe_client(client_id)

    if description:
        return JsonResponse({'description': description})
    else:
        return JsonResponse({'error': "Wrong client id"}, status=400)
