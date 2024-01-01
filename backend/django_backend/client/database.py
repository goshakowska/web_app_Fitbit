import database_models.models as models
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
import client.discount_calculate as dc
from django.utils import timezone

def registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_date, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id, current_weight):
    '''
    Adds new client.

    Args:
        login (int): The login of new client.
        password_hash (str): The password hash of new client.
        email (str): The email of new client.
        phone_number (str): The phone number of new client.
        name (str): The first name of new client.
        surname (str): The surname of the new client.
        gender (str): The gender of the new client.
        height (int): The height of the new client.
        birth_date (str): The birth date of new client, format: '%Y-%m-%d'.
        advancement (str): The advancement of the new client.
        target_weight (int): The target weight of the new client.
        training_frequency (int): The training frequency of new client.
        training_time (int): The training time of new client.
        training_goal_id (int): The training goal id of new client.
        gym_id (int): The gym id of new client.
        current_weight (int): The current weight of the new client.

    Returns:
        None
    '''
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
    '''
    Check if client login and password are correct.

    Args:
        login (str): The login of client.
        password (string): The password of client.

    Returns:
        models.Client or None: client if login and password are correct, None otherwise.
    '''
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
    '''
    Check if login of new client is busy.

    Args:
        login (str): The login of new client.

    Returns:
        bool: True if login of new client is busy, False otherwise.
    '''
    try:
        client = models.Client.objects.get(login=login)
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
        client = models.Client.objects.get(email=email)
        return True
    except models.Client.DoesNotExist:
        return False

def training_goals():
    '''
    List of training goal.

    Args:
        None.

    Returns
        list: [
            training goal id (int): id of training goal,
            training goal name (str): name of training goal
            ] for one training goal.
    '''
    training_goals = models.TrainingGoal.objects.all()
    training_goals = [[goal.training_goal_id, goal.name] for goal in training_goals]
    return training_goals

def standard_gym_ticket_offer():
    '''
    List of standard gym ticket offer.

    Args:
        None.

    Returns
        list: [
            gym ticket offer id (int): id of gym ticket,
            gym ticket offer type (str): type of gym ticket, 'Dniowy', 'Wejściowy',
            gym ticket offer price (float): price of gym ticket,
            gym ticket offer duration (int): duration of gym ticket
            ] for one gym ticket.
    '''
    gym_tickets = models.GymTicketOffer.objects.all()
    gym_tickets = [[ticket.gym_ticket_offer_id, ticket.type, ticket.price, ticket.duration] for ticket in gym_tickets]
    return gym_tickets

def gym_ticket_offer_with_discount():
    '''
    List of gym ticket offer with discount.

    Args:
        None.

    Returns
        list: [
            gym ticket offer id (int): id of gym ticket,
            discount id (int): id of discount,
            gym ticket offer type (str): type of gym ticket, 'Dniowy', 'Wejściowy',
            discount name (str): name of discount,
            discount percentages (int): percentages of discount,
            price before discount (int): price before discount,
            price after discount (float): price after discount,
            discount stop date (str): date when discount ends, format: '%Y-%m-%d',
            gym ticket offer duration (int): duration of gym ticket
            ] for one gym ticket.
    '''
    discounts = models.Discount.objects.all()
    tickets = []
    for discount in discounts:
        if discount.start_date > datetime.now().date() or discount.stop_date and discount.stop_date < datetime.now().date():
            continue
        ticket = discount.gym_ticket_offer
        price_after_discount = dc.calcucate_price_after_discount(ticket.price, discount.discount_percentages)
        tickets.append([ticket.gym_ticket_offer_id, discount.discount_id, ticket.type, discount.name, discount.discount_percentages, ticket.price, price_after_discount, dc.str_date(discount.stop_date), ticket.duration])
    return tickets

def get_gyms_list():
    '''
    List of gyms.

    Args:
        None.

    Returns:
        list: [
            gym id (int): id of gym,
            gym city (str): city of gym,
            gym street (str): street of gym,
            gym house number (str): house number of gym
            ] for one gym.
    '''
    # todo sprawdź number
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name, gym.city, gym.street, gym.house_number] for gym in gyms]
    return gyms

