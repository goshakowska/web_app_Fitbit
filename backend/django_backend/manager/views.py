from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import manager.database as database


@csrf_exempt
def ticket_popularity_month(request):
    """
    Retrieves the popularity of gym tickets for the past week and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for ticket popularity in the past week.
    """
    data = database.ticket_popularity_month()

    return JsonResponse({'plot':data})


@csrf_exempt
def discount_popularity_month(request):
    """
    Retrieves the popularity of gym ticket discounts for the past week and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for discount popularity in the past week.
    """
    data = database.discount_popularity_month()

    return JsonResponse({'plot':data})


@csrf_exempt
def count_age_range(request):
    """
    Counts the distribution of clients across different age ranges and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for the distribution of clients across age ranges.
    """
    data = database.age_range()

    return JsonResponse({'plot':data})


@csrf_exempt
def sessions(request):
    """
    Retrieves trainer session data and generates a plot.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing either the generated plot or an error message.
        If the manager with the specified ID doesn't exist, an error message is returned with a status code of 400.
    """
    data = json.loads(request.body.decode('utf-8'))
    manager_id = data.get('manager_id')
    plot = database.trainer_sessions(manager_id)
    if plot:
        return JsonResponse({'plot':plot})
    else:
        return JsonResponse({'error': "This manager doesn't exist"}, status=400)

@csrf_exempt
def clients_week(request):
    """
    Plots client entry data for a specified manager over a week.

    Returns:
        JsonResponse: A JSON response containing either the generated plot or an error message.
        If the manager with the specified ID doesn't exist, an error message is returned with a status code of 400.
    """
    data = json.loads(request.body.decode('utf-8'))
    manager_id = data.get('manager_id')
    plot = database.clients_by_week(manager_id)
    if plot:
        return JsonResponse({'plot':plot})
    else:
        return JsonResponse({'error': "This manager doesn't exist"}, status=400)


@csrf_exempt
def clients_hour(request):
    """
    Plots client entry data within the last 24 hours.

    Returns:
        JsonResponse: A JSON response containing either the generated plot or an error message.
        If the manager with the specified ID doesn't exist, an error message is returned with a status code of 400.
    """
    data = json.loads(request.body.decode('utf-8'))
    manager_id = data.get('manager_id')
    plot = database.clients_by_hour(manager_id)
    if plot:
        return JsonResponse({'plot':plot})
    else:
        return JsonResponse({'error': "This manager doesn't exist"}, status=400)



@csrf_exempt
def equipment_usage(request):
    """
    Plots equipment usage data for a specified gym(where manager works) and equipment.

    Returns:
        JsonResponse: A JSON response containing either the generated plot or an error message.
        If the manager with the specified ID doesn't exist, an error message is returned with a status code of 400.
    """
    data = json.loads(request.body.decode('utf-8'))
    manager_id = data.get('manager_id')
    equipment_name = data.get('equipment_name')
    plot = database.equipment_usage(manager_id, equipment_name)
    if plot:
        return JsonResponse({'plot':plot})
    else:
        return JsonResponse({'error': "This manager doesn't exist"}, status=400)


@csrf_exempt
def all_equipment(request):
    """
    Retrieves a list of equipment names associated with a gym where manager works.

    Returns:
        JsonResponse: A JSON response containing either the generated plot or an error message.
        If the manager with the specified ID doesn't exist, an error message is returned with a status code of 400.
    """
    data = json.loads(request.body.decode('utf-8'))
    manager_id = data.get('manager_id')
    name = database.all_equipment(manager_id)
    if name:
        return JsonResponse({'names':name})
    else:
        return JsonResponse({'error': "This manager doesn't exist"}, status=400)
