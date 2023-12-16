from django.db.models import Q, F, ExpressionWrapper, fields, Value
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta

def check_status_client(client_id):
    ticket = (m.GymTicketHistory.objects
              .filter(client_id=client_id)
              )
    if not ticket:
        # client doesn't have ticket
        return False

    # find nearest active ticket (can only by one active at a time)
    ticket_active = (m.GymTicketHistory.objects
              .filter(client_id=client_id, activation_date__isnull=False)
              .order_by('purchase_date')
              .first()
              )

    if not ticket_active:
        # ticket hasn't been activated yet
        return False

    # check if still active
    if check_if_ticket_active(ticket_active, client_id):
        # is active
        return True
    else:
        # not active
        return False


def check_if_ticket_active(ticket, client_id):
    # check if still active

    if ticket.gym_ticket_offer.type == "Dniowy":
        # ticket is for time
        end_date = ticket.activation_date + timedelta(days=ticket.gym_ticket_offer.duration)
        current_date = timezone.now().date()
        if current_date > end_date:
            # ticket has expired
            return False
        else:
            return True

    else:
        # ticket is for number of entries
        entries = m.GymVisit.objects.filter(client_user=client_id).count()
        limit_entries = ticket.gym_ticket_offer.duration
        if entries > limit_entries:
            # ticket has expired
            return False
        else:
            return True



def get_clients():
    clients = m.Client.objects.all()
    result = []
    for client in clients:
        result.append(
            {
                'id': client.client_id,
                'name': client.name,
                'surname': client.surname,
                'status': check_status_client(client.client_id)
            }
        )

    return result



def find_name_surname(name, surname):
    result = []
    if not name:
        # find only by surname
        clients = m.Client.objects.filter(surname=surname)
        for client in clients:
            result.append(
                {
                    'name': client.name,
                    'surname': client.surname,
                    'status': check_status_client(client.client_id),
                    'login': client.login,
                }
            )

    elif not surname:
        # find only by name
        clients = m.Client.objects.filter(name=name)
        for client in clients:
            result.append(
                {
                    'name': client.name,
                    'surname': client.surname,
                    'status': check_status_client(client.client_id),
                    'login': client.login,
                }
            )

    else:
        # find by name and surname
        clients = m.Client.objects.filter(name=name, surname=surname)
        for client in clients:
            result.append(
                {
                    'name': client.name,
                    'surname': client.surname,
                    'status': check_status_client(client.client_id),
                    'login': client.login,
                }
            )

    if not result:
        # given client doesn't exist
        return None

    return result


def find_phone_number(phone_number):
    result = []
    # find by phone_number
    clients = m.Client.objects.filter(phone_number=phone_number)
    for client in clients:
        result.append(
            {
                'name': client.name,
                'surname': client.surname,
                'status': check_status_client(client.client_id),
                'login': client.login,
            }
        )

    if not result:
        # given client doesn't exist
        return None

    return result


def entry(client_id, portier_id):
    # find gym
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    time = datetime.now()
    m.GymVisit.objects.create(entry_time=time, gym_gym=gym, client_user_id=client_id)
    return time


def leave(client_id, portier_id):
    # find gym
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    # find entry
    visit = (m.GymVisit.objects
             .filter(client_user_id=client_id, gym_gym=gym)
             .order_by('-entry_time')
             .first()
             )

    if not visit or visit.entry_time.date() != datetime.now().date():
        # no registered visit or registered visit from different day
        return None

    time = datetime.now()
    visit.departure_time = time
    visit.save()
    return time



def assign_locker(client_id, portier_id):
    # find gym
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    # find entry
    visit = (m.GymVisit.objects
             .filter(client_user_id=client_id, gym_gym=gym)
             .order_by('-entry_time')
             .first()
             )

    # find free locker

    exclude_locker = m.GymVisit.objects.filter(departure_time__isnull=True, gym_gym=gym, locker_locker__isnull=False)
    exclude_id = []     # locker_id that are in use
    for locker_ex in exclude_locker:
        exclude_id.append(locker_ex.locker_locker.locker_id)

    locker = m.Locker.objects.filter(gym=gym).exclude(locker_id__in=exclude_id).first()
    if not locker:
        # no free locker
        return None
    visit.locker_locker = locker
    visit.save()
    return locker.locker_number