def change_default_gym_client(client_id, gym_id):
    '''
    Changes default gym of client.

    Args:
        client_id (int): The id of client.
        gym_id (int): The id of new default gym.

    Returns:
        None
    '''
    client = models.Client.objects.get(client_id=client_id)
    new_default_gym = models.Gym.objects.get(gym_id=gym_id)
    client.gym = new_default_gym
    client.save()

def get_ordered_classes_client(client_id, start_date):
    '''
    List of client's ordered classes during one week

    Args:
        client_id (int): The id of client.
        start_date (string): The fisrt day of week, format: '%Y-%m-%d'.

    Returns:
        list: [
            ordered classe id (int): id of ordered classe,
            ordered classe date (str): date of ordered classe, format: '%Y-%m-%d',
            ordered classe start time (str): hour when oredered classe starts,
            ordered classe name (str): name of ordered classe,
            trainer name (str): first name of trainer,
            trainer surname (str): surname of trainer,
            is default gym (bool): True if is default gym, False otherwise
            ] for one ordered classe
    '''
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = end_date = start_date + timedelta(days=7)
    classes = models.OrderedSchedule.objects.filter(
        client_user__client_id=client_id,
        schedule_date__range=[start_date, end_date]
    )
    classes_list = []
    default_gym = models.Client.objects.get(client_id=client_id).gym.gym_id
    for classe in classes:
        is_default_gym = True if default_gym == classe.week_schedule.trainer.gym.gym_id else False
        classes_list.append([classe.ordered_schedule_id, dc.str_date(classe.schedule_date), classe.week_schedule.start_time, classe.week_schedule.gym_classe.name, classe.week_schedule.trainer.name, classe.week_schedule.trainer.surname, is_default_gym])
    return classes_list

def get_gym_classe_details(classe_id):
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
        details = [
            classe.week_schedule.gym_classe.name,
            classe.week_schedule.trainer.name,
            classe.week_schedule.trainer.surname,
            classe.week_schedule.trainer.gym.city,
            classe.week_schedule.trainer.gym.street,
            classe.week_schedule.trainer.gym.house_number,
            dc.str_date(classe.schedule_date),
            classe.week_schedule.start_time,
            classe.week_schedule.week_day
            ]
        return details
    except models.OrderedSchedule.DoesNotExist:
        return None

def get_training_history(client_id):
    '''
    List of client's training history

    Args:
        client_id (int): The id of client.

    Returns:
        list: [
            training id (int),
            start date (str): date when training started, format: '%Y-%m-%d',
            end date (str): date when training ended, format: '%Y-%m-%d',
            time (int): training time in seconds,
            calories (int): calories burned during training
            ] for one training
    '''
    trainings = models.GymVisit.objects.filter(client_user__client_id=client_id)
    training_list = []
    for training in trainings:
        start_date = training.entry_time
        end_date = training.departure_time
        if not end_date:    # if training is not over yet
            continue
        exercises = models.ExerciseHistory.objects.filter(
            client__client_id=client_id,
            exercise_date__range=[start_date, end_date]
        )
        calories = 0
        time = 0
        # start_date, end_date = end_date, start_date
        for exercise in exercises:
            # todo początek i koniec oraz czas
            calories += exercise.calories
            time += exercise.duration
        training_list.append([training.gym_visit_id, dc.str_date(start_date), dc.str_hour(start_date), dc.str_date(end_date), dc.str_hour(end_date), time, calories])
    return training_list

