import database_models.models as models
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
import client.discount_calculate as dc
from django.utils import timezone
import client.client_error as client_error
from django.db import transaction
import pytz
from portier.database import check_if_ticket_active
TRAINING = 2


def registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_date, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id, current_weight):
    """
    Adds a new client.

    Args:
        login (str): The login of the new client.
        password_hash (str): The password hash of the new client.
        email (str): The email of the new client.
        phone_number (str): The phone number of the new client.
        name (str): The first name of the new client.
        surname (str): The surname of the new client.
        gender (str): The gender of the new client.
        height (int): The height of the new client.
        birth_date (str): The birth date of the new client, format: '%Y-%m-%d'.
        advancement (str): The advancement of the new client.
        target_weight (int): The target weight of the new client.
        training_frequency (int): The training frequency of the new client.
        training_time (int): The training time of the new client.
        training_goal_id (int): The training goal id of the new client.
        gym_id (int): The gym id of the new client.
        current_weight (int, optional): The current weight of the new client.

    Returns:
        None
    """
    new_client = models.Client(
        login=login,
        password_hash=password_hash,
        email=email,
        phone_number=phone_number,
        name=name,
        surname=surname,
        gender=gender,
        height=height,
        birth_year=birth_date,
        advancement=advancement,
        target_weight=target_weight,
        training_frequency=training_frequency,
        training_time=training_time,
        training_goal_id=training_goal_id,
        gym_id=gym_id,
    )
    new_client.save()

    if current_weight:
        new_history = models.ClientDataHistory(
            weight=current_weight,
            measurement_date=datetime.now().date(),
            client=new_client)
        new_history.save()


def user_login(login, password):
    """
    Authenticate a user based on the provided login and password.

    Args:
        login (str): The login of the user.
        password (str): The password of the user.

    Returns:
        models.Client or None: The authenticated client if successful, None otherwise.
    """
    try:
        client = models.Client.objects.get(login=login)
        is_correct = check_password(password, client.password_hash)
        if is_correct:
            return client
        else:
            return None
    except models.Client.DoesNotExist:
        return None


def is_busy_login(login):
    """
    Check if a login is associated with an existing client in the database.

    Args:
        login (str): The login to check.

    Returns:
        bool: True if the login is associated with an existing client, False otherwise.
    """
    try:
        models.Client.objects.get(login=login)
        return True
    except models.Client.DoesNotExist:
        return False


def is_busy_email(email):
    """
    Check if an email is associated with an existing client in the database.

    Parameters:
    - email (str): The email address to check.

    Returns:
    bool: True if the email is associated with an existing client, False otherwise.
    """
    try:
        models.Client.objects.get(email=email)
        return True
    except models.Client.DoesNotExist:
        return False


def training_goals():
    """
    Retrieve a list of training goals.

    Returns:
        list: A list of lists containing training goal information.
              Each inner list includes [training_goal_id, name] for each training goal.
    """
    training_goals = models.TrainingGoal.objects.all()
    training_goals = [[goal.training_goal_id, goal.name] for goal in training_goals]
    return training_goals


def standard_gym_ticket_offer():
    """
    Retrieve information about standard gym ticket offers.

    Returns:
        list: A list of lists containing information about standard gym ticket offers.
              Each inner list includes [gym_ticket_offer_id, type, price, duration].
    """
    gym_tickets = models.GymTicketOffer.objects.all()
    gym_tickets = [[ticket.gym_ticket_offer_id, ticket.type, ticket.price, ticket.duration] for ticket in gym_tickets]
    return gym_tickets


def gym_ticket_offer_with_discount():
    """
    Retrieve information about gym ticket offers with active discounts.

    Returns:
        list: A list of lists containing information about gym ticket offers with active discounts.
              Each inner list includes [gym_ticket_offer_id, discount_id, type, discount_name,
              discount_percentage, original_price, price_after_discount, stop_date, duration].
    """
    discounts = models.Discount.objects.all()
    tickets = []
    for discount in discounts:
        # discount is not avaible yet or is no loger avaible
        if discount.start_date > datetime.now().date() or discount.stop_date and discount.stop_date < datetime.now().date():
            continue
        ticket = discount.gym_ticket_offer
        price_after_discount = dc.calculate_price_after_discount(ticket.price, discount.discount_percentages)
        tickets.append([ticket.gym_ticket_offer_id, discount.discount_id, ticket.type, discount.name, discount.discount_percentages, ticket.price, price_after_discount, dc.str_date(discount.stop_date), ticket.duration])
    return tickets


