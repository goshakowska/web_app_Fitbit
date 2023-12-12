from database_models.models import Employee
from django.contrib.auth.hashers import check_password


def trainer_validate_login(login, password):
    try:
        trainer = Employee.objects.get(login=login)
        is_correct = check_password(password, trainer.password_hash)
        if is_correct:
            return trainer.employee_id, trainer.name
        else:
            return None, None
    except Employee.DoesNotExist:
        return None, None
