from database_models.models import Employee
from django.contrib.auth.hashers import check_password


def portier_validate_login(login, password):
    try:
        portier = Employee.objects.get(login=login)
        is_correct = check_password(password, portier.password_hash)
        if is_correct:
            return portier.employee_id, portier.name
        else:
            return None, None
    except Employee.DoesNotExist:
        return None, None