def get_gyms_list():
    """
    Retrieve information about gyms.

    Returns:
        list: A list of lists containing information about gyms.
              Each inner list includes [gym_id, name, city, street, house_number].
    """
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name, gym.city, gym.street, gym.house_number] for gym in gyms]
    return gyms


def change_default_gym_client(client_id, gym_id):
    """
    Change the default gym for a client.

    Args:
        client_id (int): The unique identifier of the client.
        gym_id (int): The unique identifier of the new default gym.

    Returns:
        None

    Raises:
        models.Client.DoesNotExist: If the client with the specified client_id does not exist.
        models.Gym.DoesNotExist: If the gym with the specified gym_id does not exist.
    """
    client = models.Client.objects.get(client_id=client_id)
    new_default_gym = models.Gym.objects.get(gym_id=gym_id)
    client.gym = new_default_gym
    client.save()


def get_ordered_classes_client(client_id, start_date):
    """
    Retrieve a list of ordered classes for a client within a specified date range.

    Args:
        client_id (int): The unique identifier of the client.
        start_date (str): The start date of the range in the format '%Y-%m-%d'.

    Returns:
        list: A list of lists containing information about ordered classes.
              Each inner list includes [ordered_schedule_id, schedule_date, start_time,
              gym_class_name, trainer_name, trainer_surname, is_default_gym].
    """
    delete_unpaid_orders()
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = end_date = start_date + timedelta(days=7)
    classes = models.OrderedSchedule.objects.filter(
        client_user__client_id=client_id,
        schedule_date__range=[start_date, end_date],
        payment_date__isnull=False
    )
    classes_list = []
    default_gym = models.Client.objects.get(client_id=client_id).gym.gym_id
    for classe in classes:
        is_default_gym = True if default_gym == classe.week_schedule.trainer.gym.gym_id else False
        classes_list.append(
            [
                classe.ordered_schedule_id,
                dc.str_date(classe.schedule_date),
                classe.week_schedule.start_time,
                classe.week_schedule.gym_classe.name,
                classe.week_schedule.trainer.name,
                classe.week_schedule.trainer.surname,
                is_default_gym
            ])
    return classes_list


def get_ordered_gym_classe_details(classe_id):
    """
    Retrieve details of a gym class based on the provided class_id.

    Parameters:
    - class_id (int): The unique identifier of the gym class.

    Returns:
    list: A list containing details of the gym class, including class name, trainer name,
          trainer surname, gym city, gym street, gym house number, gym classe date,
          start time, and week day.
    """
    try:
        classe = models.OrderedSchedule.objects.get(ordered_schedule_id=classe_id)
        details = get_week_schedule_details(classe.week_schedule.week_schedule_id)
        details.insert(6, dc.str_date(classe.schedule_date))
        return details
    except models.OrderedSchedule.DoesNotExist:
        return None


def get_week_schedule_details(week_schedule_id):
    """
    Get details for a specific gym class week schedule.

    Args:
        week_schedule_id (int): The unique identifier of the week schedule associated with the gym class.

    Returns:
        list: A list containing details about the gym class week schedule.
           Each inner list includes [gym_classe_Name, trainer_name, trainer_surname, gym_city, gym_street, gym_house_number, start_time, week_day]
    """
    gym_classe = models.WeekSchedule.objects.get(week_schedule_id=week_schedule_id)
    details = [
            gym_classe.gym_classe.name,
            gym_classe.trainer.name,
            gym_classe.trainer.surname,
            gym_classe.trainer.gym.city,
            gym_classe.trainer.gym.street,
            gym_classe.trainer.gym.house_number,
            gym_classe.start_time,
            gym_classe.week_day
            ]
    return details


