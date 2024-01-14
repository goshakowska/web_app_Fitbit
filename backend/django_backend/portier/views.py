from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import portier.database as database


@csrf_exempt
def list_clients(request):
    """
    Retrieves a list of clients.

    Args:
        request (HttpRequest): The HTTP request object (no needed data).

    Returns:
        JsonResponse: A JSON response containing the list of clients.
    """
    clients = database.get_clients()
    return JsonResponse({'clients': clients})


@csrf_exempt
def find_client_by_name_surname(request):
    """
    Finds clients based on the provided name and/or surname.

    Args:
        request (HttpRequest): The HTTP request object (name, surname).

    Returns:
        JsonResponse: A JSON response containing the list of clients matching the given name and/or surname.
                      If no matching clients are found, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    surname = data.get('surname')
    clients = database.find_name_surname(name, surname)

    if clients:
        return JsonResponse({'clients': clients})
    else:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)


@csrf_exempt
def find_client_by_phone_number(request):
    """
    Finds clients based on the provided phone number.

    Args:
        request (HttpRequest): The HTTP request object (phone_number).

    Returns:
        JsonResponse: A JSON response containing the list of clients matching the given phone number.
                      If no matching clients are found, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    phone = data.get('phone_number')
    clients = database.find_phone_number(phone)

    if clients:
        return JsonResponse({'clients': clients})
    else:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)


@csrf_exempt
def register_entry(request):
    """
    Registers the entry of a client to the gym.

    Args:
        request (HttpRequest): The HTTP request object (client_id, portier_id).

    Returns:
        JsonResponse: A JSON response containing the entry time.
                      If there is an error or the portier id is incorrect, returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    portier = data.get('portier_id')
    time = database.entry(client, portier)

    if time:
        return JsonResponse({'time': time})
    else:
        return JsonResponse({'error': "Wrong portier id"}, status=400)


@csrf_exempt
def register_leave(request):
    """
    Registers the departure of a client from the gym.

    Args:
        request (HttpRequest): The HTTP request object (client_id, portier_id).

    Returns:
        JsonResponse: A JSON response containing the departure time and, if applicable, the locker number.
                      If there is an error, the portier id is incorrect, or there is no registered entry,
                      returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    portier = data.get('portier_id')
    time, locker = database.leave(client, portier)

    if time:
        return JsonResponse({'time': time, 'locker': locker})
    else:
        return JsonResponse({'error': "Wrong portier id or no registered entry"}, status=400)


@csrf_exempt
def assign_locker(request):
    """
    Assigns a locker to a client.

    Args:
        request (HttpRequest): The HTTP request object (client_id, portier_id).

    Returns:
        JsonResponse: A JSON response containing the assigned locker number.
                      If there is an error, the portier id is incorrect, or there is no free locker,
                      returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    portier = data.get('portier_id')
    locker = database.assign_locker(client, portier)

    if locker:
        return JsonResponse({'locker': locker})
    else:
        return JsonResponse({'error': "Wrong portier id or no free locker"}, status=400)


@csrf_exempt
def activate_ticket(request):
    """
    Activates a gym ticket for a client.

    Args:
        request (HttpRequest): The HTTP request object (client_id).

    Returns:
        JsonResponse: A JSON response indicating whether the ticket was successfully activated.
                      If the client already has an active ticket or doesn't have a ticket to activate,
                      returns an error response with a 400 status code.
    """
    data = json.loads(request.body.decode('utf-8'))
    client = data.get('client_id')
    result = database.activate_ticket(client)

    if result:
        return JsonResponse({'message': "Ticket activated"})
    else:
        return JsonResponse({'error': "Client has active ticket or doesn't have ticket to activate"}, status=400)
