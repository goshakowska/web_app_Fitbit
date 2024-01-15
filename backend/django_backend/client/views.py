from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
import client.database as database
from django.core.mail import send_mail
import client.client_error as client_error
import database_models.models as models


@csrf_exempt
def registration(request):
    """
    View to handle user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the success or failure of the registration.
                      {'login': login} if registration is successful, {'error': 'Invalid request method'} otherwise.
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        login = data.get('login')
        password_hash = data.get('password_hash')
        password_hash = make_password(password_hash)
        email = data.get('email')
        phone_number = data.get('phone_number')
        name = data.get('name')
        surname = data.get('surname')
        gender = data.get('gender')
        height = data.get('height')
        birth_year = data.get('birth_year')
        advancement = data.get('advancement')
        target_weight = data.get('target_weight')
        training_frequency = data.get('training_frequency')
        training_time = data.get('training_time')
        training_goal_id = data.get('training_goal_id')
        gym_id = data.get('gym_id')
        current_weight = data.get('current_weight')
        database.registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_year, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id, current_weight)
        send_email(email)
        return JsonResponse({'login': login})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def send_email(email):
    """
    Send a registration confirmation email.

    Args:
        email (str): The email address of the recipient.

    Returns:
        None
    """
    subject = 'Rejestracja'
    message = "Dzień dobry!\n"
    message += "Dziękujemy za rejestrację w serwisie FitBit. "
    message += "Twoje konto jest już aktywne.\n"
    message += "Zachęcamy do zapisania się na swoje pierwsze zajęcia już dziś, ponieważ "
    message += "jak mówi znane przysłowie: Nie odkładaj na jutro tego, co możesz zrobić dziś!\n"
    message += "Życzymy sukcesów i satysfakcji ze swoich wyników,\n"
    message += "Zespół FitBit\n"
    from_email = 'health.strength.power@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


@csrf_exempt
def client_login(request):
    """
    View to handle client login.

    Args:
        request (HttpRequest): The HTTP request object containing user login credentials.

    Returns:
        JsonResponse: A JSON response containing client information if login is successful,
                      or an error message with status 400 if login fails.
    """
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    client = database.user_login(login, password)
    if client:
        return JsonResponse({'id':client.client_id, 'name': client.name})
    else:
        error_message = 'Incorrect user login!'
        return JsonResponse({'error': error_message}, status=400)

@csrf_exempt
def is_busy_login(request):
    """
    View to check if a login is already in use.

    Args:
        request (HttpRequest): The HTTP request object containing the login to check.

    Returns:
        JsonResponse: A JSON response indicating whether the login is in use or not.
    """
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    is_busy = database.is_busy_login(login)
    return JsonResponse({'is_busy': is_busy})

@csrf_exempt
def is_busy_email(request):
    """
    View to check if an email is associated with an existing client in the database.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: A JSON response indicating whether the email is associated with an existing client.
                  {'is_busy': True} if the email is busy, {'is_busy': False} otherwise.
    """
    data = json.loads(request.body.decode('utf-8'))
    email = data.get('email')
    is_busy = database.is_busy_email(email)
    return JsonResponse({'is_busy': is_busy})

@csrf_exempt
def training_goals(request):
    """
    View to retrieve information about training goals.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of training goals.
    """
    goals = database.training_goals()
    return JsonResponse({'goals': goals})

@csrf_exempt
def standard_gym_ticket_offer(request):
    """
    View to retrieve information about standard gym ticket offers.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of standard gym ticket offers.
    """
    tickets = database.standard_gym_ticket_offer()
    return JsonResponse({'tickets': tickets})

@csrf_exempt
def discount_gym_ticket_offer(request):
    """
    View to retrieve information about gyms.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of gyms.
    """
    tickets = database.gym_ticket_offer_with_discount()
    return JsonResponse({'tickets': tickets})

@csrf_exempt
def gyms_list(request):
    """
    Retrieve information about gyms.

    Returns:
        list: A list of lists containing information about gyms.
              Each inner list includes [gym_id, name, city, street, house_number].
    """
    gyms = database.get_gyms_list()
    return JsonResponse({'gyms': gyms})

@csrf_exempt
def change_default_gym_client(request):
    """
    View to change the default gym for a client.

    Args:
        request (HttpRequest): The HTTP request object containing client_id and gym_id in the request body.

    Returns:
        JsonResponse: A JSON response indicating the completion of the operation.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    gym_id = data.get('gym_id')
    database.change_default_gym_client(client_id, gym_id)
    return JsonResponse({'response': 'completed'})