def get_training_history(client_id):
    """
    Retrieve the training history for a client.

    Args:
        client_id (int): The unique identifier of the client.

    Returns:
        list: A list of lists containing information about the client's training history.
              Each inner list includes [gym_visit_id, start_date, start_hour, end_date, end_hour, duration, calories].
    """
    trainings = models.GymVisit.objects.filter(client_user__client_id=client_id)
    training_list = []
    for training in trainings:
        start_date = training.entry_time.astimezone(pytz.timezone('Europe/Warsaw'))
        end_date = training.departure_time.astimezone(pytz.timezone('Europe/Warsaw')) if training.departure_time else datetime.now(pytz.timezone('Europe/Warsaw'))
        exercises = models.ExerciseHistory.objects.filter(
            client__client_id=client_id,
            exercise_date__range=[start_date, end_date]
        )
        calories = 0
        time = 0
        for exercise in exercises:
            calories += exercise.calories
            time += exercise.duration
        end_date = training.departure_time.astimezone(pytz.timezone('Europe/Warsaw')) if training.departure_time else None
        training_list.append([training.gym_visit_id, dc.str_date(start_date), dc.str_hour(start_date), dc.str_date(end_date), dc.str_hour(end_date), time, calories])
    return training_list

def get_training_details(training_id):
    """
    Retrieve details of a specific training.

    Args:
        training_id (int): The unique identifier of the training.

    Returns:
        list: A list of dictionaries containing information about exercises in the training.
              Each dictionary includes exercise details such as name, start_date, start_hour, duration, repetitions_number, calories, and parameters if available.

    Raises:
        models.GymVisit.DoesNotExist: If the training with the specified training_id does not exist.
    """
    training = models.GymVisit.objects.get(gym_visit_id=training_id)
    # if training is not finished yet
    deaprture_time = training.departure_time if training.departure_time else datetime.now(pytz.timezone('Europe/Warsaw'))
    exercises = models.ExerciseHistory.objects.filter(
            client__client_id=training.client_user.client_id,
            exercise_date__range=[training.entry_time, deaprture_time]
        )
    exercises_list = []
    for exercise in exercises:
        item = {
            'name': exercise.exercise.name,
            'start_date': dc.str_date(exercise.exercise_date.astimezone(pytz.timezone('Europe/Warsaw'))),
            'start_hour': dc.str_hour(exercise.exercise_date.astimezone(pytz.timezone('Europe/Warsaw'))),
            'duration': exercise.duration,
            'repetitions_number': exercise.repetitions_number,
            'calories': exercise.calories
            }
        print(exercise.exercise_history_id)
        parameter_values = models.ExerciseHistoryParamValue.objects.filter(exercise_history__exercise_history_id=exercise.exercise_history_id)
        if parameter_values:
            parameters = [{'name': parameter.parameter.name, 'value': parameter.value, 'unit': parameter.parameter.units} for parameter in parameter_values]
            item.update({'parameters': parameters})
        exercises_list.append(item)
    return exercises_list

def get_gym_ticket_client(client_id):
    """
    Retrieve a list of gym tickets for a client.

    Args:
        client_id (int): The unique identifier of the client.

    Returns:
        list: A list of dictionaries containing information about the client's gym tickets.
              Each dictionary includes id, ticket_name, type, duration, status, discount_name, discount, price, end_date.
    """
    tickets = models.GymTicketHistory.objects.filter(client_id=client_id)
    tickets_list = []
    for ticket in tickets:
        status = check_if_ticket_active(ticket, client_id) if ticket.activation_date else None
        item = {
            'id': ticket.gym_ticket_history_id,
            'ticket_name': ticket.gym_ticket_offer.name,
            'type': ticket.gym_ticket_offer.type,
            'duration': ticket.gym_ticket_offer.duration,
            'status': status
            }
        discount = 0
        if ticket.discount:
            discount = ticket.discount.discount_percentages
            item.update({'discount_name': ticket.discount.name, 'discount': discount})
        item.update({'price': dc.calculate_price_after_discount(ticket.gym_ticket_offer.price, discount)})
        if ticket.gym_ticket_offer.type == "Dniowy" and (status or status == False):
            end_date = ticket.activation_date + timedelta(days=ticket.gym_ticket_offer.duration)
            item.update({'end_date': dc.str_date(end_date)})
        tickets_list.append(item)
    return tickets_list


