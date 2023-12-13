import database_models.models as m
from datetime import datetime, timedelta


def _is_date_in_current_week(check_date):
    current_date = datetime.now()
    current_weekday = current_date.weekday()

    days_until_monday = current_weekday
    monday_of_current_week = current_date - timedelta(days=days_until_monday)

    return monday_of_current_week <= check_date <= (monday_of_current_week + timedelta(days=6))



def get_classes_for_trainer(trainer_id):
    week_schedule_classes = m.WeekSchedule.objects.filter(trainer_id=trainer_id)
    result = []

    for week_schedule_class in week_schedule_classes:
        # check if it is individual training
        if week_schedule_class.gym_classe.name == 'zajęcia indywidualne':
            ordered_schedule = m.OrderedSchedule.objects.filter(
                week_schedule=week_schedule_class.week_schedule_id
            ).first()
            # if it is ordered add client's data
            if ordered_schedule:
                result.append({
                    'class_id': week_schedule_class.gym_classe.gym_classe_id,
                    'class_name': week_schedule_class.gym_classe.name,
                    'client_id': ordered_schedule.client_user.client_id,
                    'client_name': ordered_schedule.client_user.name,
                })
        else:
            # not an individual training or training not ordered yet
            result.append({
                'class_id': week_schedule_class.gym_classe.gym_classe_id,
                'class_name': week_schedule_class.gym_classe.name,
                'client_id': None,
                'client_name': None
            })
    return result