@csrf_exempt
def get_ordered_classes_client(request):
    """
    View to retrieve a list of ordered classes for a client within a specified date range.

    Args:
        request (HttpRequest): The HTTP request object containing client_id and start_date in the request body.

    Returns:
        JsonResponse: A JSON response containing a list of ordered classes.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    start_date = data.get('start_date')
    classes = database.get_ordered_classes_client(client_id, start_date)
    return JsonResponse({'classes': classes})

@csrf_exempt
def get_ordered_gym_classe_details(request):
    """
    View to retrieve details of a gym class based on the provided class_id.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the class_id in the request body.

    Returns:
    JsonResponse: A JSON response containing the details of the gym class.
                  {'details': [list of gym class details]}.
    """
    data = json.loads(request.body.decode('utf-8'))
    classe_id = data.get('classe_id')
    details = database.get_ordered_gym_classe_details(classe_id)
    return JsonResponse({'details': details})

@csrf_exempt
def get_trainings_client(request):
    """
    View to retrieve the training history for a client.

    Args:
        request (HttpRequest): The HTTP request object containing client_id in the request body.

    Returns:
        JsonResponse: A JSON response containing a list of training history for the client.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    trenings = database.get_training_history(client_id)
    return JsonResponse({'trenings': trenings})

@csrf_exempt
def get_trening_details(request):
    """
    View to retrieve details of a specific training.

    Args:
        request (HttpRequest): The HTTP request object containing training_id in the request body.

    Returns:
        JsonResponse: A JSON response containing details of the specified training.
    """
    data = json.loads(request.body.decode('utf-8'))
    training_id = data.get('training_id')
    details = database.get_training_details(training_id)
    return JsonResponse({'details': details})

@csrf_exempt
def get_gym_tickets_client_history(request):
    """
    View to retrieve the gym ticket history for a client.

    Args:
        request (HttpRequest): The HTTP request object containing client_id in the request body.

    Returns:
        JsonResponse: A JSON response containing a list of gym ticket history for the client.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    tickets = database.get_gym_ticket_client(client_id)
    return JsonResponse({'tickets': tickets})

@csrf_exempt
def get_gym_tickets_details(request):
    """
    View to retrieve details of a specific gym ticket.

    Args:
        request (HttpRequest): The HTTP request object containing ticket_id in the request body.

    Returns:
        JsonResponse: A JSON response containing details of the specified gym ticket.

    Raises:
        models.GymTicketHistory.DoesNotExist: If the gym ticket with the specified ticket_id does not exist.
    """
    data = json.loads(request.body.decode('utf-8'))
    ticket_id = data.get('ticket_id')
    details = database.gym_ticket_details(ticket_id)
    return JsonResponse({'details': details})

@csrf_exempt
def get_client_data(request):
    """
    View to retrieve data for a client.

    Args:
        request (HttpRequest): The HTTP request object containing client_id in the request body.

    Returns:
        JsonResponse: A JSON response containing information about the client.

    Raises:
        models.Client.DoesNotExist: If the client with the specified client_id does not exist.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    client_data = database.get_client_data(client_id)
    return JsonResponse({'client_data': client_data})

@csrf_exempt
def get_trainer_by_gym(request):
    """
    Get a list of trainers associated with a specific gym.

    Args:
        request (HttpRequest): The HTTP request object containing the JSON data.
            Requires 'gym_id' in the JSON data.

    Returns:
        JsonResponse: A JSON response containing the list of trainers.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    trainers = database.get_trainer_by_gym(gym_id)
    return JsonResponse({'trainers': trainers})

@csrf_exempt
def get_gym_classes(request):
    """
    Get a list of gym classes offered by trainers in a specific gym.

    Args:
        request (HttpRequest): The HTTP request object containing the JSON data.
            Requires 'gym_id' in the JSON data.

    Returns:
        JsonResponse: A JSON response containing the list of gym classes.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    classes = database.get_gym_classes(gym_id)
    return JsonResponse({'classes': classes})

