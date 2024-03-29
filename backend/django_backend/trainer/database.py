from django.db.models import F, ExpressionWrapper, fields, Value
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta
from dateutil.parser import parse
import calendar


def _current_week():
    """
    Returns dates of beginning and end of the current week

    Returns:
        list [datetime, datetime]: Beginnig, end of the current week
    """
    current_date = datetime.now().date()
    current_weekday = current_date.weekday()

    days_until_monday = current_weekday
    monday_of_current_week = current_date - timedelta(days=days_until_monday)

    return [monday_of_current_week,(monday_of_current_week + timedelta(days=6))]


def _add_minutes(start, minutes):
    """
    Adds given number of minutes to given time

    Args:
        start (str): Given time in format hh:mm
        minutes (int): Number of minutes to add

    Returns:
        str: Time after adding those minutes
    """
    start = datetime.strptime(start, "%H:%M")   # convert to datetime
    stop = start + timedelta(minutes=minutes)
    stop = stop.strftime("%H:%M")   # convert to string
    return stop

def _convert_to_datetime(week, start_time):
    # map week_day_name to number
    day_mapping = {day: idx for idx, day in enumerate(calendar.day_name)}
    # map polish names to english
    convert_polish = {
        "PONIEDZIAŁEK": "Monday",
        "WTOREK": "Tuesday",
        "ŚRODA": "Wednesday",
        "CZWARTEK": "Thursday",
        "PIĄTEK": "Friday",
        "SOBOTA": "Saturday",
        "NIEDZIELA": "Sunday"
    }

    convert_week = convert_polish[week.upper()]

    today = datetime.now()

    current_week_range = _current_week()

    # difference beetwen current week day and desired week day
    current_day_number = today.weekday()
    target_day_number = day_mapping[convert_week]
    day_difference = (target_day_number - current_day_number) % 7

    target_date = today + timedelta(days=day_difference)

    if current_week_range[0] <= target_date.date() <= current_week_range[1]:
        # if desired week day is in future (looking from today)
        target_datetime_str = f'{target_date.strftime("%Y-%m-%d")} {start_time}'
        target_datetime = parse(target_datetime_str)
        return target_datetime
    else:
        # if desired week day is in past (looking from today: for example it is Wednesday and we look for Monday)
        target_date = target_date - timedelta(days=7)
        target_datetime_str = f'{target_date.strftime("%Y-%m-%d")} {start_time}'
        target_datetime = parse(target_datetime_str)
        return target_datetime


def get_classes_for_trainer(trainer_id):
    """
    Fetches the class schedule for a trainer based on their trainer ID.

    Args:
        trainer_id (int): The unique identifier for the trainer.

    Returns:
        list: A list of dictionaries representing the classes scheduled for the trainer. Each dictionary contains
        information about the class, including class ID, class name, day of the week when it is scheduled,
        starting time, ending time, client ID (if it is an individual training), and client name (if applicable).
    """
    week_schedule_classes = m.WeekSchedule.objects.filter(trainer_id=trainer_id)
    result = []
    week = _current_week()

    for week_schedule_class in week_schedule_classes:
        # check if it is individual training
        if week_schedule_class.gym_classe.name == 'Trening indywidualny':
            ordered_schedule = m.OrderedSchedule.objects.filter(
                week_schedule=week_schedule_class.week_schedule_id,  # and
                schedule_date__gte=week[0],  # and
                schedule_date__lte=week[1]      # check if date is in current week
            ).first()
            # if it is ordered add client's data
            if ordered_schedule:
                start = _convert_to_datetime(week_schedule_class.week_day, week_schedule_class.start_time)
                end_time = _add_minutes(week_schedule_class.start_time,
                                                week_schedule_class.gym_classe.duration)
                end = _convert_to_datetime(week_schedule_class.week_day, end_time)
                result.append({
                    'class_id': week_schedule_class.gym_classe.gym_classe_id,
                    'id': week_schedule_class.gym_classe.gym_classe_id,
                    'title': week_schedule_class.gym_classe.name,
                    'class_day': week_schedule_class.week_day,
                    'client_id': ordered_schedule.client_user.client_id,
                    'client_name': ordered_schedule.client_user.name,
                    'start': start.strftime("%Y-%m-%dT%H:%M:%S"),
                    'end': end.strftime("%Y-%m-%dT%H:%M:%S"),
                })
            else:
                # not an individual training or training not ordered yet or for another week
                start = _convert_to_datetime(week_schedule_class.week_day, week_schedule_class.start_time)
                end_time = _add_minutes(week_schedule_class.start_time,
                                                    week_schedule_class.gym_classe.duration)
                end = _convert_to_datetime(week_schedule_class.week_day, end_time)
                result.append({
                    'class_id': week_schedule_class.gym_classe.gym_classe_id,
                    'id': week_schedule_class.gym_classe.gym_classe_id,
                    'title': week_schedule_class.gym_classe.name,
                    'class_day': week_schedule_class.week_day,
                    'client_id': None,
                    'client_name': None,
                    'start': start.strftime("%Y-%m-%dT%H:%M:%S"),
                    'end': end.strftime("%Y-%m-%dT%H:%M:%S"),
                })

        else:
            # not an individual training or training not ordered yet or for another week
            start = _convert_to_datetime(week_schedule_class.week_day, week_schedule_class.start_time)
            end_time = _add_minutes(week_schedule_class.start_time,
                                                week_schedule_class.gym_classe.duration)
            end = _convert_to_datetime(week_schedule_class.week_day, end_time)
            result.append({
                'class_id': week_schedule_class.gym_classe.gym_classe_id,
                'id': week_schedule_class.gym_classe.gym_classe_id,
                'title': week_schedule_class.gym_classe.name,
                'class_day': week_schedule_class.week_day,
                'client_id': None,
                'client_name': None,
                'start': start.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': end.strftime("%Y-%m-%dT%H:%M:%S"),
            })

    return result


