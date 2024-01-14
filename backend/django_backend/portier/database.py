from django.db.models import Q, F, ExpressionWrapper, fields, Value
from django.utils import timezone
import database_models.models as m
from datetime import datetime, timedelta

def check_status_client(client_id):
    """
    Checks the status of a client, whether they have active ticket or not.

    Args:
        client_id (int): The unique identifier for the client.

    Returns:
        bool: True if the client has an active gym ticket, False otherwise.
    """
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
    """
    Checks if a given gym ticket is still active.

    Args:
        ticket (models.GymTicketHistory): The gym ticket object.
        client_id (int): The unique identifier for the client.

    Returns:
        bool: True if the ticket is still active, False otherwise.
    """

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
    """
    Retrieves a list of all clients along with their basic information and status.

    Returns:
        list: A list of dictionaries containing client details including 'id', 'name', 'surname', and 'status'.
    """
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
    """
    Finds clients based on the provided name and/or surname.

    Args:
        name (str): The name of the client, can be empty or None.
        surname (str): The surname of the client, can be empty or None.

    Returns:
        list or None: A list of dictionaries containing client details including 'name', 'surname', 'status', and 'login'
                      if clients are found. Returns None if no matching clients are found.
    """
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
    """
    Finds clients based on the provided phone number.

    Args:
        phone_number (str): The phone number of the client.

    Returns:
        list or None: A list of dictionaries containing client details including 'name', 'surname', 'status', and 'login'
                      if clients are found. Returns None if no matching clients are found.
    """
    result = []
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
    """
    Records a client's entry into the gym.

    Args:
        client_id (int): The unique identifier for the client.
        portier_id (int): The unique identifier for the employee acting as a "portier."

    Returns:
        datetime or None: Returns the entry time if successful, or None if the specified employee does not exist.
    """
    # find gym where portier works
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    time = timezone.now()
    m.GymVisit.objects.create(entry_time=time, gym_gym=gym, client_user_id=client_id)
    return time


def leave(client_id, portier_id):
    """
    Records a client's departure from the gym and frees the locker.

    Args:
        client_id (int): The unique identifier for the client.
        portier_id (int): The unique identifier for the employee acting as a "portier."

    Returns:
        tuple or None: Returns a tuple containing departure time and locker number if successful, or None if the specified
                       employee does not exist, there is no registered visit, or the visit is from a different day.
    """
    # find gym where portier works
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    # find entry
    visit = (m.GymVisit.objects
             .filter(client_user_id=client_id, gym_gym=gym, departure_time__isnull=True)
             .order_by('-entry_time')
             .first()
             )

    if not visit or visit.entry_time.date() != datetime.now().date():
        # no registered visit or registered visit from different day
        return None

    time = timezone.now()
    visit.departure_time = time
    visit.save()

    # check locker number
    locker = 0
    if visit.locker_locker:
        locker = visit.locker_locker.locker_number
    else:
        locker = None

    return time, locker



def assign_locker(client_id, portier_id):
    """
    Assigns a locker to a client during their gym visit.

    Args:
        client_id (int): The unique identifier for the client.
        portier_id (int): The unique identifier for the employee acting as a "portier."

    Returns:
        int or None: Returns the assigned locker number if successful, or None if the specified
                     employee does not exist, there is no registered visit, or there are no available lockers.
    """
    # find gym where portier works
    try:
        portier = m.Employee.objects.get(employee_id=portier_id)
        gym = portier.gym
    except m.Employee.DoesNotExist:
        return None

    # find entry
    visit = (m.GymVisit.objects
             .filter(client_user_id=client_id, gym_gym=gym, departure_time__isnull=True)
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


def activate_ticket(client_id):
    """
    Activates the gym ticket for a client if it is not already active.

    Args:
        client_id (int): The unique identifier for the client.

    Returns:
        bool or None: Returns True if the activation was successful, None if the client already has an active ticket
                      or if the client does not have a ticket to activate.
    """
    if check_status_client(client_id):
        # client has active ticket
        return None

    ticket_to_activate = (m.GymTicketHistory.objects
                          .filter(
                              client_id=client_id,
                              activation_date__isnull=True
                              )
                          .first())
    if not ticket_to_activate:
        # client doesn't have ticket
        return None

    # activate ticket
    time = datetime.now().date()
    ticket_to_activate.activation_date = time
    ticket_to_activate.save()
    return True