@csrf_exempt
def get_free_trainings(request):
    """
    Get a list of free trainings offered by a specific trainer on a specific date.

    Args:
        request (HttpRequest): The HTTP request object containing the JSON data.
            Requires 'trainer_id', 'start_date', and 'client_id' in the JSON data.

    Returns:
        JsonResponse: A JSON response containing the list of free trainings.
    """
    data = json.loads(request.body.decode('utf-8'))
    trainer_id = data.get('trainer_id')
    start_date = data.get('start_date')
    client_id = data.get('client_id')
    trainings = database.get_free_trainings(trainer_id, start_date, client_id)
    return JsonResponse({'trainings': trainings})

@csrf_exempt
def get_free_gym_classes(request):
    """
    Get a list of free gym classes offered by a specific gym on a specific date.

    Args:
        request (HttpRequest): The HTTP request object containing the JSON data.
            Requires 'gym_id', 'start_date', and 'client_id' in the JSON data.

    Returns:
        JsonResponse: A JSON response containing the list of free gym classes.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    start_date = data.get('start_date')
    client_id = data.get('client_id')
    classes = database.get_free_gym_classes(gym_id, start_date, client_id)
    return JsonResponse({'classes': classes})

@csrf_exempt
def get_gym_opening_hours(request):
    """
    View to retrieve the opening hours of a gym based on the provided gym_id.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the gym_id in the request body.

    Returns:
    JsonResponse: A JSON response containing the opening hours of the gym.
                  {'opening_hours': [list of opening hours]}.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_id = data.get('gym_id')
    opening_hours = database.get_gym_opening_hours(gym_id)
    return JsonResponse({'opening_hours': opening_hours})

@csrf_exempt
def check_client_can_buy_gym_ticket(request):
    """
    Check if a client is eligible to buy a specific type of gym ticket.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating whether the client can buy the ticket.
                      {'can_buy': True} if eligible, {'can_buy': False} otherwise.
    """
    data = json.loads(request.body.decode('utf-8'))
    client_id = data.get('client_id')
    ticket_type = data.get('type')
    can_buy = database.check_client_can_buy_gym_ticket(client_id, ticket_type)
    return JsonResponse({'can_buy': can_buy})

@csrf_exempt
def delete_gym_ticket(request):
    """
    Delete a gym ticket by its ID, only if it has not been activated.

    Args:
        request (HttpRequest): Django HTTP request object containing the JSON payload.
            The JSON payload should include the 'gym_ticket_id' key with the ID of the gym ticket to be deleted.

    Returns:
        JsonResponse: JSON response indicating the result of the deletion operation.
            If the deletion is successful, the response will contain {'result': 'success'}.
            If the gym ticket has already been activated, the response will contain {'result': 'error', 'message': 'Cannot delete an activated gym ticket.'}.
            If there is no gym ticket with the specified ID, the response will contain {'result': 'error', 'message': 'There is not any gym ticket with this id.'}.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_ticket_id = data.get('gym_ticket_id')

    try:
        database.delete_gym_ticket(gym_ticket_id)
        response_data = {'result': 'success'}
    except client_error.NotActivationDate:
        response_data = {'result': 'error', 'message': 'Cannot delete an activated gym ticket.'}
    except database.models.GymTicketHistory.DoesNotExist:
        response_data = {'result': 'error', 'message': 'There is not any gym ticket with this id.'}
    return JsonResponse(response_data)

@csrf_exempt
def cancel_gym_classe(request):
    """
    View to cancel a gym class based on the provided ordered_gym_classe_id.

    Args:
        request (HttpRequest): The HTTP request object containing the ordered_gym_classe_id
                               in the request body as JSON.

    Returns:
        JsonResponse: A JSON response indicating the result of the cancellation.
            - If successful, {'result': 'success'} is returned.
            - If an error occurs during the cancellation process, the exception message is returned.
    """
    data = json.loads(request.body.decode('utf-8'))
    ordered_gym_classe_id = data.get('ordered_gym_classe_id')
    try:
        database.cancel_gym_classe(ordered_gym_classe_id)
        response_data = {'result': 'success'}
    except client_error.CannotCancelOrderedGymClasse as e:
        response_data = {'error': 'Nie możesz już odwołać swojego udziału w tych zajęciach.'}
    return JsonResponse(response_data)

@csrf_exempt
def reserve_gym_classes(request):
    """
    View to reserve multiple gym classes for a client.

    Args:
        request (HttpRequest): The HTTP request object containing the gym_classes and client_id
                               in the request body as JSON.

    Returns:
        JsonResponse: A JSON response indicating the result of the reservation.
            - If successful, {'reserved_id': [list_of_reserved_ids]} is returned.
            - If there are not enough free places, {'error': 'Not enough free places.'} is returned.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_classes = data.get('gym_classes')
    client_id = data.get('client_id')
    try:
        reserved_id = database.reserve_gym_classes(gym_classes, client_id)
        response_data = {'reserved_id': reserved_id }
    except client_error.NotEnoughFreePlaces:
        response_data = {'error': 'Not enough free places.'}
    return JsonResponse(response_data)