def describe_group_class(class_id):
    """
    Retrieves the name and description of a group class based on its class ID.

    Args:
        class_id (int): The unique identifier for the group class.

    Returns:
        tuple: A tuple containing the name and description of the group class. If the class ID is not found,
        returns (None, None).
    """
    try:
        group_class = m.GymClasse.objects.get(gym_classe_id=class_id)
        return group_class.name, group_class.description
    except m.GymClasse.DoesNotExist:
        return None, None


def describe_client(client_id):
    """
    Fetches details about a client based on their client ID.

    Args:
        client_id (int): The unique identifier for the client.

    Returns:
        dict or None: A dictionary containing information about the client, including name, surname, email,
        phone number, height, weight, training frequency, training time, birth year, gender, target goal, and target weight.
        If the client with the specified ID is not found, returns None.
    """
    try:
        client = m.Client.objects.get(client_id=client_id)

        current_date = timezone.now()

        # get client's weight meassured nearest to current date
        client_weight = (
            m.ClientDataHistory.objects
            .filter(client=client_id, measurement_date__lte=current_date)
            .annotate(date_diff=ExpressionWrapper(current_date - F('measurement_date'), output_field=fields.DurationField()))
            .order_by('date_diff')
            .values('weight')
            .first()
        )

        return {
            'name': client.name,
            'surname': client.surname,
            'email': client.email,
            'phone_number': client.phone_number,
            'height': client.height,
            'weight': client_weight,
            'training_frequency': client.training_frequency,
            'training_time': client.training_time,
            'birth_year': client.birth_year.strftime('%d.%m.%Y'),
            'gender': client.gender,
            'target_goal': client.training_goal.name,
            'target_weight': client.target_weight,
        }
    except m.Client.DoesNotExist:
        return None


def get_exercises_for_training(trainer_id, client_id):
    """
    Retrieves the exercises planned for a training session with specific trainer and client.

    Args:
        trainer_id (int): The unique identifier for the trainer.
        client_id (int): The unique identifier for the client.

    Returns:
        tuple: A tuple containing a list of dictionaries with exercise details and the exercise plan ID.
        Each dictionary contains exercise ID, number of repetition or time of exercise, name, position in planned trainning session,
        If the exercise plan is not found, returns (None, None).
    """
    current_date = timezone.now()
    ordered_schedule_training = (
        m.OrderedSchedule.objects
        .select_related('week_schedule')  # join with WeekSchedule
        .filter(client_user=client_id, week_schedule__trainer_id=trainer_id, schedule_date__gte=current_date)
        .order_by('schedule_date')
        .first()
    )
    if not ordered_schedule_training:
        return None, None
    result = []
    exercise_plan_id = (m.ExercisePlan.objects
                        .filter(ordered_id=ordered_schedule_training.ordered_schedule_id)
                        .first())
    positions = m.ExercisePlanPosition.objects.filter(exercise_plan=exercise_plan_id).order_by('position')
    for position in positions:
        result.append(
                            {
                'exercise_id': position.exercise.exercise_id,
                'position': position.position,
                'name': position.exercise.name,
                'rep': position.repetitions_number if position.repetitions_number !=0 else None,
                'duration': position.duration if position.repetitions_number ==0 else None
            }
        )

    return result, exercise_plan_id.exercise_plan_id