def gym_ticket_details(ticket_id):
    """
    Retrieve details of a specific gym ticket.

    Args:
        ticket_id (int): The unique identifier of the gym ticket.

    Returns:
        dict: A dictionary containing details of the specified gym ticket.
              The dictionary includes ticket_name, type, duration, status, price_before, activation_date,
              discount_name, discount, price_after, end_date, days_to_end, or visits_to_end based on the type and status.

    Raises:
        models.GymTicketHistory.DoesNotExist: If the gym ticket with the specified ticket_id does not exist.
    """
    # todo refactorization of this and up function
    ticket = models.GymTicketHistory.objects.get(gym_ticket_history_id=ticket_id)
    client_id = ticket.client.client_id
    status = check_if_ticket_active(ticket, client_id) if ticket.activation_date else None
    item = {
            'ticket_name': ticket.gym_ticket_offer.name,
            'type': ticket.gym_ticket_offer.type,
            'duration': ticket.gym_ticket_offer.duration,
            'status': status,
            'price_before': ticket.gym_ticket_offer.price,
            'activation_date': dc.str_date(ticket.activation_date)
            }
    if ticket.discount:
        discount = ticket.discount.discount_percentages
        item.update({
            'discount_name': ticket.discount.name,
            'discount': discount,
            'price_after': dc.calculate_price_after_discount(ticket.gym_ticket_offer.price, discount)
            })
    if ticket.gym_ticket_offer.type == "Dniowy" and (status or status == False):
        end_date = ticket.activation_date + timedelta(days=ticket.gym_ticket_offer.duration)
        item.update({'end_date': dc.str_date(end_date)})
        if status:
            delta = end_date - timezone.now().date()
            item.update({'days_to_end': delta.days})
    elif ticket.gym_ticket_offer.type == "Wejściowy" and status:
            gym_visits = models.GymVisit.objects.filter(entry_time__gte=ticket.activation_date, client_user__client_id=client_id)
            visit_to_end = ticket.gym_ticket_offer.duration - len(gym_visits)
            item.update({'visits_to_end': visit_to_end})
    return item

def get_client_data(client_id):
    """
    Retrieve data for a client.

    Args:
        client_id (int): The unique identifier of the client.

    Returns:
        dict: A dictionary containing information about the client.
              The dictionary includes login, email, phone_number, name, surname, gender, height,
              birth_year, advancement, target_weight, training_frequency, training_time, training_goal,
              gym, current_weight.

    Raises:
        models.Client.DoesNotExist: If the client with the specified client_id does not exist.
    """
    client = models.Client.objects.get(client_id=client_id)
    # latest weight
    lastest = models.ClientDataHistory.objects.filter(client_id=1).order_by('measurement_date').first()
    current_weight = lastest.weight if lastest else None
    client_data = {
        'login': client.login,
        'email': client.email,
        'phone_number': client.phone_number,
        'name': client.name,
        'surname': client.surname,
        'gender': client.gender,
        'height': client.height,
        'birth_year': dc.str_date(client.birth_year),
        'advancement': client.advancement,
        'target_weight': client.target_weight,
        'training_frequency': client.training_frequency,
        'training_time': client.training_time,
        'training_goal': client.training_goal.name,
        'gym': client.gym.name,
        'current_weight': current_weight
    }
    return client_data

def get_trainer_by_gym(gym_id):
    """
    Get a list of trainers associated with a specific gym.

    Args:
        gym_id (int): The ID of the gym.

    Returns:
        List[List[int, str, str]]: A list containing trainer details (ID, name, surname).
    """
    trainers = models.Employee.objects.filter(gym_id=gym_id, type='trener')
    trainers = [[trainer.employee_id, trainer.name, trainer.surname] for trainer in trainers]
    return trainers

def get_gym_classes(gym_id):
    """
    Get a list of gym classes offered by trainers in a specific gym.

    Args:
        gym_id (int): The ID of the gym.

    Returns:
        List[List[int, str]]: A list containing gym class details (ID, name).
    """
    week_classes = models.WeekSchedule.objects.filter(trainer__gym_id=gym_id)
    gym_classes = [classe.gym_classe for classe in week_classes]
    id_list = []
    gym_classe_list = []
    for classe in gym_classes:
        if classe.gym_classe_id in id_list:
            continue
        gym_classe_list.append([classe.gym_classe_id, classe.name])
        id_list.append(classe.gym_classe_id)
    return gym_classe_list

