from django.db.models import F, ExpressionWrapper, fields, Value
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta
from trainer.database import _current_week
from random import randint
import matplotlib.pyplot as plt
import io
import base64


def ticket_popularity_week():
    ticket_offer = m.GymTicketOffer.objects.all()
    current_week = _current_week()
    # dates for last week
    day = current_week[0] - timedelta(days=7)
    last_day = current_week[1] - timedelta(days=7)
    data = {}
    ticket_types = [f"{ticket.type} ({ticket.duration})" for ticket in ticket_offer]

    while day <= last_day:
        ticket_number = {}
        for ticket in ticket_offer:
            # ticket_number[f"{ticket.type} ({ticket.duration})"] = (m.GymTicketHistory.objects
            #                                                        .filter(gym_ticket_offer = ticket,
            #                                                                purchase_date = day
            #                                                                )
            #                                                        .count()
            #                                                        )
            ticket_number[f"{ticket.type} ({ticket.duration})"] = randint(1, 20)
        data[f"{day.strftime('%d-%m-%Y')}"] = ticket_number
        day += timedelta(days=1)


    # Create plot
    plt.figure(figsize=(10, 6))

    bar_width = 0.1
    index = range(len(data.keys()))

    colors = ['#3498db', '#85c1e9', '#2ecc71', '#f39c12', '#fb6d4c', '#c0392b']

    for i, type in enumerate(ticket_types):
        x_values = [idx + i * bar_width for idx in index]
        y_values = [data[day].get(type, 0) for day in data.keys()]
        plt.bar(x_values, y_values, width=bar_width, label=type, color=colors[i])

    plt.title('Popularność karnetów w zeszłym tygodniu')
    plt.xlabel('Data')
    plt.ylabel('Liczba sprzedanych karnetów')
    plt.xticks(index, data.keys())
    plt.legend()

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64



def discount_popularity_week():
    current_week = _current_week()
    # dates for last week
    day = current_week[0] - timedelta(days=7)
    last_day = current_week[1] - timedelta(days=7)

    data_count = []

    discount_types = m.Discount.objects.values('name').distinct()
    discount_types = [discount['name'] for discount in discount_types]

    for discount in discount_types:
        # count = (m.GymTicketHistory.objects
        #          .filter(discount__name=discount, purchase_date__gte=day, purchase_date__lte=last_day)
        #          .count())
        count = randint(1, 10)
        data_count.append(count)

    print(data_count)

    # Create plot
    plt.figure(figsize=(10, 6))

    bar_width = 0.2
    plt.bar(discount_types, data_count, width=bar_width, color='#2ecc71')

    plt.title('Popularność zniżek w zeszłym tygodniu')
    plt.xlabel('Nazwa zniżki')
    plt.ylabel('Liczba sprzedanych karnetów ze zniżką')

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64
