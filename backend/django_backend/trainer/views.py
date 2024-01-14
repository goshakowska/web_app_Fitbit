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

    if training_id:
        return JsonResponse({'exercises':exercises, 'training_id': training_id})
    else:
        return JsonResponse({'error': "No plan in database for this training"}, status=400)


@csrf_exempt
def exercise_measured_repetition_number(request):
    # check if this exercise is measured by repetition number
    data = json.loads(request.body.decode('utf-8'))
    exercise = data.get('exercise_id')
    answer = database.measured_by_repetition(exercise)

    if answer is not None:
        return JsonResponse({'answer':answer})
    else:
        return JsonResponse({'error': "Wrong exercise id"}, status=400)


@csrf_exempt
def exercise_measured_duration(request):
    # check if this exercise is measured by duration
    data = json.loads(request.body.decode('utf-8'))
    exercise = data.get('exercise_id')
    answer = database.measured_by_duration(exercise)

    if answer is not None:
        return JsonResponse({'answer':answer})
    else:
        return JsonResponse({'error': "Wrong exercise id"}, status=400)


@csrf_exempt
def add_exercise_to_training(request):
    data = json.loads(request.body.decode('utf-8'))
    training = data.get('training_id')
    exercise = data.get('exercise_id')
    measured = data.get('measured')     # repetition number or duration
    result = database.add_exercise(training, exercise, measured)

    if result:
        return JsonResponse({'message': "Exercise added"})
    else:
        return JsonResponse({'error': "Error during adding exercise"}, status=400)


@csrf_exempt
def move_up_exercise(request):
    data = json.loads(request.body.decode('utf-8'))
    training = data.get('training_id')
    exercise_pos = data.get('position')
    result = database.move_up(training, exercise_pos)

    if result:
        return JsonResponse({'message': "Exercise moved"})
    else:
        return JsonResponse({'error': "Can't move exercise"}, status=400)


@csrf_exempt
def move_down_exercise(request):
    data = json.loads(request.body.decode('utf-8'))
    training = data.get('training_id')
    exercise_pos = data.get('position')
    result = database.move_down(training, exercise_pos)

    if result:
        return JsonResponse({'message': "Exercise moved"})
    else:
        return JsonResponse({'error': "Can't move exercise"}, status=400)


@csrf_exempt
def delete_exercise_from_training(request):
    data = json.loads(request.body.decode('utf-8'))
    training = data.get('training_id')
    exercise_pos = data.get('position')
    result = database.delete_exercise(training, exercise_pos)

    if result:
        return JsonResponse({'message': "Exercise deleted"})
    else:
        return JsonResponse({'error': "Wrong position or training id"}, status=400)


@csrf_exempt
def all_exercises(request):
    result = database.all_exercises()
    return JsonResponse({'exercises': result})

