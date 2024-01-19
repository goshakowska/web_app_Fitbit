from django.test import TestCase, Client
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
import json
from unittest.mock import patch, MagicMock

import database_models.models as m
import portier.views as v
import portier.database as db


class CheckStatusClientTestCase(TestCase):

    def setUp(self):
        super().setUp()
        # Create a client and gym ticket for testing
        self.client = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )
        self.client_without_ticket = m.Client.objects.create(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John2',
            surname='Doe2',
            gender='M',
            birth_year='1990-01-01'
            )

        self.ticket_days = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=1,
            name="Standardowy",
            duration=3,
            price=12,
            type="Dniowy"
        )

        self.ticket = m.GymTicketHistory.objects.create(
            gym_ticket_history_id=1,
            client_id=self.client.client_id,
            purchase_date=datetime.now().date() - timedelta(days=10),  # Purchased 10 days ago
            activation_date=datetime.now().date() - timedelta(days=2),  # Activated 2 days ago
            gym_ticket_offer_id=1,
        )

    def test_check_status_client_with_active_ticket(self):
        result = db.check_status_client(self.client.client_id)
        self.assertTrue(result)

    def test_check_status_client_ticket_not_activated(self):
        self.ticket.activation_date = None  # activation date change to None
        self.ticket.save()

        result = db.check_status_client(self.client.client_id)
        self.assertFalse(result)

    def test_check_status_client_with_expired_ticket(self):
        # ticket is for 3 days, change activated 6 days ago
        self.ticket.activation_date = datetime.now().date() - timedelta(days=6)  # Expired
        self.ticket.save()

        result = db.check_status_client(self.client.client_id)
        self.assertFalse(result)

    def test_check_status_client_no_ticket(self):
        result = db.check_status_client(self.client_without_ticket.client_id)
        self.assertFalse(result)


class CheckIfTicketActiveTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.ticket_days = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=1,
            name="Standardowy",
            duration=3,
            price=12,
            type="Dniowy"
        )

        self.ticket_entry = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=2,
            name="Standardowy",
            duration=3,
            price=12,
            type="Wejściowy"
        )

        # create client
        self.client = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )

        # client has ticket daily, active
        self.ticket_daily = m.GymTicketHistory.objects.create(
            gym_ticket_history_id=1,
            client_id=1,
            purchase_date=datetime.now().date() - timedelta(days=10),  # Purchased 10 days ago
            activation_date=datetime.now().date() - timedelta(days=2),  # Activated 2 days ago
            gym_ticket_offer_id=1,
        )

        # client has ticket entry, active
        self.ticket_entries = m.GymTicketHistory.objects.create(
            gym_ticket_history_id=2,
            client_id=1,
            purchase_date=datetime.now().date() - timedelta(days=10),  # Purchased 10 days ago
            activation_date=datetime.now().date() - timedelta(days=2),  # Activated 2 days ago
            gym_ticket_offer_id=2,
        )

        # Create gym visits for the client
        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')
        m.GymVisit.objects.create(entry_time=timezone.now(), gym_gym=self.gym,
                                   client_user=self.client)
        m.GymVisit.objects.create(entry_time=timezone.now(), gym_gym=self.gym,
                                   client_user=self.client)

    def test_check_if_ticket_active_daily(self):
        result = db.check_if_ticket_active(self.ticket_daily, self.client.client_id)
        self.assertTrue(result)

    def test_check_if_ticket_active_entries(self):
        result = db.check_if_ticket_active(self.ticket_entries, self.client.client_id)
        self.assertTrue(result)

    def test_check_if_ticket_expired_daily(self):
        # ticket is for 3 days, activated 6 days ago
        self.ticket_daily.activation_date = datetime.now().date() - timedelta(days=6)  # Expired
        self.ticket_daily.save()

        result = db.check_if_ticket_active(self.ticket_daily, self.client.client_id)
        self.assertFalse(result)

    def test_check_if_ticket_expired_entries(self):
        # create entries more than limit
        m.GymVisit.objects.create(entry_time=timezone.now(), gym_gym=self.gym,
                                   client_user=self.client)
        m.GymVisit.objects.create(entry_time=timezone.now(), gym_gym=self.gym,
                                   client_user=self.client)

        result = db.check_if_ticket_active(self.ticket_entries, self.client.client_id)
        self.assertFalse(result)


class GetClientsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client() # for testing api

    def test_database_get_clients_no_clients(self):
        result = db.get_clients()
        self.assertEqual(result, [])

    def test_view_list_clients_no_clients(self):
        response = self.client.get('/portier/list_clients/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['clients'], [])

    @patch('portier.database.check_status_client', return_value=True)
    def test_database_get_clients(self, mock_check_status_client):
        # create client
        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )

        self.client2 = m.Client.objects.create(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John2',
            surname='Doe2',
            gender='M',
            birth_year='1990-01-01'
            )

        correct_result_1 = {
            'id': self.client1.client_id,
            'phone_number': None,
            'name': self.client1.name,
            'surname': self.client1.surname,
            'status': True
        }

        correct_result_2 = {
            'id': self.client2.client_id,
            'phone_number': None,
            'name': self.client2.name,
            'surname': self.client2.surname,
            'status': True
        }

        result = db.get_clients()

        self.assertIn(correct_result_1, result)
        self.assertIn(correct_result_2, result)

    @patch('portier.database.check_status_client', return_value=True)
    def test_view_list_clients(self, mock_check_status_client):
        # create clients
        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )

        self.client2 = m.Client.objects.create(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John2',
            surname='Doe2',
            gender='M',
            birth_year='1990-01-01'
            )

        correct_result_1 = {
            'id': self.client1.client_id,
            'phone_number': None,
            'name': self.client1.name,
            'surname': self.client1.surname,
            'status': True
        }

        correct_result_2 = {
            'id': self.client2.client_id,
            'phone_number': None,
            'name': self.client2.name,
            'surname': self.client2.surname,
            'status': True
        }
        response = self.client.get('/portier/list_clients/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        self.assertIn(correct_result_1, data['clients'])
        self.assertIn(correct_result_2, data['clients'])


class FindNameSurnameTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client() # for testing api

        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )

        self.client2 = m.Client.objects.create(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John2',
            surname='Doe2',
            gender='M',
            birth_year='1990-01-01'
            )

        self.client3 = m.Client.objects.create(
            login='testuser3',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John3',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01'
            )

    def test_database_find_name_surname_without_name_and_surname(self):
        # Test when both name and surname are None
        result = db.find_name_surname(name=None, surname=None)
        self.assertIsNone(result)

    def test_view_find_client_by_name_surname_without_name_and_surname(self):
        data = {'name': None, 'surname': None}
        response = self.client.post('/portier/find_name_surname/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("This client doesn't exist", data['error'])

    def test_find_name_surname_only_by_surname(self):
        result = db.find_name_surname(name=None, surname='Doe')

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'John')
        self.assertEqual(result[1]['name'], 'John3')

    def test_view_find_client_by_name_surname_only_by_surname(self):
        data = {'name': None, 'surname': 'Doe'}
        response = self.client.post('/portier/find_name_surname/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['clients']), 2)
        self.assertEqual(data['clients'][0]['name'], 'John')
        self.assertEqual(data['clients'][1]['name'], 'John3')

    def test_find_name_surname_only_by_name(self):
        result = db.find_name_surname(name='John', surname=None)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['surname'], 'Doe')

    def test_view_find_client_by_name_surname_only_by_name(self):
        data = {'name': 'John', 'surname': None}
        response = self.client.post('/portier/find_name_surname/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['clients']), 1)
        self.assertEqual(data['clients'][0]['surname'], 'Doe')

    def test_find_name_surname_by_name_and_surname(self):
        result = db.find_name_surname(name='John', surname='Doe')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'John')
        self.assertEqual(result[0]['surname'], 'Doe')

    def test_view_find_client_by_name_surname_by_name_and_surname(self):
        data = {'name': 'John', 'surname': 'Doe'}
        response = self.client.post('/portier/find_name_surname/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['clients']), 1)
        self.assertEqual(data['clients'][0]['surname'], 'Doe')
        self.assertEqual(data['clients'][0]['name'], 'John')

    def test_find_name_surname_no_matching_clients(self):
        result = db.find_name_surname(name='Jane', surname='Smith')
        self.assertIsNone(result)

    def test_view_find_client_by_name_surname_no_matching_clients(self):
        data = {'name': 'Jane', 'surname': 'Smith'}
        response = self.client.post('/portier/find_name_surname/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("This client doesn't exist", data['error'])


class FindPhoneNumberTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()

        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )

        self.client2 = m.Client.objects.create(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            name='John2',
            surname='Doe2',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )

    def test_database_find_phone_number_with_matching_clients(self):
        result = db.find_phone_number(phone_number='11111')

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'John')
        self.assertEqual(result[1]['name'], 'John2')

    def test_view_find_client_by_phone_number_with_matching_clients(self):
        data = {'phone_number': '11111'}
        response = self.client.post('/portier/find_phone_number/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['clients']), 2)
        self.assertEqual(data['clients'][0]['name'], 'John')
        self.assertEqual(data['clients'][1]['name'], 'John2')

    def test_database_find_phone_number_no_matching_clients(self):
        result = db.find_phone_number(phone_number='987654321')
        self.assertIsNone(result)

    def test_view_find_client_by_phone_number_no_matching_clients(self):
        data = {'phone_number': '12345'}
        response = self.client.post('/portier/find_phone_number/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("This client doesn't exist", data['error'])

    def test_database_find_phone_number_none_phone_number(self):
        result = db.find_phone_number(phone_number=None)
        self.assertIsNone(result)

    def test_view_find_client_by_phone_number_none_phone_number(self):
        data = {'phone_number': None}
        response = self.client.post('/portier/find_phone_number/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("This client doesn't exist", data['error'])


class EntryTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='portier',
            employee_id=1,
            email='a@a',
            phone_number='1',
            surname='test_surname',
            gender='M',
            gym=self.gym
        )

        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )

    @patch('django.utils.timezone.now', return_value=timezone.make_aware(timezone.datetime(2024, 1, 18, 12, 30, 0)))
    def test_database_entry_successful(self, mock_now):
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        entry_time = db.entry(self.client1.client_id, portier_id)

        self.assertIsNotNone(entry_time)
        self.assertEquals('12:30 18-01-2024', entry_time)

        # Check if a GymVisit record is created
        gym_visit = m.GymVisit.objects.get(client_user_id=client_id)

        self.assertEqual(gym_visit.gym_gym, self.gym)
        # in database is in UTC and in aplication we use Europe/Warsaw (1 hour differenece)
        self.assertEqual(gym_visit.entry_time.strftime('%H:%M %d-%m-%Y'), '11:30 18-01-2024')

    def test_view_register_entry_successful(self):
        data = {'client_id': self.client1.client_id, 'portier_id': self.employee.employee_id}
        response = self.client.post('/portier/register_entry/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('time', data)

    def test_database_entry_portier_not_existing(self):
        client_id = self.client1.client_id
        portier_id = 999  # An ID that does not exist

        entry_time = db.entry(client_id, portier_id)

        self.assertIsNone(entry_time)

        # Check that no GymVisit record is created
        with self.assertRaises(m.GymVisit.DoesNotExist):
            m.GymVisit.objects.get(client_user_id=client_id)

    def test_view_register_entry_portier_not_existing(self):
        data = {'client_id': self.client1.client_id, 'portier_id': 9999}
        response = self.client.post('/portier/register_entry/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Wrong portier id", data['error'])


class LeaveTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='portier',
            employee_id=1,
            email='a@a',
            phone_number='1',
            surname='test_surname',
            gender='M',
            gym=self.gym
        )

        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )
        self.locker = m.Locker.objects.create(locker_id=1, locker_number=1, gym=self.gym)

    @patch('django.utils.timezone.now', return_value=timezone.make_aware(timezone.datetime(2024, 1, 18, 12, 30, 0)))
    def test_database_leave_successful(self, mock_now):
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        # Register entry
        entry_time = db.entry(client_id, portier_id)
        db.assign_locker(client_id, portier_id)

        # Perform leave
        leave_time, locker_number = db.leave(client_id, portier_id)

        self.assertIsNotNone(leave_time)
        self.assertEquals('12:30 18-01-2024', leave_time)
        self.assertEqual(locker_number, self.locker.locker_number)

        # Check if the GymVisit record is updated
        updated_visit = m.GymVisit.objects.get(client_user_id=client_id)
        # in database is in UTC and in aplication we use Europe/Warsaw (1 hour differenece)
        self.assertEqual(updated_visit.departure_time.strftime('%H:%M %d-%m-%Y'), '11:30 18-01-2024')

    @patch('django.utils.timezone.now', return_value=timezone.make_aware(timezone.datetime(2024, 1, 18, 12, 30, 0)))
    def test_database_leave_successful_no_locker(self, mock_now):
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        # Register entry
        entry_time = db.entry(client_id, portier_id)

        # Perform leave
        leave_time, locker_number = db.leave(client_id, portier_id)

        self.assertIsNotNone(leave_time)
        self.assertEquals('12:30 18-01-2024', leave_time)
        self.assertIsNone(locker_number)

        # Check if the GymVisit record is updated
        updated_visit = m.GymVisit.objects.get(client_user_id=client_id)
        # in database is in UTC and in aplication we use Europe/Warsaw (1 hour differenece)
        self.assertEqual(updated_visit.departure_time.strftime('%H:%M %d-%m-%Y'), '11:30 18-01-2024')

    def test_database_leave_wrong_portier_id(self):
        client_id = self.client1.client_id
        portier_id = 999  # An ID that does not exist

        result = db.leave(client_id, portier_id)

        self.assertIsNone(result[0])
        self.assertIsNone(result[1])

    def test_database_leave_no_registered_visit(self):
        # there is no registered visit for the client
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        result = db.leave(client_id, portier_id)

        self.assertIsNone(result[0])
        self.assertIsNone(result[1])

    def test_database_leave_registered_visit_from_different_day(self):
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        # Register entry from a different day
        entry_time = timezone.now() - timezone.timedelta(days=2)
        m.GymVisit.objects.create(entry_time=entry_time, gym_gym=self.gym, client_user_id=client_id)

        result = db.leave(client_id, portier_id)

        self.assertIsNone(result[0])
        self.assertIsNone(result[1])

    def test_view_register_leave_successful(self):
        # Register entry
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id
        entry_time = db.entry(client_id, portier_id)
        db.assign_locker(client_id, portier_id)

        data = {'client_id': client_id, 'portier_id': portier_id}
        response = self.client.post('/portier/register_leave/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('time', data)
        self.assertEqual(data['locker'], self.locker.locker_number)

    def test_view_register_leave_portier_not_existing(self):
        data = {'client_id': self.client1.client_id, 'portier_id': 99999}
        response = self.client.post('/portier/register_leave/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Wrong portier id or no registered entry", data['error'])


class AssignLockerTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='Test Gym')
        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='portier',
            employee_id=1,
            email='a@a',
            phone_number='1',
            surname='test_surname',
            gender='M',
            gym=self.gym
        )
        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )
        # Create two lockers in the gym
        self.locker1 = m.Locker.objects.create(locker_id=1, locker_number=1, gym=self.gym)
        self.locker2 = m.Locker.objects.create(locker_id=2, locker_number=2, gym=self.gym)

    def test_assign_locker_successful(self):
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        # Register entry
        entry_time = timezone.now() - timezone.timedelta(minutes=30)
        visit = m.GymVisit.objects.create(entry_time=entry_time, gym_gym=self.gym, client_user_id=client_id)

        locker_number = db.assign_locker(client_id, portier_id)

        self.assertIsNotNone(locker_number)
        self.assertEqual(locker_number, self.locker1.locker_number)

        # Check if the GymVisit record is updated
        updated_visit = m.GymVisit.objects.get(client_user_id=client_id)
        self.assertEqual(updated_visit.locker_locker, self.locker1)

    def test_assign_locker_wrong_portier_id(self):
        client_id = self.client1.client_id
        portier_id = 999  # An ID that does not exist

        result = db.assign_locker(client_id, portier_id)

        self.assertIsNone(result)

    def test_assign_locker_no_available_lockers(self):
        # there are no available lockers in the gym
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id

        # Register entry with all lockers occupied
        entry_time = timezone.now() - timezone.timedelta(minutes=30)
        m.GymVisit.objects.create(entry_time=entry_time, gym_gym=self.gym, client_user_id=client_id, locker_locker=self.locker1)
        m.GymVisit.objects.create(entry_time=entry_time, gym_gym=self.gym, client_user_id=client_id, locker_locker=self.locker2)

        result = db.assign_locker(client_id, portier_id)

        self.assertIsNone(result)

    def test_view_assign_locker_successful(self):
        # Register entry
        client_id = self.client1.client_id
        portier_id = self.employee.employee_id
        entry_time = db.entry(client_id, portier_id)

        data = {'client_id': client_id, 'portier_id': portier_id}
        response = self.client.post('/portier/assign_locker/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['locker'], self.locker1.locker_number)

    def test_view_assign_locker_portier_not_existing(self):
        data = {'client_id': self.client1.client_id, 'portier_id': 99999}
        response = self.client.post('/portier/assign_locker/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Wrong portier id or no free locker", data['error'])


class ActivateTicketTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='Test Gym')
        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='portier',
            employee_id=1,
            email='a@a',
            phone_number='1',
            surname='test_surname',
            gender='M',
            gym=self.gym
        )
        self.client1 = m.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='M',
            birth_year='1990-01-01',
            phone_number='11111'
            )
        self.ticket_entry = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=1,
            name="Standardowy",
            duration=3,
            price=12,
            type="Wejściowy"
        )

        # Create an inactive gym ticket
        self.inactive_ticket = m.GymTicketHistory.objects.create(
            gym_ticket_history_id=1,
            client_id=self.client1.client_id,
            purchase_date=datetime.now().date() - timedelta(days=10),  # Purchased 10 days ago
            activation_date=None,  # Inactive
            gym_ticket_offer_id=1,
        )

    def test_activate_ticket_successful(self):
        # Test a successful activation of a ticket
        result = db.activate_ticket(self.client1.client_id, self.inactive_ticket.gym_ticket_history_id)

        self.assertTrue(result)

        # Check if the GymTicketHistory record is updated
        updated_ticket = m.GymTicketHistory.objects.get(gym_ticket_history_id=self.inactive_ticket.gym_ticket_history_id)
        self.assertIsNotNone(updated_ticket.activation_date)

    def test_activate_ticket_client_has_active_ticket(self):
        # Create an active gym ticket
        self.active_ticket = m.GymTicketHistory.objects.create(
            gym_ticket_history_id=2,
            client_id=self.client1.client_id,
            purchase_date=datetime.now().date() - timedelta(days=10),  # Purchased 10 days ago
            activation_date=datetime.now().date() - timedelta(days=1),  # Activated 1 day ago
            gym_ticket_offer_id=1,
        )
        result = db.activate_ticket(self.client1.client_id, self.active_ticket.gym_ticket_history_id)

        self.assertIsNone(result)

    def test_activate_ticket_client_has_no_ticket(self):
        # the client does not have a this ticket to activate
        result = db.activate_ticket(self.client1.client_id, 999)  # An ID that does not exist

        self.assertIsNone(result)

    def test_activate_ticket_invalid_client_id(self):
        # Test when providing an invalid client ID
        result = db.activate_ticket(999, self.inactive_ticket.gym_ticket_history_id)

        self.assertIsNone(result)

    def test_view_activate_ticket_successful(self):
        # Register entry
        client_id = self.client1.client_id
        ticket_id = self.inactive_ticket.gym_ticket_history_id

        data = {'client_id': client_id, 'ticket_id': ticket_id}
        response = self.client.post('/portier/activate_ticket/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['message'], "Ticket activated")

    def test_view_activate_ticket_unsuccesful(self):
        data = {'client_id': self.client1.client_id, 'ticket_id': 99999}
        response = self.client.post('/portier/activate_ticket/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Client has active ticket or doesn't have ticket to activate", data['error'])
