from django.db.models import Value, Count, Case, When, CharField, ExpressionWrapper, IntegerField, Q
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
    ticket_types = [f"{ticket.type} ({ticket.duration})" for ticket in ticket_offer]

    # calculate last month
    current_date = datetime.now().date()
    last_day = current_date - timedelta(days=current_date.day)
    day = last_day.replace(day=1)
    data_count = []

    for ticket in ticket_offer:
        count = m.GymTicketHistory.objects.filter(
            gym_ticket_offer = ticket,
            purchase_date__gte = day,
            purchase_date__lte = last_day
        ).count()
        # count = randint(20, 60)
        data_count.append(count)

    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    colors = ['#3498db', '#85c1e9', '#2ecc71', '#f39c12', '#fb6d4c', '#c0392b']

    wedges, texts, autotexts = plt.pie(data_count, labels=ticket_types, autopct='', startangle=90, wedgeprops=dict(width=1), colors=colors)

    plt.title('Popularność karnetów w zeszłym miesiącu')
    plt.axis('equal')

    for i, text in enumerate(texts):
        text.set_text(f"{ticket_types[i]}\n{data_count[i]}")

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
    # calculate last month
    current_date = datetime.now().date()
    last_day = current_date - timedelta(days=current_date.day)
    day = last_day.replace(day=1)

    data_count = []

    discount_types = m.Discount.objects.values('name').distinct()
    discount_types = [discount['name'] for discount in discount_types]

    for discount in discount_types:
        count = (m.GymTicketHistory.objects
                 .filter(Q(discount__name=discount) &
                          Q(purchase_date__gte=day) &
                          Q(purchase_date__lte=last_day) &
                          Q(discount__start_date__lte=day) &
                          (Q(discount__stop_date__isnull=True) | Q(discount__stop_date__gte=last_day))
                          )
                 .count())
        # count = randint(1, 10)
        data_count.append(count)


    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))
    colors = ['#3498db', '#85c1e9', '#2ecc71', '#f39c12', '#fb6d4c', '#c0392b']

    wedges, texts, autotexts = plt.pie(data_count, labels=discount_types, autopct='', startangle=90, wedgeprops=dict(width=1), colors=colors)

    plt.title('Popularność zniżek w zeszłym miesiącu')
    plt.axis('equal')

    for i, text in enumerate(texts):
        text.set_text(f"{discount_types[i]}\n{data_count[i]}")

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

    colors = ['#3498db', '#85c1e9', '#2ecc71', '#f39c12', '#fb6d4c', '#c0392b', '#1F618D']

    wedges, texts, autotexts = plt.pie(count, labels=age, autopct='', startangle=90, wedgeprops=dict(width=1), colors=colors)

    plt.axis('equal')

    for i, text in enumerate(texts):
        text.set_text(f"{age[i]}\n{count[i]}")

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

        order = list(m.OrderedSchedule.objects.filter(
            week_schedule__trainer_id=trainer.employee_id,
            week_schedule__gym_classe__name="Trening indywidualny",
            ))
        ord_count = 0
        for ord in order:
            if (ord.schedule_date.month == last_month and
            ord.schedule_date.year == last_month_year):
                ord_count += 1

        sessions.append(ses_count)
        ordered.append(ord_count)
        # sessions.append(randint(20, 40))
        # ordered.append(randint(1, 40))


    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    bar_width = 0.3

    bars1 = plt.bar(trainers_name, sessions, bar_width, label='Wszystkie sesje', color='#3498db')
    bars2 = plt.bar(trainers_name, ordered, bar_width, label='Wykupione sesje', color='#2ecc71')

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