@csrf_exempt
def buy_items(request):
    """
    View to purchase gym tickets and reserved gym classes for a client.

    Args:
        request (HttpRequest): The HTTP request object containing the gym_tickets,
                               reserved_gym_classes, and client_id in the request body as JSON.

    Returns:
        JsonResponse: A JSON response indicating the result of the purchase.
            - If successful, {'result': 'success'} is returned.
            - If there are no reserved gym classes to buy or it's too late, {'error': 'Too late to buy items.'} is returned.
    """
    data = json.loads(request.body.decode('utf-8'))
    gym_tickets = data.get('gym_tickets')
    reserved_gym_classes = data.get('reserved_gym_classes')
    client_id = data.get('client_id')
    try:
        database.buy_items(gym_tickets, reserved_gym_classes, client_id)
        response_data = {'result': 'success' }
    except models.OrderedSchedule.DoesNotExist:
        response_data = {'error': 'Too late to buy items.'}
    return JsonResponse(response_data)


@csrf_exempt
def get_free_gym_classe_details(request):
    """
    View to retrieve details and free places for a specific gym class on a given date.

    Args:
        request (HttpRequest): The HTTP request object containing the 'date' and 'gym_classe_id' in the request body as JSON.

    Returns:
        JsonResponse: A JSON response containing the details and free places for the specified gym class.
            The response format is {'details': [list_of_details]}.
    """
    data = json.loads(request.body.decode('utf-8'))
    date = data.get('date')
    gym_classe_id = data.get('gym_classe_id')
    details = database.get_free_gym_classe_details(date, gym_classe_id)
    response_data = {'details': details }
    return JsonResponse(response_data)


@csrf_exempt
def get_price_list(request):
    """
    View to retrieve the price list for all gym classes.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the price list for all gym classes.
            The response format is {'price_list': [list_of_price_details]}.
    """
    price_list = database.get_price_list()
    response_data = {'price_list': price_list }
    return JsonResponse(response_data)


@csrf_exempt
def check_collision_in_busket(request):
    data = json.loads(request.body.decode('utf-8'))
    date_str = data.get('date')
    week_schedule_id = data.get('week_schedule_id')
    basket = data.get('basket')
    is_collision = database.check_collision_in_basket(week_schedule_id, date_str, basket)
    response_data = {'is_collision': is_collision }
    return JsonResponse(response_data)


@csrf_exempt
def describe_client_portier(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id= data.get('client_id')
    result = database.describe_client_portier(client_id)
    if result:
        return JsonResponse({'description': result})
    else:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)

@csrf_exempt
def not_active_list(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id= data.get('client_id')
    result = database.not_active_ticket(client_id)
    if result is None:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)
    else:
        return JsonResponse({'tickets': result})

@csrf_exempt
def is_on_gym(request):
    data = json.loads(request.body.decode('utf-8'))
    client_id= data.get('client_id')
    result = database.is_on_gym(client_id)
    if result is None:
        return JsonResponse({'error': "This client doesn't exist"}, status=400)
    else:
        return JsonResponse({'is_on_gym': result})
