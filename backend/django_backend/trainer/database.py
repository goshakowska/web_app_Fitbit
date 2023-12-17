from django.db.models import F, ExpressionWrapper, fields, Value
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta


def _current_week():
    current_date = datetime.now().date()
    current_weekday = current_date.weekday()

    days_until_monday = current_weekday
    monday_of_current_week = current_date - timedelta(days=days_until_monday)

    return [monday_of_current_week,(monday_of_current_week + timedelta(days=6))]


def _add_minutes(start, minutes):
    start = datetime.strptime(start, "%H:%M")   #convert to datetime
    stop = start + timedelta(minutes=minutes)
    stop = stop.strftime("%H:%M")   #convert to string
    return stop


def get_classes_for_trainer(trainer_id):
    week_schedule_classes = m.WeekSchedule.objects.filter(trainer_id=trainer_id)
    result = []
    week = _current_week()

    for week_schedule_class in week_schedule_classes:
        # check if it is individual training
        if week_schedule_class.gym_classe.name == 'zajęcia indywidualne':
            ordered_schedule = m.OrderedSchedule.objects.filter(
                week_schedule=week_schedule_class.week_schedule_id,  # and
                schedule_date__gte=week[0],  # and
                schedule_date__lte=week[1]      # check if date is in current week
            ).first()
            # if it is ordered add client's data
            if ordered_schedule:
                result.append({
                    'class_id': week_schedule_class.gym_classe.gym_classe_id,
                    'class_name': week_schedule_class.gym_classe.name,
                    'class_day': week_schedule_class.week_day,
                    'class_start': week_schedule_class.start_time,
                    'class_stop': _add_minutes(week_schedule_class.start_time,
                                                week_schedule_class.gym_classe.duration),
                    'client_id': ordered_schedule.client_user.client_id,
                    'client_name': ordered_schedule.client_user.name,
                })
        else:
            # not an individual training or training not ordered yet or for another week
            result.append({
                'class_id': week_schedule_class.gym_classe.gym_classe_id,
                'class_name': week_schedule_class.gym_classe.name,
                'class_day': week_schedule_class.week_day,
                'class_start': week_schedule_class.start_time,
                'class_stop': _add_minutes(week_schedule_class.start_time,
                                            week_schedule_class.gym_classe.duration),
                'client_id': None,
                'client_name': None
            })
    return result


def describe_group_class(class_id):
    try:
        group_class = m.GymClasse.objects.get(gym_classe_id=class_id)
        return group_class.name, group_class.description
    except m.GymClasse.DoesNotExist:
        return None, None


def describe_client(client_id):
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

    current_date = timezone.now()
    ordered_schedule_training = (
        m.OrderedSchedule.objects
        .select_related('week_schedule')  # join with WeekSchedule
        .filter(client_user=client_id, week_schedule__trainer_id=trainer_id, schedule_date__gte=current_date)
        .order_by('schedule_date')
        .first()
    )
    result = []
    try:
        exercise_plan_id = (m.ExercisePlan.objects
                            .filter(ordered_id=ordered_schedule_training.ordered_schedule_id)
                            .first())
        positions = m.ExercisePlanPosition.objects.filter(exercise_plan=exercise_plan_id).order_by('position')
        for position in positions:
            result.append(
                {
                    'exercise_id': position.exercise.exercise_id,
                    'number': position.repetitions_number if position.repetitions_number != 0 else position.duration/60,
                    'name': position.exercise.name,
                    'position': position.position
                }
            )
    except m.ExercisePlan.DoesNotExist:
        return None, None

    return result, exercise_plan_id.exercise_plan_id


def measured_by_repetition(exercise_id):
    try:
        exercise = m.Exercise.objects.get(exercise_id=exercise_id)
        answer = False
        if exercise.repetitions_number != 0:
            answer = True
        return answer
    except m.Exercise.DoesNotExist:
        return None


def measured_by_duration(exercise_id):
    try:
        exercise = m.Exercise.objects.get(exercise_id=exercise_id)
        answer = True
        if exercise.repetitions_number != 0:
            answer = False
        return answer
    except m.Exercise.DoesNotExist:
        return None


def add_exercise(training_id, exercise_id, measured):
    # find last position in this training
    last_position = m.ExercisePlanPosition.objects.filter(exercise_plan=training_id).order_by('-position').first()
    last_position = last_position.position
    position = last_position + 1
    print(position)
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
            position=last_position+1,
            duration=duration,
            repetitions_number=repetition_number,
            exercise=exercise,
            exercise_plan=plan
            )
        return True
    except Exception as e:
        print(e)
        return None


def can_move_up(pos):
    if pos == 1:
        return False
    else:
        return True


def move_up(training_id, exercise_pos):

    if not can_move_up(exercise_pos):
        # can't move, it is on top of the list
        return None

    try:
        exercise_up = m.ExercisePlanPosition.objects.get(position=exercise_pos-1, exercise_plan_id=training_id)
        exercise = m.ExercisePlanPosition.objects.get(position=exercise_pos, exercise_plan_id=training_id)

        # swap positions of exercises
        exercise_up.position = exercise_pos
        exercise.position = exercise_pos - 1
        exercise_up.save()
        exercise.save()

        return True
    except m.ExercisePlanPosition.DoesNotExist:
        return None


def can_move_down(pos, training_id):
    last_position = m.ExercisePlanPosition.objects.filter(exercise_plan=training_id).order_by('-position').first()
    print(last_position.position)
    if pos == last_position.position:
        print("no")
        return False
    else:
        print("yes")
        return True


def move_down(training_id, exercise_pos):

    if not can_move_down(exercise_pos, training_id):
        # can't move, it is on bottom of the list
        return None

    try:
        exercise_up = m.ExercisePlanPosition.objects.get(position=exercise_pos+1, exercise_plan_id=training_id)
        exercise = m.ExercisePlanPosition.objects.get(position=exercise_pos, exercise_plan_id=training_id)

        # swap positions of exercises
        exercise_up.position = exercise_pos
        exercise.position = exercise_pos + 1
        exercise_up.save()
        exercise.save()

        return True
    except m.ExercisePlanPosition.DoesNotExist:
        return None


def delete_exercise(training_id, exercise_pos):
    try:
        # delete exercise
        exercise_delete = m.ExercisePlanPosition.objects.get(exercise_plan_id=training_id, position=exercise_pos)
        exercise_delete.delete()

        # find all exercises that have lower position
        exercises_down = (m.ExercisePlanPosition.objects
                        .filter(exercise_plan_id=training_id, position__gt=exercise_pos)
                        .order_by('position'))
        for exercise in exercises_down:
            # move every exercise up
            exercise.position = exercise.position - 1
            exercise.save()
        return True
    except m.ExercisePlanPosition.DoesNotExist:
        return None
