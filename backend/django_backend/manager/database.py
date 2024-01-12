from django.db.models import Value, Count, Case, When, CharField, ExpressionWrapper, IntegerField, F
from django.db.models.functions import ExtractYear
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta
from trainer.database import _current_week
from random import randint
import matplotlib.pyplot as plt
import matplotlib
import io
import base64


def ticket_popularity_week():
    """
    Generates a bar chart depicting the popularity of gym ticket types over the last week.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
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
    matplotlib.use('Agg')   # non-interactive mode
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
    """
    Generates a bar chart depicting the popularity of gym ticket discounts over the last week.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
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
    matplotlib.use('Agg')   # non-interactive mode
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



def age_range():
    """
    Generates a bar chart depicting the distribution of clients in different age ranges.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
    age_ranges = [
        (0, 17, '<18'),
        (18, 24, '18-24'),
        (25, 34, '25-34'),
        (35, 44, '35-44'),
        (45, 54, '45-54'),
        (55, 64, '55-64'),
        (65, 200, '65+')
    ]
    today = datetime.now().date()
    age_expression = ExpressionWrapper(today.year - ExtractYear('birth_year'), output_field=IntegerField())

    # count clients in age ranges
    age_counts = m.Client.objects.annotate(
        age=age_expression
    ).annotate(
        age_group=Case(
            *[When(age__range=(start, end), then=Value(group)) for start, end, group in age_ranges],
            default=Value('Unknown'),
            output_field=CharField()
        )
    ).values('age_group').annotate(count_clients=Count('client_id')).order_by('age_group')

    # Plot
    matplotlib.use('Agg')   # non-interactive mode
    age = []
    count = []
    for row in age_counts:
        age.append(row['age_group'])
        count.append(row['count_clients'])
    plt.figure(figsize=(10, 6))

    bar_width = 0.2
    plt.bar(age, count, width=bar_width, color='#2ecc71')

    plt.title('Rozkład wieku klientów')
    plt.xlabel('Grupa wiekowa')
    plt.ylabel('Liczba klientów')

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64




def trainer_sessions(manager_id):
    # find gym where manager works
    try:
        portier = m.Employee.objects.get(employee_id=manager_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    trainers = m.Employee.objects.all().filter(gym=gym, type="trener")
    trainers_name = []
    sessions = []   # all session for trainer
    ordered = []  # sessions that have been ordered

    # calculate last month
    current_date = datetime.now()
    last = current_date - timedelta(days=current_date.day)
    last_month_year = last.year
    last_month = last.month

    weeks = 4   # there is around 4 weeks in month


    for trainer in trainers:
        trainers_name.append(f"{trainer.name} {trainer.surname}")
        ses_count = m.WeekSchedule.objects.filter(
                         trainer_id=trainer.employee_id,
                         gym_classe__name = "Trening indywidualny"
                         ).count()  # this is for one week
        ses_count = ses_count * weeks   # in month

        ord_count = m.OrderedSchedule.objects.filter(
            week_schedule__trainer_id=trainer.employee_id,
            week_schedule__gym_classe__name="Trening indywidualny",
            schedule_date__month=last_month,
            schedule_date__year=last_month_year
            ).count()
        # sessions.append(ses_count)
        # ordered.append(ord_count)
        sessions.append(randint(20, 40))
        ordered.append(randint(1, 40))


    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    bar_width = 0.3

    colors = ['#3498db', '#85c1e9', '#2ecc71', '#f39c12', '#fb6d4c', '#c0392b']

    bars1 = plt.bar(trainers_name, sessions, bar_width, label='Wszystkie sesje', color=colors[0])
    bars2 = plt.bar(trainers_name, ordered, bar_width, label='Wykupione sesje', color=colors[2])

    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    plt.title('Liczba sesji i sesji wykupionych')
    plt.ylabel('Liczba sesji')
    plt.legend()

    # X labels
    for i, bar in enumerate(bars1):
        if i % 2 == 0:
            plt.text(bar.get_x() + bar.get_width() / 2, -2, trainers_name[i], ha='center', va='center')
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, -4, trainers_name[i], ha='center', va='center')

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64