def get_training_details(training_id):
    '''
    List of details of client's training history

    Args:
        training_id (int): The id of training.

    Returns:
        list: {
            name (str): name of exercise,
            start date (str): date when exercise started,
            duration (int): exercise duration,
            repetitions number (int): repetitions number,
            calories (int): calories burned during exercise,
            parameters (list): {
                name (str): name of parameter,
                value (int): value of parameter,
                unit (str): unit of parameter
            } for one parameter if parameters, [] otherwise
        } for one exercise
    '''
    training = models.GymVisit.objects.get(gym_visit_id=training_id)
    exercises = models.ExerciseHistory.objects.filter(
            client__client_id=training.client_user.client_id,
            exercise_date__range=[training.entry_time, training.departure_time]
        )
    exercises_list = []
    for exercise in exercises:
        item = {
            'name': exercise.exercise.name,
            'start_date': dc.str_date(exercise.exercise_date),
            'start_hour': dc.str_hour(exercise.exercise_date),
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
    '''
    List of client's gym tickets history

    Args:
        client_id (int): The id of client.

    Returns:
        list: {
            id (int): id of gym ticket history,
            ticket_name (str): name of gym ticket,
            type (str): type of gym ticket, 'Dniowy', 'Wejściowy',
            duration (int): duration of gym ticket,
            status (bool): True if ticket is valid, False if ticket is invalid, None if ticket is inactive
            discount_name (str): name of discount if discount
            discount (int): percentages of discount,
            price (float): ends price
        } for one gym ticket
    '''
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
        item.update({'price': dc.calcucate_price_after_discount(ticket.gym_ticket_offer.price, discount)})
        tickets_list.append(item)
    return tickets_list


def gym_ticket_details(ticket_id):
    '''
    Details of client's gym tickets history.

    Args:
        ticket_id (int): The id of gym ticket history.

    Returns:
        dict: {
            ticket_name (str): name of gym ticket,
            type (str): name of gym ticket,
            duration (int): duration of gym ticket,
            status (bool): True if ticket is valid, False if ticket is invalid, None if ticket is inactive,
            price_before (int): standard price of gym ticket,
            activation_date (str): activation date of gym ticket, format: '%Y-%m-%d',
            discount_name (str): name of discount if discount,
            discount (int): percentages of discount if discount,
            price_after (float): price after discount if discount,
            days_to_end (int): days to gym ticket ends if ticket is valid and type is 'Dniowy',
            end_date (str): date when gym ticket ends if ticket is not inactive and type is 'Dniowy', format: '%Y-%m-%d',
            visits_to_end (int): number of avaible visits of gym ticket if ticket is valid and type is 'Wejściowy'
        }.
    '''
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
            'price_after': dc.calcucate_price_after_discount(ticket.gym_ticket_offer.price, discount)
            })
    # to do end_date when type is 'Dniowy' and status == False
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
    '''
    Data of client.

    Args:
        client_id (int): The id of client.

    Returns:
        dict: {
        login (str): login of client
        email (str): email of client,
        phone_number (str): phone number of client,
        name (str): name of client,
        surname (str): surname of client,
        gender (str): gender of client,
        height (int): height of client,
        birth_year (str): birth date of client, format: '%Y-%m-%d',
        advancement (str): advancement of client,
        target_weight (int): target weight of client,
        training_frequency (int): standard training frequency of client,
        training_time (int): standard training time of client,
        training_goal (str): training goal's  name of client,
        gym (str): default gym's name of client,
        current_weight (int): current weight of client if client has current weight
        }.
    '''
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
    '''
    List of traniners of gym.

    Args:
        gym_id (int): The id of gym.

    Returns
        list: [
            trainer id (int): id of trainer,
            trainer name (str): fisrt name of trainer,
            trainer surname (str): surname of trainer
            ] for one trainer.
    '''
    trainers = models.Employee.objects.filter(gym_id=gym_id, type='trener')
    trainers = [[trainer.employee_id, trainer.name, trainer.surname] for trainer in trainers]
    return trainers

def get_gym_classes(gym_id):
    '''
    List of gym classes of gym.

    Args:
        gym_id (int): The id of gym.

    Returns
        list: [
            gym classe id (int): id of gym classe,
            gym classe name (str): name of classe
            ] for one gym classe.
    '''
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

def get_free_trainings(trainer_id, start_date, client_id):
    '''
    List of free individual trainings of trainer in one week.

    Args:
        trainer_id (int): The id of trainer.
        start_date (str): First day of week.
        client_id (int): The id of client.

    Returns
        list: [
            training id (int): id of training,
            training name (str): name of training,
            day (str): date of training,
            start time (str): hours when training starts,
            collision (bool): True if is collision, False otherwise
            ] for one gym classe.
    '''
    week_classes = models.WeekSchedule.objects.filter(trainer__employee_id=trainer_id)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if start_date.strftime('%A') !=  "Sunday":
        return
    end_date = end_date = start_date + timedelta(days=7)
    ordered_classes = models.OrderedSchedule.objects.filter(
        schedule_date__range=[start_date, end_date]
    )
    ordered_classes = [ classe.week_schedule.week_schedule_id for classe in ordered_classes]
    day_delta = {
        'poniedziałek': 1,
        'wtorek': 2,
        'środa': 3,
        'czwartek': 4,
        'piątek': 5,
        'sobota': 6,
        'niedziela': 0
    }
    # todo zrób to mądrzej i ładniej
    # todo colisions
    classes_list = []
    for week_classe in week_classes:
        if week_classe.week_schedule_id in ordered_classes or week_classe.gym_classe.gym_classe_id != 2:
            continue
        day = start_date + timedelta(days=day_delta[week_classe.week_day])
        collision = check_collision(client_id, week_classe, day)
        item = [week_classe.week_schedule_id, week_classe.gym_classe.name, dc.str_date(day), week_classe.start_time, collision]
        classes_list.append(item)
    return classes_list

