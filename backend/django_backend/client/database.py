import database_models.models as models
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
import client.discount_calculate as dc
from django.utils import timezone

def registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_year, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id, current_weight):
    new_client = models.Client(
        login=login,
        password_hash=password_hash,
        email=email,
        phone_number=phone_number,
        name=name,
        surname=surname,
        gender=gender,
        height=height,
        birth_year=birth_year,
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
    try:
        client = models.Client.objects.get(login=login)
        is_correct = check_password(password, client.password_hash)
        if is_correct:
            return client.client_id, client.name
        else:
            return None, None
    except models.Client.DoesNotExist:
        return None, None

def is_busy_login(login):
    try:
        client = models.Client.objects.get(login=login)
        return True
    except models.Client.DoesNotExist:
        return False

def training_goals():
    training_goals = models.TrainingGoal.objects.all()
    training_goals = [[goal.training_goal_id, goal.name] for goal in training_goals]
    return training_goals

def standard_gym_ticket_offer():
    gym_tickets = models.GymTicketOffer.objects.all()
    gym_tickets = [[ticket.gym_ticket_offer_id, ticket.type, ticket.price, ticket.duration] for ticket in gym_tickets]
    return gym_tickets

def gym_ticket_offer_with_discount():
    discounts = models.Discount.objects.all()
    tickets = []
    for discount in discounts:
        if discount.start_date > datetime.now().date() or discount.stop_date and discount.stop_date < datetime.now().date():
            continue
        print(discount.gym_ticket_offer)
        ticket = discount.gym_ticket_offer
        price_after_discount = dc.calcucate_price_after_discount(ticket.price, discount.discount_percentages)
        tickets.append([ticket.gym_ticket_offer_id, discount.discount_id, ticket.type, discount.name, discount.discount_percentages, ticket.price, price_after_discount, discount.stop_date, ticket.duration])
    return tickets

def get_gyms_list():
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name, gym.city, gym.street, gym.house_number] for gym in gyms]
    return gyms

def change_default_gym_client(client_id, gym_id):
    client = models.Client.objects.get(client_id=client_id)
    new_default_gym = models.Gym.objects.get(gym_id=gym_id)
    client.gym = new_default_gym
    client.save()

def get_ordered_classes_client(client_id, start_date):
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
        classes_list.append([classe.ordered_schedule_id, classe.schedule_date, classe.week_schedule.start_time, classe.week_schedule.gym_classe.name, classe.week_schedule.trainer.name, classe.week_schedule.trainer.surname, is_default_gym])
    return classes_list

def get_trening_history(client_id):
    trenings = models.GymVisit.objects.filter(client_user__client_id=client_id)
    trening_list = []
    for trening in trenings:
        start_date = trening.entry_time
        end_date = trening.departure_time
        if not end_date:    # jeśli trening jeszcze się nie skończył
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
        trening_list.append([trening.gym_visit_id, start_date, end_date, time, calories])
    return trening_list

def get_training_details(training_id):
    training = models.GymVisit.objects.get(gym_visit_id=training_id)
    exercises = models.ExerciseHistory.objects.filter(
            client__client_id=training.client_user.client_id,
            exercise_date__range=[training.entry_time, training.departure_time]
        )
    exercises_list = []
    for exercise in exercises:
        item = {
            'name': exercise.exercise.name,
            'start_date': exercise.exercise_date,
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
            'activation_date': ticket.activation_date
            }
    if ticket.discount:
        discount = ticket.discount.discount_percentages
        item.update({
            'discount_name': ticket.discount.name,
            'discount': discount,
            'price_after': dc.calcucate_price_after_discount(ticket.gym_ticket_offer.price, discount)
            })
    if status:
        if ticket.gym_ticket_offer.type == "Dniowy":
            end_date = ticket.activation_date + timedelta(days=ticket.gym_ticket_offer.duration)
            delta = end_date - timezone.now().date()
            item.update({'days_to_end': delta.days, 'end_date': end_date})
        else:
            gym_visits = models.GymVisit.objects.filter(entry_time__gte=ticket.activation_date)
            visit_to_end = ticket.gym_ticket_offer.duration - len(gym_visits)
            item.update({'visits_to_end': visit_to_end})
    return item

def get_client_data(client_id):
    client = models.Client.objects.get(client_id=client_id)
    # latest weight
    lastest = models.ClientDataHistory.objects.filter(client_id=1).order_by('-measurement_date').first()
    current_weight = lastest.weight if lastest else None
    client_data = {
        'login': client.login,
        'email': client.email,
        'phone_number': client.phone_number,
        'name': client.name,
        'surname': client.surname,
        'gender': client.gender,
        'height': client.height,
        'birth_year': client.birth_year,
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
    trainers = models.Employee.objects.filter(gym_id=gym_id, type='trener')
    trainers = [[trainer.employee_id, trainer.name, trainer.surname] for trainer in trainers]
    return trainers

def get_gym_classes(gym_id):
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
    week_classes = models.WeekSchedule.objects.filter(trainer__employee_id=trainer_id)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if start_date.strftime('%A') !=  "Monday":
        return
    end_date = end_date = start_date + timedelta(days=7)
    ordered_classes = models.OrderedSchedule.objects.filter(
        schedule_date__range=[start_date, end_date]
    )
    ordered_classes = [ classe.week_schedule.week_schedule_id for classe in ordered_classes]
    day_delta = {
        'poniedziałek': 0,
        'wtorek': 1,
        'środa': 2,
        'czwartek': 3,
        'piątek': 4,
        'sobota': 5,
        'niedziela': 6
    }
    # todo zrób to mądrzej i ładniej
    # todo colisions
    classes_list = []
    for week_classe in week_classes:
        if week_classe.week_schedule_id in ordered_classes or week_classe.gym_classe.gym_classe_id != 2:
            continue
        day = start_date + timedelta(days=day_delta[week_classe.week_day])
        collision = check_collision(client_id, week_classe, day)
        item = [week_classe.week_schedule_id, week_classe.gym_classe.name, day, week_classe.start_time, collision]
        classes_list.append(item)
    return classes_list

def check_collision(client_id, week_classe, date):
    classes = models.OrderedSchedule.objects.filter(schedule_date=date, client_user__client_id=client_id)
    if not classes:
        return False
    # date_str = datetime.strptime(date, '%Y-%m-%d')
    # date_another = datetime.strptime(f'{date_str} {week_classe.start_time}', '%Y-%m-%d %H:%M')
    for classe in classes:
        return True



def check_if_ticket_active(ticket, client_id):
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