def get_free_trainings(trainer_id, start_date_str, client_id):
    """
    Get a list of free trainings offered by a specific trainer on a specific date.

    Args:
        trainer_id (int): The ID of the trainer.
        start_date (str): The start date of the week (format: '%Y-%m-%d').
        client_id (int): The ID of the client.

    Returns:
        List[List[int, str, str, str, bool]]: A list containing free training details (ID, name, date, start_time, collision).

    Raises:
        None
    """
    delete_unpaid_orders()
    week_classes = models.WeekSchedule.objects.filter(
        trainer__employee_id=trainer_id,
        gym_classe__gym_classe_id=TRAINING
        )
    classes_list = get_free_items(start_date_str, week_classes, client_id)
    return classes_list

def get_free_places_gym_classe(classe_date, week_schedule_id):
    """
    Calculates the number of available places in a gym class for a given date and week schedule.

    Args:
        classe_date (date): The date of the gym class.
        week_schedule_id (int): The ID of the week schedule associated with the gym class.

    Returns:
        int: The number of available places in the gym class for the specified date and week schedule.
    """
    classe_date_stop = classe_date + timedelta(days=1)
    busy_classes = models.OrderedSchedule.objects.filter(
        schedule_date__gte=classe_date,
        schedule_date__lte=classe_date_stop,
        week_schedule__week_schedule_id=week_schedule_id
    )
    gym_classe = models.WeekSchedule.objects.get(week_schedule_id=week_schedule_id)
    return gym_classe.gym_classe.max_people - busy_classes.count()


def get_free_gym_classes(gym_id, start_date_str, client_id):
    """
    Get a list of free gym classes in a given gym starting from a specific date.

    Args:
        gym_id (int): The ID of the gym.
        start_date (str): The start date in the format '%Y-%m-%d'.
        client_id (int): The ID of the client.

    Returns:
        List: A list of dictionaries representing free gym classes.
    """
    delete_unpaid_orders()
    week_classes = models.WeekSchedule.objects.filter(
        trainer__gym_id=gym_id
    ).exclude(gym_classe__gym_classe_id=TRAINING)
    classes_list = get_free_items(start_date_str, week_classes, client_id)
    return classes_list


def get_free_items(start_date_str, week_classes, client_id):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').replace(tzinfo=pytz.timezone('Europe/Warsaw'))
    classes_list = []
    for week_classe in week_classes:
        week_classe_date = gym_classe_date(start_date, week_classe.week_day)
        if week_classe_date < datetime.now(pytz.timezone('Europe/Warsaw')):
            continue
        collision = check_collision(client_id, week_classe, dc.str_date(week_classe_date))
        free_places = get_free_places_gym_classe(week_classe_date, week_classe.week_schedule_id)
        item = [
            week_classe.week_schedule_id,
            week_classe.gym_classe.name,
            week_classe.trainer.name,
            week_classe.trainer.surname,
            dc.str_date(week_classe_date),
            week_classe.start_time,
            collision,
            free_places,
            week_classe.gym_classe.price
            ]
        classes_list.append(item)
    return classes_list


def gym_classe_date(input_date, weekday):
    day_delta = {
        'poniedziałek': 0,
        'wtorek': 1,
        'środa': 2,
        'czwartek': 3,
        'piątek': 4,
        'sobota': 5,
        'niedziela': 6
    }
    days_until_target = (day_delta[weekday] - input_date.weekday() + 7) % 7
    result_date = input_date + timedelta(days=days_until_target)
    return result_date


