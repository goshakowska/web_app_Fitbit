from database_models.models import Client, TrainingGoal
from django.contrib.auth.hashers import check_password


def registration(login, password_hash, email, phone_number,
        name, surname, gender, height, birth_year, advancement, target_weight,
        training_frequency, training_time, training_goal_id, gym_id):
    new_client = Client(
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


def user_login(login, password):
    try:
        client = Client.objects.get(login=login)
        is_correct = check_password(password, client.password_hash)
        if is_correct:
            return client.client_id, client.name
        else:
            return None, None
    except Client.DoesNotExist:
        return None, None

def is_busy_login(login):
    try:
        client = Client.objects.get(login=login)
        return True
    except Client.DoesNotExist:
        return False

def training_goals():
    training_goals = TrainingGoal.objects.all()
    training_goals = [[goal.training_goal_id, goal.name] for goal in training_goals]
    return training_goals