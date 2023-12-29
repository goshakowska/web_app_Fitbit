from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import trainer.database as database


@csrf_exempt
def timetable(request):
    """
    Retrieves the timetable for a trainer based on the provided trainer_id.

    Args:
        request (HttpRequest): The HTTP request object (trainer_id).

    Returns:
        JsonResponse: A JSON response containing the classes for the specified trainer.
    """
    data = json.loads(request.body.decode('utf-8'))
    trainer = data.get('trainer_id')
    classes = database.get_classes_for_trainer(trainer)

    return JsonResponse({'classes':classes})


@csrf_exempt
def describe_group_class(request):
    """
    Retrieves the name and description for a group class based on the provided class_id.

    Args:
        request (HttpRequest): The HTTP request object (class_id).

    Returns:
        JsonResponse: A JSON response containing the name and description for the specified group class.
                      If the class_id is invalid, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    class_id = data.get('class_id')
    name, description = database.describe_group_class(class_id)
    if name:
        return JsonResponse({'name': name, 'description': description})
    else:
        return JsonResponse({'error': "Wrong class id"}, status=400)


@csrf_exempt
def describe_client(request):
    """
    Retrieves the description for a client based on the provided client_id.

    Args:
        request (HttpRequest): The HTTP request object (client_id).

    Returns:
        JsonResponse: A JSON response containing the description for the specified client.
                      If the client_id is invalid, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    description = database.describe_client(client_id)

    if description:
        return JsonResponse({'description': description})
    else:
        return JsonResponse({'error': "Wrong client id"}, status=400)


@csrf_exempt
def incoming_training(request):
    """
    Retrieves the exercises and training_id for a training session based on the provided trainer_id and client_id.

    Args:
        request (HttpRequest): The HTTP request object (trainer_id, client_id).

    Returns:
        JsonResponse: A JSON response containing the exercises and training_id for the specified training session.
                      If there is no plan in the database for this training, returns an error response with a 400 status code.
    """
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
    """
    Checks if the specified exercise is measured by repetition number.

    Args:
        request (HttpRequest): The HTTP request object (exercise_id).

    Returns:
        JsonResponse: A JSON response containing the answer indicating whether the exercise is measured by repetition number.
                      If the exercise_id is invalid, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    exercise = data.get('exercise_id')
    answer = database.measured_by_repetition(exercise)

    if answer is not None:
        return JsonResponse({'answer':answer})
    else:
        return JsonResponse({'error': "Wrong exercise id"}, status=400)


@csrf_exempt
def exercise_measured_duration(request):
    """
    Checks if the specified exercise is measured by duration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the answer indicating whether the exercise is measured by duration.
                      If the exercise_id is invalid, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    exercise = data.get('exercise_id')
    answer = database.measured_by_duration(exercise)

    if answer is not None:
        return JsonResponse({'answer':answer})
    else:
        return JsonResponse({'error': "Wrong exercise id"}, status=400)


@csrf_exempt
def add_exercise_to_training(request):
    """
    Adds an exercise to a training session.

    Args:
        request (HttpRequest): The HTTP request object (training_id, exercise_id, measured).

    Returns:
        JsonResponse: A JSON response indicating whether the exercise was successfully added to the training session.
                      If there is an error during the process, returns an error response with a 400 status code.
    """
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
    """
    Moves an exercise up within the order of exercises in a training session.

    Args:
        request (HttpRequest): The HTTP request object (training_id, position).

    Returns:
        JsonResponse: A JSON response indicating whether the exercise was successfully moved up.
                      If the exercise is already at the top or there is an error during the process,
                      returns an error response with a 400 status code.
    """
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
    """
    Moves an exercise down within the order of exercises in a training session.

    Args:
        request (HttpRequest): The HTTP request object (training_id, position).

    Returns:
        JsonResponse: A JSON response indicating whether the exercise was successfully moved down.
                      If the exercise is already at the bottom or there is an error during the process,
                      returns an error response with a 400 status code.
    """
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
    """
    Deletes an exercise from a training session.

    Args:
        request (HttpRequest): The HTTP request object (training_id, position).

    Returns:
        JsonResponse: A JSON response indicating whether the exercise was successfully deleted.
                      If there is an error during the process or the position or training id is incorrect,
                      returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    training = data.get('training_id')
    exercise_pos = data.get('position')
    result = database.delete_exercise(training, exercise_pos)

    if result:
        return JsonResponse({'message': "Exercise deleted"})
    else:
        return JsonResponse({'error': "Wrong position or training id"}, status=400)