def check_collision(client_id, week_classe: models.WeekSchedule, date_str):
    """
    Check if there is a collision between a gym class and existing OrderedSchedules for a client on a specified date.

    Parameters:
    - client_id (int): The unique identifier of the client.
    - week_classe (models.WeekSchedule): The gym class to check for collisions.
    - date (str): The date of the gym class in the format 'YYYY-MM-DD'.

    Returns:
    int or None: Oreder gym classe id if is collision, otherwise None.
    """
    classe_date_start = datetime.strptime(date_str, "%Y-%m-%d")
    classe_date_stop = classe_date_start + timedelta(days=1)
    classes = models.OrderedSchedule.objects.filter(
        schedule_date__gt=classe_date_start,
        schedule_date__lt=classe_date_stop,
        client_user__client_id=client_id,
        payment_date__isnull=False
    )
    if not classes:
        return None
    date_str += f' {week_classe.start_time}'
    classe_date_start = datetime.strptime(date_str, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.timezone('Europe/Warsaw'))
    classe_date_stop = classe_date_start + timedelta(minutes=week_classe.gym_classe.duration)
    for classe in classes:
        ordered_start = classe.schedule_date
        ordered_stop = ordered_start + timedelta(minutes=classe.week_schedule.gym_classe.duration)
        if not (ordered_start > classe_date_stop or classe_date_start > ordered_stop):
            return classe.ordered_schedule_id
    return None


def get_gym_opening_hours(gym_id):
    """
    Retrieve the opening hours of a gym based on the provided gym_id.

    Parameters:
    - gym_id (int): The unique identifier of the gym.

    Returns:
    list or None: A list containing strings representing the opening hours for each day of the week
                  in the format 'opening-closing'. The list order corresponds to Sunday to Saturday.
                  Returns None if no gym is found with the specified gym_id.
    """
    try:
        gym = models.Gym.objects.get(gym_id=gym_id)
        opening_hours = [
            f'{gym.sunday_opening}-{gym.sunday_closing}',
            f'{gym.monday_opening}-{gym.monday_closing}',
            f'{gym.tuesday_opening}-{gym.tuesday_closing}',
            f'{gym.wednesday_opening}-{gym.wednesday_closing}',
            f'{gym.thursday_opening}-{gym.thursday_closing}',
            f'{gym.friday_opening}-{gym.friday_closing}',
            f'{gym.saturday_opening}-{gym.saturday_closing}'
        ]
        return opening_hours
    except models.Gym.DoesNotExist:
        return None


def check_client_can_buy_gym_ticket(client_id, ticket_type):
    """
    Check if a client is eligible to buy a specific type of gym ticket.

    Args:
        client_id (int): The ID of the client.
        ticket_type (str): The type of gym ticket.

    Returns:
        bool: True if the client can buy the ticket, False otherwise.
    """
    try:
        ticket = models.GymTicketHistory.objects.get(
            client__client_id=client_id,
            gym_ticket_offer__type=ticket_type,
            activation_date=None)
        return False
    except:
        return True


def delete_gym_ticket(gym_ticket_id):
    """
    Delete a gym ticket by its ID, only if it has not been activated.

    Args:
        gym_ticket_id (int): The ID of the gym ticket to be deleted.

    Raises:
        NotActivationDate: If the gym ticket has been activated and cannot be deleted.
        models.GymTicketHistory.DoesNotExist: If the gym ticket with the specified gym_ticket_id does not exist.
    """
    gym_ticket = models.GymTicketHistory.objects.get(gym_ticket_history_id=gym_ticket_id)
    if gym_ticket.activation_date:
        raise client_error.NotActivationDate
    else:
        gym_ticket.delete()


def cancel_gym_classe(ordered_gym_classe_id):
    """
    Cancels a gym class based on the provided ordered_gym_classe_id.

    Args:
        ordered_gym_classe_id (int): The unique identifier of the ordered gym class to be canceled.

    Raises:
        client_error.CannotCancelOrderedGymClasse: Raised if the scheduled date of the gym class
            is less than 24 hours from the current time, indicating that it cannot be canceled.

    Returns:
        None
    """
    ordered_gym_classe = models.OrderedSchedule.objects.get(ordered_schedule_id=ordered_gym_classe_id)
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    if ordered_gym_classe.schedule_date < now + timedelta(days=1):
        raise client_error.CannotCancelOrderedGymClasse
    else:
        ordered_gym_classe.delete()


