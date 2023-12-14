from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from database_models.models import Employee
from django.contrib.auth.hashers import check_password



@csrf_exempt  # Ignoruje CSRF dla uproszczenia
def modify_number(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        received_number = data.get('number', 0)
        modified_number = received_number * 2  # Modyfikacja: Podwaja liczbę
        return JsonResponse({'result': modified_number})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def test_message(request):
    data = {
        'id': 1,
        'message': 'Udało się'
    }

    return JsonResponse(data)





def employee_validate_login(login, password):
    try:
        employee = Employee.objects.get(login=login)
        is_correct = check_password(password, employee.password_hash)
        if is_correct:
            return employee.employee_id, employee.name, employee.type
        else:
            return None, None, None
    except Employee.DoesNotExist:
        return None, None, None

@csrf_exempt
def employee_login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get('login')
    password = data.get('password')
    id, name, type = employee_validate_login(login, password)
    if id:
        return JsonResponse({'id':id, 'name': name, 'type': type})
    else:
        raise JsonResponse({'error': "Incorrect employee login or password"}, status=400)