def clients_by_week(manager_id):
     # find gym where manager works
    try:
        portier = m.Employee.objects.get(employee_id=manager_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    current_week = _current_week()

    # dates for last week
    day = current_week[0] - timedelta(days=7)
    last_day = current_week[1] - timedelta(days=7)
    dates = []
    counts = []

    while day <= last_day:
        clients = m.GymVisit.objects.filter(
            gym_gym=gym,
        )
        client_count=0
        for client in clients:
            if client.entry_time.date() == day:
                client_count+=1

        # client_count = randint(20, 50)
        dates.append(f"{day.strftime('%d-%m-%Y')}")
        counts.append(client_count)
        day += timedelta(days=1)

    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    plt.plot(dates, counts, marker='o', color='#3498db')

    plt.ylim(bottom=0)

    plt.title('Wejścia na siłownie w tygodniu')
    plt.xlabel('Data')
    plt.ylabel('Liczba wejść')

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64


def clients_by_hour(manager_id):
     # find gym where manager works
    try:
        portier = m.Employee.objects.get(employee_id=manager_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    data = {}

    current_day = datetime.now().date()
    yesterday = current_day - timedelta(days=1)
    yesterday = yesterday.day
    entries = m.GymVisit.objects.filter(
            gym_gym=gym,
        ).order_by('entry_time')
    for entry in entries:
        if entry.entry_time.day == yesterday:
            time_zone = entry.entry_time + timedelta(hours=1)
            time = time_zone.time().strftime('%H:%M')
            if time in data:
                data[time] += 1
            else:
                data[time] = 1
    # data = {
    #     '9:00': 7,
    #     '10:00': 5,
    #     '10:30': 6,
    #     '11:00': 8,
    #     '12:00': 9
    # }

    times = list(data.keys())
    counts = list(data.values())

    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    plt.bar(times, counts, color='#3498db')

    plt.ylim(bottom=0)

    plt.title('Wejścia na siłownie w ciągu zeszłego dnia')
    plt.xlabel('Godzina')
    plt.ylabel('Liczba wejść')

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64



def equipment_usage(manager_id, equipment_name):
     # find gym where manager works
    try:
        portier = m.Employee.objects.get(employee_id=manager_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    data = {}

    # calculate last month
    current_date = datetime.now().date()
    last_day = current_date - timedelta(days=current_date.day)
    day = last_day.replace(day=1)
    first_day = last_day.replace(day=1)

    equipments_id = m.GymEquipment.objects.filter(gym=gym, equipment__name=equipment_name)

    while day <= last_day:
        usage = {
            'hours': [],
            'equipment': []
        }
        for equipment in equipments_id:
            count = m.ExerciseHistory.objects.filter(
                gym=gym,
                gym_equipment=equipment,
                exercise_date__date=day
            ).count()
            usage['equipment'].append(f"{equipment.equipment.name} {equipment.gym_equipment_id}")
            usage['hours'].append(count/3600)   # in database stored in seconds

        data[day.strftime('%d')] = usage
        day = day + timedelta(days=1)

    print(data)

    data = {
    '01': {'hours': [8, 10, 15], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '02': {'hours': [9, 11, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '03': {'hours': [8, 12, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '04': {'hours': [10, 13, 19], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '05': {'hours': [9, 12, 16], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '06': {'hours': [8, 12, 17], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '07': {'hours': [7, 13, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '08': {'hours': [9, 15, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '09': {'hours': [9, 15, 19], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '10': {'hours': [11, 12, 20], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '11': {'hours': [10, 14, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '12': {'hours': [9, 13, 19], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '13': {'hours': [9, 13, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '14': {'hours': [7, 15, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '15': {'hours': [7, 12, 19], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
    '16': {'hours': [9, 13, 18], 'equipment': ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']},
}


    # Process data for plot
    dates = []
    # equipment_names = [f"{equipment.equipment.name} {equipment.gym_equipment_id}" for equipment in equipments_id]
    equipment_names = ['Sprzęt A', 'Sprzęt B', 'Sprzęt C']
    daily_hours = {equip: [] for equip in equipment_names}

    for date, values in data.items():
        dates.append(date)
        for equip, hours in zip(values['equipment'], values['hours']):
            daily_hours[equip].append(hours)

    # Create plot
    matplotlib.use('Agg')   # non-interactive mode
    plt.figure(figsize=(10, 6))

    for equip in equipment_names:
        plt.plot(dates, daily_hours[equip], label=equip, marker='o')

    plt.title(f'Wykorzystanie sprzętu na siłowni {first_day.strftime("%d/%m/%Y")} - {last_day.strftime("%d/%m/%Y")}')
    plt.xlabel('Data')
    plt.ylabel('Liczba godzin korzystania')
    plt.legend()

    # Save image in memory
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='jpeg')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()

    return image_base64


def all_equipment(manager_id):
    # find gym where manager works
    try:
        portier = m.Employee.objects.get(employee_id=manager_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    equipment = m.GymEquipment.objects.filter(gym=gym)
    equipment_name = []
    for eqp in equipment:
        equipment_name.append(eqp.equipment.name)

    return list(set(equipment_name))
