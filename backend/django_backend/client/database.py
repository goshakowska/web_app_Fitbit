import database_models.models as models
from django.contrib.auth.hashers import check_password
from datetime import datetime
import client.discount_calculate as dc


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
    gym_tickets = [[ticket.gym_ticket_offer_id, ticket.type, ticket.price] for ticket in gym_tickets]
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
        tickets.append([ticket.gym_ticket_offer_id, discount.discount_id, ticket.type, discount.name, discount.discount_percentages, ticket.price, price_after_discount, discount.stop_date])
    return tickets

def get_gyms_list():
    gyms = models.Gym.objects.all()
    gyms = [[gym.gym_id, gym.name, gym.city, gym.street, gym.house_number] for gym in gyms]
    return gyms