def add_exercise(training_id, exercise_id, measured, position=None):
    """Adds an exercise to a training plan.

    Args:
        training_id (int): The unique identifier for the training plan.
        exercise_id (int): The unique identifier for the exercise.
        measured (int): The measurement value, either repetitions number or duration, depending on the exercise type.

    Returns:
        bool: True if the exercise is successfully added, False if an error occurs.
              Returns None if the exercise or training plan is not found.
    """
    if not position:
        # find last position in this training
        last_position = m.ExercisePlanPosition.objects.filter(exercise_plan=training_id).order_by('-position').first()
        if not last_position:
            position = 1
        else:
            last_position = last_position.position
            position = last_position + 1
    try:
        exercise = m.Exercise.objects.get(exercise_id=exercise_id)
        # measured by repetition number
        if exercise.repetitions_number != 0:
            repetition_number = measured
            # scale duration to new repetition number
            duration = (exercise.duration * repetition_number) // exercise.repetitions_number
        # measured by duration
        else:
            repetition_number = 0
            duration = measured

        plan = m.ExercisePlan.objects.get(exercise_plan_id=training_id)

        m.ExercisePlanPosition.objects.create(
            position=position,
            duration=duration,
            repetitions_number=repetition_number,
            exercise=exercise,
            exercise_plan=plan
            )
        return True
    except Exception as e:
        print(e)
        return None


def all_exercises():
    """
    Retrieves a list of all exercises with their details.

    This function fetches all exercises from the database and constructs a list of dictionaries,
    where each dictionary represents an exercise with the following details:
    - 'exercise_id': The unique identifier for the exercise.
    - 'name': The name of the exercise.
    - 'rep': The number of repetitions for the exercise, or None if it is a duration-based exercise.
    - 'duration': The duration of the exercise in seconds, or None if it is a repetition-based exercise.

    Returns:
        list: A list of dictionaries representing each exercise with its details.
    """
    result = []
    exercises = m.Exercise.objects.all()
    for exer in exercises:
        result.append(
                {
                    'exercise_id': exer.exercise_id,
                    'name': exer.name,
                    'rep': exer.repetitions_number if exer.repetitions_number != 0 else None,
                    'duration': exer.duration if exer.repetitions_number == 0 else None

                })

    return result


def save_exercises(exercise_list, exercise_plan_id):
    """
    Save a list of exercises to an exercise plan.

    This function takes a list of exercises with their details and saves them to the specified exercise plan.
    It removes any existing data related to the given exercise plan and adds the new exercises to the plan.

    Args:
        exercise_list (list): A list of dictionaries representing each exercise with details.
            Each dictionary should contain the following keys:
            - 'exercise_id': The unique identifier for the exercise.
            - 'rep': The number of repetitions for the exercise, or None if it is a duration-based exercise.
            - 'duration': The duration of the exercise in seconds, or None if it is a repetition-based exercise.
            - 'position': The position of the exercise in the exercise plan.
        exercise_plan_id (int): The unique identifier for the exercise plan.

    Returns:
        bool or None: Returns True if the exercises are successfully saved, None if there is an error during the process.
    """
    # remove old data for this training
    m.ExercisePlanPosition.objects.filter(exercise_plan_id=exercise_plan_id).delete()
    for exercise in exercise_list:
        measured = exercise['rep'] if exercise['rep'] else exercise['duration']
        result = add_exercise(exercise_plan_id,
                     exercise['exercise_id'],
                     measured,
                     exercise['position'])
        if not result:
            # error
            return None
    return True

