from database_models.models import Employee
from django.contrib.auth.hashers import check_password


def manager_validate_login(login, password):
    try:
        manager = Employee.objects.get(login=login)
        is_correct = check_password(password, manager.password_hash)
        if is_correct:
            return manager.employee_id, manager.name
        else:
            return None, None
    except Employee.DoesNotExist:
        return None, None