@transaction.atomic
def reserve_gym_classes(gym_classes, client_id):
    """
    Reserves multiple gym classes for a client.

    Args:
        gym_classes (list): A list of dictionaries containing information about the gym classes to be reserved.
            Each dictionary should have the following keys:
            - 'schedule_date' (str): The date of the gym class in the format 'YYYY-MM-DD'.
            - 'hour' (str): The time of the gym class in the format 'HH:MM'.
            - 'week_schedule_id' (int): The unique identifier of the week schedule associated with the gym class.

        client_id (int): The unique identifier of the client for whom the gym classes are reserved.

    Returns:
        list: A list of ordered_schedule_id values for the successfully reserved gym classes.

    Raises:
        client_error.NotEnoughFreePlaces: Raised if there are not enough free places for any of the specified gym classes.
    """
    delete_unpaid_orders()
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    reserved_id = []
    for gym_classe in gym_classes:
        date_str = f"{gym_classe['schedule_date']} {gym_classe['hour']}"
        gym_classe_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        if get_free_places_gym_classe(gym_classe_date, gym_classe['week_schedule_id']) == 0:
            raise client_error.NotEnoughFreePlaces
        reserved_gym_classe = models.OrderedSchedule.objects.create(
            schedule_date=gym_classe_date,
            week_schedule_id=gym_classe['week_schedule_id'],
            client_user_id=client_id,
            reservation_date=now
            )
        reserved_gym_classe.save()
        reserved_id.append(reserved_gym_classe.ordered_schedule_id)
    return reserved_id


@transaction.atomic
def buy_items(gym_tickets, reserved_gym_classes, client_id):
    """
    Executes a transaction to purchase gym classes and tickets for a client.

    Args:
        gym_tickets (list): A list of dictionaries containing information about the gym tickets to be purchased.
            Each dictionary should have the necessary details for purchasing a gym ticket.

        reserved_gym_classes (list): A list of ordered_schedule_id values representing the gym classes to be purchased.

        client_id (int): The unique identifier of the client making the purchase.

    Returns:
        None
    """
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    buy_gym_classes(reserved_gym_classes, now)
    buy_tickets(gym_tickets, client_id, now)


@transaction.atomic
def buy_tickets(gym_tickets, client_id, now):
    """
    Purchase gym tickets for a client.

    Args:
        gym_tickets (list): A list of dictionaries containing information about the gym tickets to be purchased.
            Each dictionary should have the following keys:
            - 'gym_ticket_offer_id' (int): The unique identifier of the gym ticket offer.
            - 'discount_id' (int): The unique identifier of the discount applied to the gym ticket.
            - Other keys specific to gym ticket details.

        client_id (int): The unique identifier of the client making the purchase.

        now (datetime): The current date and time.

    Returns:
        None
    """
    for gym_ticket in gym_tickets:
        sold_gym_ticket = models.GymTicketHistory.objects.create(
            purchase_date=now,
            gym_ticket_offer_id = gym_ticket['gymTicketOfferId'],
            discount_id = gym_ticket['discountId'],
            client_id=client_id
        )
        sold_gym_ticket.save()


@transaction.atomic
def buy_gym_classes(reserved_gym_classes, now):
    """
    Purchase reserved gym classes for a client.

    Args:
        reserved_gym_classes (list): A list of ordered_schedule_id values representing the reserved gym classes.

        now (datetime): The current date and time.

    Returns:
        None
    """
    delete_unpaid_orders()
    for reserved_gym_classe_id in reserved_gym_classes:
        reseration = models.OrderedSchedule.objects.get(ordered_schedule_id=reserved_gym_classe_id)
        reseration.payment_date = now
        reseration.save()


def delete_unpaid_orders():
    """
    Delete unpaid gym class reservations that exceed a time threshold.

    Any gym class reservation made more than 15 minutes ago with no payment date
    will be deleted from the database.

    Args:
        None

    Returns:
        None
    """
    current_time = datetime.now(pytz.timezone('Europe/Warsaw'))
    time_threshold = current_time - timedelta(minutes=15)
    models.OrderedSchedule.objects.filter(
        reservation_date__lt=time_threshold,
        payment_date__isnull=True
    ).delete()


