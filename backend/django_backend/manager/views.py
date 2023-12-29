from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import manager.database as database


@csrf_exempt
def ticket_popularity_week(request):
    """
    Retrieves the popularity of gym tickets for the past week and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for ticket popularity in the past week.
    """
    data = database.ticket_popularity_week()

    return JsonResponse({'plot':data})


@csrf_exempt
def discount_popularity_week(request):
    """
    Retrieves the popularity of gym ticket discounts for the past week and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for discount popularity in the past week.
    """
    data = database.discount_popularity_week()

    return JsonResponse({'plot':data})


@csrf_exempt
def count_age_range(request):
    """
    Counts the distribution of clients across different age ranges and returns a plot.

    Args:
        request (HttpRequest): The HTTP request object (no data needed).

    Returns:
        JsonResponse: A JSON response containing the plot data for the distribution of clients across age ranges.
    """
    data = database.age_range()

    return JsonResponse({'plot':data})
