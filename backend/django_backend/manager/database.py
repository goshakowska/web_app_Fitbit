from django.db.models import Value, Count, Case, When, CharField, ExpressionWrapper, IntegerField, Q, Sum
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


def count_ticket_popularity():
    """
    Count the popularity of gym ticket offers based on the number of purchases
    in the last month.

    Returns:
        Tuple[List[int], List[str]]: A tuple containing two lists:
            - List of purchase counts for each gym ticket offer.
            - List of formatted ticket types (type and duration).
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
            gym_ticket_offer=ticket,
            purchase_date__gte=day,
            purchase_date__lte=last_day
        ).count()
        data_count.append(count)
    return data_count, ticket_types


def ticket_popularity_month():
    """
    Generates a bar chart depicting the popularity of gym ticket types over the last month.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
    data_count, ticket_types = count_ticket_popularity()

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


def count_discount_popularity():
    """
    Count the popularity of gym ticket discounts based on the number of purchases
    in the last month.

    Returns:
        Tuple[List[int], List[str]]: A tuple containing two lists:
            - List of purchase counts for each gym ticket discount.
            - List of distinct discount names.
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
        data_count.append(count)
    return data_count, discount_types


def discount_popularity_month():
    """
    Generates a bar chart depicting the popularity of gym ticket discounts over the last week.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
    data_count, discount_types = count_discount_popularity()


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


def count_age():
    """
    Count the number of clients in different age ranges.

    Returns:
        Tuple[List[str], List[int]]: A tuple containing two lists:
            - List of age ranges.
            - List of corresponding counts of clients in each age range.
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
    age = []
    count = []
    for row in age_counts:
        age.append(row['age_group'])
        count.append(row['count_clients'])
    return age, count


def age_range():
    """
    Generates a bar chart depicting the distribution of clients in different age ranges.

    Returns:
        str: Base64-encoded image of the bar chart.
    """
    age, count = count_age()

    # Plot
    matplotlib.use('Agg')   # non-interactive mode
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


def count_sessions(manager_id):
    """
    Count the number of gym sessions and ordered sessions for each trainer
    in the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        Optional[Tuple[List[int], List[int], List[str]]]: A tuple containing three lists:
            - List of total gym sessions for each trainer in the last month.
            - List of ordered gym sessions for each trainer in the last month.
            - List of trainer names.

        Returns None if the manager with the specified ID does not exist.
    """
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
    return sessions, ordered, trainers_name


def trainer_sessions(manager_id):
    """
    Generate a bar chart depicting the number of gym sessions and ordered sessions
    for each trainer in the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        str: Base64 encoded image representation of the bar chart.
            Returns None if the manager with the specified ID does not exist.
    """
    sessions, ordered, trainers_name = count_sessions(manager_id)

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


def count_clients_week(manager_id):
    """
    Count the number of gym visits for each day in the last week
    for the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        Optional[Tuple[List[str], List[int]]]: A tuple containing two lists:
            - List of dates for the current week.
            - List of corresponding counts of gym visits for each day.

        Returns None if the manager with the specified ID does not exist.
    """
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

        dates.append(f"{day.strftime('%d-%m-%Y')}")
        counts.append(client_count)
        day += timedelta(days=1)

    return dates, counts


def clients_by_week(manager_id):
    """
    Generate a line chart depicting the number of gym visits for each day in the last week
    for the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        str: Base64 encoded image representation of the line chart.
            Returns None if the manager with the specified ID does not exist.
    """
    dates, counts = count_clients_week(manager_id)

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


def count_clients_hour(manager_id):
    """
    Count the number of gym visits for each hour on the previous day
    for the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        Optional[Tuple[List[str], List[int]]]: A tuple containing two lists:
            - List of hours during which gym visits occurred.
            - List of corresponding counts of gym visits for each hour.

        Returns None if the manager with the specified ID does not exist.
    """
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

    times = list(data.keys())
    counts = list(data.values())
    return times, counts


def clients_by_hour(manager_id):
    """
    Generate a bar chart depicting the number of gym visits for each hour on the previous day
    for the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        str: Base64 encoded image representation of the bar chart.
            Returns None if the manager with the specified ID does not exist.
    """
    times, counts = count_clients_hour(manager_id)

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


def count_usage(manager_id, equipment_name):
    """
    Count the usage of a specific gym equipment in hours for each day of the last month
    at the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.
        equipment_name (str): The name of the gym equipment.

    Returns:
        Optional[Tuple[List[str], List[str], dict]]: A tuple containing three elements:
            - List of dates in the format '%d' representing each day of the last month.
            - List of equipment names in the format 'equipment_name gym_equipment_id'.
            - Dictionary containing daily usage in hours for each equipment.

        Returns None if the manager with the specified ID does not exist.
    """
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
            ).aggregate(Sum('duration'))['duration__sum']
            if count is None:
                count = 0
            usage['equipment'].append(f"{equipment.equipment.name} {equipment.gym_equipment_id}")
            usage['hours'].append(count/3600)   # in database stored in seconds

        data[day.strftime('%d')] = usage
        day = day + timedelta(days=1)

    # Process data for plot
    dates = []
    equipment_names = [f"{equipment.equipment.name} {equipment.gym_equipment_id}" for equipment in equipments_id]
    daily_hours = {equip: [] for equip in equipment_names}

    for date, values in data.items():
        dates.append(date)
        for equip, hours in zip(values['equipment'], values['hours']):
            daily_hours[equip].append(hours)

    return dates, equipment_names, daily_hours


def equipment_usage(manager_id, equipment_name):
    """
    Generate a line plot showing the usage of a specific gym equipment over the last month
    at the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.
        equipment_name (str): The name of the gym equipment.

    Returns:
        str: A base64-encoded image of the generated plot.
        Returns None if the manager with the specified ID does not exist
        or if there is an issue generating the plot.
    """

    # calculate last month
    current_date = datetime.now().date()
    last_day = current_date - timedelta(days=current_date.day)
    first_day = last_day.replace(day=1)

    dates, equipment_names, daily_hours = count_usage(manager_id, equipment_name)

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
    """
    Retrieve a list of unique gym equipment names available at the gym where the manager works.

    Args:
        manager_id (int): The ID of the manager.

    Returns:
        List[str]: A list of unique gym equipment names.
        Returns None if the manager with the specified ID does not exist or if there is an issue retrieving the data.
    """
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