def get_free_gym_classe_details(fgc_date_str, fgc_id):
    """
    Get details and free places for a gym class on a specific date.

    Args:
        fgc_date_str (str): The date and time of the gym class in the format 'YYYY-MM-DD HH:MM'.
        fgc_id (int): The unique identifier of the week schedule associated with the gym class.

    Returns:
        list: A list containing details about the gym class and the number of free places.
    """
    week_schedule = models.WeekSchedule.objects.get(week_schedule_id=fgc_id)
    fgc_date_str += f' {week_schedule.start_time}'
    fgc_date = datetime.strptime(fgc_date_str, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.timezone('Europe/Warsaw'))
    print(fgc_date)
    details = get_week_schedule_details(fgc_id)
    print(details)
    details.insert(6, fgc_date_str[:-5])
    details.append(get_free_places_gym_classe(fgc_date, fgc_id))
    return details


def get_price_list():
    """
    Get the price list for all gym classes.

    Returns:
        list: A list of lists containing gym class names and their corresponding prices.
            Each inner list has two elements: gym class name and price.
    """
    gym_classes = models.GymClasse.objects.all()
    price_list = [ [ gym_classe.name, gym_classe.price ] for gym_classe in gym_classes ]
    return price_list


def check_collision_in_basket(week_schedule_id, date_str, basket):
    week_schedule = models.WeekSchedule.objects.get(week_schedule_id=week_schedule_id)
    date_str += f' {week_schedule.start_time}'
    gym_classe_start = datetime.strptime(date_str, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.timezone('Europe/Warsaw'))
    gym_classe_stop = gym_classe_start + timedelta(minutes=week_schedule.gym_classe.duration)
    for basket_item in basket:
        basket_week_schedule = models.WeekSchedule.objects.get(week_schedule_id=basket_item['week_schedule_id'])
        basket_date_str = f'{basket_item["schedule_date"]} {basket_week_schedule.start_time}'
        basket_start = datetime.strptime(basket_date_str, "%Y-%m-%d %H:%M").replace(tzinfo=pytz.timezone('Europe/Warsaw'))
        basket_stop = basket_start + timedelta(minutes=basket_week_schedule.gym_classe.duration)
        if not (gym_classe_start > basket_stop or basket_start > gym_classe_stop):
            return basket_item
    return None


def nearest_training(client_id):
    tr = []
    current_day = datetime.now().date()
    training = list(models.OrderedSchedule.objects.all().filter(client_user_id=client_id))
    for train in training:
        if train.schedule_date.date() >= current_day:
            tr.append(train)

    if not tr:
        return None

    tr_min = min(tr, key=lambda t: t.schedule_date)
    return tr_min.week_schedule.gym_classe.name


def describe_client_portier(client_id):
    try:
        client = models.Client.objects.get(client_id=client_id)
    except models.Client.DoesNotExist:
        return None

    result = {}
    result['name'] = client.name
    result['surname'] = client.surname
    result['email'] = client.email
    result['phone'] = client.phone_number
    result['training'] = nearest_training(client_id)
    tickets = get_gym_ticket_client(client_id)
    active_ticket = next((t for t in tickets if t.get('status')), None)
    if not active_ticket:
        result['active'] = False
        return result
    # ticket is active
    result['active'] = True
    ticket_info = gym_ticket_details(active_ticket['id'])
    result['ticket_name'] = f"{ticket_info['type']}, {ticket_info['duration']}"
    result['activation_date'] = ticket_info['activation_date']
    if ticket_info['type'] == 'Dniowy':
        result['daily'] = True
        result['end_date'] = ticket_info['end_date']
    else:
        result['daily'] = False
        result['visit_left'] = ticket_info['visit_to_end']

    return result


def not_active_ticket(client_id):
    try:
        client = models.Client.objects.get(client_id=client_id)
    except models.Client.DoesNotExist:
        return None
    tickets = get_gym_ticket_client(client_id)
    notactive_ticket = [t for t in tickets if t.get('status') is None]
    result = []
    for ticket in notactive_ticket:
        result.append({
            'ticket_id': ticket['id'],
            'ticket_name': f"{ticket['type']} {ticket['duration']}"
        })
    return result

def is_on_gym(client_id):
    try:
        client = models.Client.objects.get(client_id=client_id)
    except models.Client.DoesNotExist:
        return None
    visits = list(models.GymVisit.objects.all().filter(client_user_id=client_id, departure_time__isnull=True))
    if not visits:
        return False
    current_day = datetime.now().date()
    for v in visits:
        if v.entry_time.date() == current_day:
            return True
        return False
