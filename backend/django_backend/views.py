from django.http import JsonResponse

def test_message(request):
    data = {
        'id': 1,
        'message': 'Udało się'
    }

    return JsonResponse(data)
