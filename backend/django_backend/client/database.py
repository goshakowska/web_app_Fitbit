from database_models.models import Client
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
        user = Client.objects.get(login=login)
        is_correct = check_password(password, user.password_hash)
        if is_correct:
            print(user.client_id)
            return user.client_id
        else:
            print(user.client_id),
            return user.client_id
    except Client.DoesNotExist:
        return None