def get_free_gym_classes(gym_id, start_date, client_id):
    '''
    List of free gym classes in one week.

    Args:
        trainer_id (int): The id of trainer.
        start_date (str): First day of week.
        client_id (int): The id of client.

    Returns
        list: [
            training id (int): id of training,
            training name (str): name of training,
            day (str): date of training,
            start time (str): hours when training starts,
            collision (bool): True if is collision, False otherwise
            ] for one gym classe.
    '''
    week_classes = models.WeekSchedule.objects.filter(trainer__gym_id=gym_id)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if start_date.strftime('%A') !=  "Sunday":
        return
    end_date = end_date = start_date + timedelta(days=7)
    ordered_classes = models.OrderedSchedule.objects.filter(
        schedule_date__range=[start_date, end_date]
    )
    ordered_classes = [ classe.week_schedule.week_schedule_id for classe in ordered_classes]
    day_delta = {
        'poniedziałek': 1,
        'wtorek': 2,
        'środa': 3,
        'czwartek': 4,
        'piątek': 5,
        'sobota': 6,
        'niedziela': 0
    }
    # todo zrób to mądrzej i ładniej
    # todo colisions
    classes_list = []
    for week_classe in week_classes:
        if week_classe.week_schedule_id in ordered_classes or week_classe.gym_classe.gym_classe_id != 2:
            continue
        day = start_date + timedelta(days=day_delta[week_classe.week_day])
        collision = check_collision(client_id, week_classe, day)
        item = [week_classe.week_schedule_id, week_classe.gym_classe.name, dc.str_date(day), week_classe.start_time, collision]
        classes_list.append(item)
    return classes_list

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


def check_collision(client_id, week_classe:models.WeekSchedule, date):
    """
    Check if there is a collision between a gym classe and existing OrderedSchedules for a client on a specified date.

    Parameters:
    - client_id (int): The unique identifier of the client.
    - week_classe (models.WeekSchedule): The WeekSchedule to check for collisions.
    - date (str): The date of the gym class in the format 'YYYY-MM-DD'.

    Returns:
    bool: True if there is a collision, False otherwise.
    """
    classe_date_start = datetime.strptime(date, "%Y-%m-%d")
    classe_date_stop = classe_date_start + timedelta(1)
    classes = models.OrderedSchedule.objects.filter(
        schedule_date__gt=classe_date_start,
        schedule_date__lt=classe_date_stop,
        client_user__client_id=client_id
    )
    if not classes:
        return False
    hours = int(week_classe.start_time[0:2])
    minutes = int(week_classe.start_time[3:5])
    classe_date_start += timedelta(hours=hours, minutes=minutes)
    classe_date_stop = classe_date_start + timedelta(minutes=week_classe.gym_classe.duration)
    for classe in classes:
        ordered_start = classe.schedule_date
        ordered_stop = ordered_start + timedelta(minutes=classe.week_schedule.gym_classe.duration)
        if not (ordered_start > classe_date_stop or classe_date_start > ordered_stop):
            return True
    return False




def check_if_ticket_active(ticket, client_id):      # podmienić funkcję
    # check if still active
    if ticket.gym_ticket_offer.type == "Dniowy":
        # ticket is for time
        end_date = ticket.activation_date + timedelta(days=ticket.gym_ticket_offer.duration)
        current_date = timezone.now().date()
        if current_date > end_date:
            # ticket has expired
            return False
        else:
            return True
    else:
        # ticket is for number of entries
        entries = models.GymVisit.objects.filter(client_user=client_id).count()
        limit_entries = ticket.gym_ticket_offer.duration
        if entries > limit_entries:
            # ticket has expired
            return False
        else:
            return True