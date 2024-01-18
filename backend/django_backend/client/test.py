from django.test import SimpleTestCase, TestCase, override_settings, Client
from django.core import mail
import client.discount_calculate as dc
from django.contrib.auth.hashers import make_password
import client.database as database
import client.views as views
import database_models.models as models
from datetime import datetime, timedelta
from django.utils import timezone
import pytz
import json

class DiscountTest(SimpleTestCase):

    def test_calculate_price_after_discount_one_percent(self):
        self.assertEqual(dc.calculate_price_after_discount(100, 1), 99)

    def test_calculate_price_after_discount_ten_percent(self):
        self.assertEqual(dc.calculate_price_after_discount(100, 10), 90)

    def test_calculate_price_after_discount_fraction_with_tens_part(self):
        self.assertEqual(dc.calculate_price_after_discount(10, 88), 1.2)

    def test_calculate_price_after_discount_fraction_with_hundredth_part(self):
        self.assertEqual(dc.calculate_price_after_discount(99, 7), 92.07)

class DateToString(SimpleTestCase):

    def test_str_date_valid_date(self):
        date_obj = datetime(2022, 1, 15)
        formatted_date = dc.str_date(date_obj)
        self.assertEqual(formatted_date, "2022-01-15")

    def test_str_date_invalid_date(self):
        formatted_date = dc.str_date(None)
        self.assertIsNone(formatted_date)

    def test_str_hour_valid_time(self):
        time_obj = datetime(1900, 1, 1, 14, 30, 0)
        formatted_time = dc.str_hour(time_obj)
        self.assertEqual(formatted_time, "14:30:00")

    def test_str_hour_invalid_time(self):
        formatted_time = dc.str_hour(None)
        self.assertIsNone(formatted_time)


class RegistrationTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        models.TrainingGoal.objects.create(training_goal_id=1, name='Weight Loss')
        models.Gym.objects.create(
            gym_id=1,
            name='Example Gym',
            phone_number='123456789',
            city='City',
            street='Street',
            house_number='1',
            county='County',
            zip_code='12-345'
        )
        models.Client.objects.create(login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='Male',
            birth_year='1990-01-01')

    def test_registration(self):
        # Test registration function
        database.registration(
            login='testuser2',
            password_hash=make_password('testpassword'),
            email='testuser2@example.com',
            phone_number='1234567890',
            name='John',
            surname='Doe',
            gender='Male',
            height=180,
            birth_date='1990-01-01',
            advancement='Beginner',
            target_weight=70,
            training_frequency=3,
            training_time=60,
            training_goal_id=1,
            gym_id=1,
            current_weight=75
        )
        self.assertTrue(models.Client.objects.filter(login='testuser2').exists())
        self.assertTrue(models.ClientDataHistory.objects.filter(client__login='testuser2', weight=75).exists())

    def test_user_login(self):
        # Test user_login function valid
        authenticated_client = database.user_login('testuser', 'testpassword')
        self.assertIsNotNone(authenticated_client)

    def test_user_login_invalid_credentials(self):
        # Test user_login function invalid
        authenticated_client = database.user_login('testuser', 'wrongpassword')
        self.assertIsNone(authenticated_client)

    def test_is_busy_login(self):
        # Test is_busy_login function
        self.assertTrue(database.is_busy_login('testuser'))
        self.assertFalse(database.is_busy_login('nonexistentuser'))

    def test_is_busy_email(self):
        # Test is_busy_email function
        self.assertTrue(database.is_busy_email('testuser@example.com'))
        self.assertFalse(database.is_busy_email('nonexistent@example.com'))

    def test_registration_success(self):
        # Check if the view registration returns login
        data = {
            'login': 'testuser2',
            'password_hash': 'testpassword',
            'email': 'test2@example.com',
            'phone_number': '1234567890',
            'name': 'John',
            'surname': 'Doe',
            'gender': 'M',
            'height': 180,
            'birth_year': '1990-01-01',
            'advancement': 'beginner',
            'target_weight': 70,
            'training_frequency': 3,
            'training_time': 3,
            'training_goal_id': 1,
            'gym_id': 1,
            'current_weight': 75,
        }
        response = self.client.post('/client/registration/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['login'], 'testuser2')

    def test_registration_invalid_method(self):
        # Check if the view registration returns error
        response = self.client.get('/client/registration/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Invalid request method')

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_send_email(self):
        # Test send_email function
        email_address = 'test@example.com'
        views.send_email(email_address)
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, 'Rejestracja')
        self.assertIn('Dzień dobry!', sent_email.body)
        self.assertIn('Zespół FitBit', sent_email.body)
        self.assertEqual(sent_email.to, [email_address])

    def test_client_login_success(self):
        # Check if the view returns that login and password are valid
        valid_login_data = {
            'login': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/client/client_login/', json.dumps(valid_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'id': 1, 'name': 'John'})

    def test_client_login_failure(self):
        # Check if the view returns that login and password are invalid
        invalid_login_data = {
            'login': 'invalid_username',
            'password': 'invalid_password'
        }
        response = self.client.post('/client/client_login/', json.dumps(invalid_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'error': 'Incorrect user login!'})

    def test_is_busy_login_true(self):
        # Check if the view returns that login is busy
        busy_login_data = { 'login': 'testuser' }
        response = self.client.post('/client/is_busy_login/', json.dumps(busy_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'is_busy': True})

    def test_is_busy_login_false(self):
        # Check if the view returns that login is not busy
        free_login_data = { 'login': 'new_username' }
        response = self.client.post('/client/is_busy_login/', json.dumps(free_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'is_busy': False})

    def test_is_busy_email_true(self):
        # Check if the view returns that email is busy
        data = {'email': 'testuser@example.com'}
        response = self.client.post('/client/is_busy_email/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertTrue(content['is_busy'])

    def test_is_busy_email_false(self):
        # Check if the view returns that email is not busy
        data = {'email': 'new@example.com'}
        response = self.client.post('/client/is_busy_email/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertFalse(content['is_busy'])


class TrainingGoalsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        models.TrainingGoal.objects.create(training_goal_id=1, name='Weight Loss')
        models.TrainingGoal.objects.create(training_goal_id=2, name='Muscle Gain')

    def test_training_goals(self):
        # Test trainingg_goal function
        goals_list = database.training_goals()
        self.assertIsInstance(goals_list, list)
        for goal in goals_list:
            self.assertIsInstance(goal, list)
            self.assertEqual(len(goal), 2)
        self.assertIn([1, 'Weight Loss'], goals_list)
        self.assertIn([2, 'Muscle Gain'], goals_list)

    def test_training_goals(self):
        # Check if the view returns a list of training goals
        response = self.client.get('/client/training_goals/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('goals', content)
        self.assertIsInstance(content['goals'], list)

    def tearDown(self):
        models.TrainingGoal.objects.all().delete()


class GymTicketOfferTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        models.GymTicketOffer.objects.create(gym_ticket_offer_id=1, name='Standard Ticket', duration=30, price=50, type='Standard')
        models.GymTicketOffer.objects.create(gym_ticket_offer_id=2, name='Premium Ticket', duration=60, price=100, type='Premium')

        models.Discount.objects.create(discount_id=1, name='Discount 1', start_date=datetime.now().date(), stop_date=datetime.now().date() + timedelta(days=15), discount_percentages=10, gym_ticket_offer_id=1)
        models.Discount.objects.create(discount_id=2, name='Discount 2', start_date=datetime.now().date(), stop_date=datetime.now().date() + timedelta(days=20), discount_percentages=20, gym_ticket_offer_id=2)

    def test_standard_gym_ticket_offer(self):
        # Test standard_gym_ticket_offer function
        ticket_offers = database.standard_gym_ticket_offer()
        self.assertIsInstance(ticket_offers, list)
        for ticket_offer in ticket_offers:
            self.assertIsInstance(ticket_offer, list)
            self.assertEqual(len(ticket_offer), 4)

    def test_gym_ticket_offer_with_discount(self):
        # Test gym_ticket_offer_with_discount function
        tickets_with_discount = database.gym_ticket_offer_with_discount()
        self.assertIsInstance(tickets_with_discount, list)
        for ticket_with_discount in tickets_with_discount:
            self.assertIsInstance(ticket_with_discount, list)
            self.assertEqual(len(ticket_with_discount), 9)

    def test_standard_gym_ticket_offer(self):
        # Check if the view returns a list of standard gym ticket offers
        response = self.client.get('/client/standard_gym_ticket_offer/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('tickets', content)
        self.assertIsInstance(content['tickets'], list)

    def test_discount_gym_ticket_offer(self):
        # Check if the view returns a list of gym ticket offers with discount
        response = self.client.get('/client/discount_gym_ticket_offer/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('tickets', content)
        self.assertIsInstance(content['tickets'], list)

    def tearDown(self):
        # Clean up after each test if necessary
        models.GymTicketOffer.objects.all().delete()
        models.Discount.objects.all().delete()


class GymFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Create instances of Gym for testing
        models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        models.Gym.objects.create(gym_id=2, name='Gym 2', city='City 2', street='Street 2', house_number='456')

        # Create an instance of Client for testing
        models.Client.objects.create(login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='Male',
            birth_year='1990-01-01')

    def test_get_gyms_list(self):
        # Test get_gyms_list function
        gyms_list = database.get_gyms_list()
        self.assertIsInstance(gyms_list, list)
        for gym_info in gyms_list:
            self.assertIsInstance(gym_info, list)
            self.assertEqual(len(gym_info), 5)

    def test_change_default_gym_client(self):
        # Test change_default_gym_client function
        database.change_default_gym_client(client_id=1, gym_id=2)
        updated_client = models.Client.objects.get(client_id=1)
        self.assertEqual(updated_client.gym.gym_id, 2)

    def test_gyms_list(self):
        # Check if the view returns a list of gyms
        response = self.client.get('/client/gyms_list/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('gyms', content)
        self.assertIsInstance(content['gyms'], list)

    def test_change_default_gym_client(self):
        # Check if the view works good
        data = {'client_id': 1, 'gym_id': 1}
        response = self.client.post('/client/change_default_gym/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('response', content)
        self.assertEqual(content['response'], 'completed')

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.Client.objects.all().delete()

class GymClassFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Create instances of Gym, Trainer, GymClass, Client, OrederedSchedule for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        trainer = models.Employee.objects.create(employee_id=1, login='trainer1', password_hash='hashed_password', email='trainer@example.com', phone_number='123456789', name='John', surname='Doe', gender='M', type='Trainer', gym=gym)
        gym_class = models.GymClasse.objects.create(gym_classe_id=1, name='Class 1', price=20, duration=60)
        week_schedule = models.WeekSchedule.objects.create(week_schedule_id=1, gym_classe=gym_class, trainer=trainer, start_time='10:00:00', week_day='Monday')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym)
        models.OrderedSchedule.objects.create(ordered_schedule_id=1, client_user=client, week_schedule=week_schedule, schedule_date=datetime.now().date(), payment_date=datetime.now().date())

    def test_get_ordered_classes_client(self):
        # Test get_ordered_classes_client function
        classes_list = database.get_ordered_classes_client(client_id=1, start_date='2022-01-01')
        self.assertIsInstance(classes_list, list)
        for gym_class_info in classes_list:
            self.assertIsInstance(gym_class_info, list)
            self.assertEqual(len(gym_class_info), 7)

    def test_get_ordered_gym_classe_details(self):
        # Test get_ordered_gym_classe_details function
        details = database.get_ordered_gym_classe_details(classe_id=1)
        self.assertIsInstance(details, list)
        self.assertEqual(len(details), 9)

    def test_get_week_schedule_details(self):
        # Test get_week_schedule_details function
        details = database.get_week_schedule_details(week_schedule_id=1)
        self.assertIsInstance(details, list)
        self.assertEqual(len(details), 8)

    def test_get_ordered_classes_client(self):
         # Check if the view returns classes
        data = {'client_id': 1, 'start_date': '2024-01-15'}
        response = self.client.post('/client/ordered_classes/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('classes', content)

    def test_get_ordered_gym_classe_details(self):
        # Check if the view returns class' details
        data = {'classe_id': 1}
        response = self.client.post('/client/ordered_classe_details/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('details', content)

    def tearDown(self):
        # Clean up after each test if necessary
        models.OrderedSchedule.objects.all().delete()
        models.Client.objects.all().delete()
        models.WeekSchedule.objects.all().delete()
        models.Employee.objects.all().delete()
        models.GymClasse.objects.all().delete()
        models.Gym.objects.all().delete()


class TrainingFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Create a client and gym visit for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym)
        gym_visit = models.GymVisit.objects.create(gym_visit_id=1, client_user=client, entry_time=datetime.now(pytz.timezone('Europe/Warsaw')), gym_gym=gym)
        exercise = models.Exercise.objects.create(exercise_id=1, name='Exercise 1', type='type 1', calories=1, duration=12, advancement_level='Beginner', repetitions_number=0, description='abc')
        models.ExerciseHistory.objects.create(exercise_history_id=1, client=client, exercise=exercise, exercise_date=datetime.now(pytz.timezone('Europe/Warsaw')), duration=30, repetitions_number=10, calories=150, gym=gym)

    def test_get_training_history(self):
        # Test get_training_history function
        training_history = database.get_training_history(client_id=1)
        self.assertIsInstance(training_history, list)
        for training_info in training_history:
            self.assertIsInstance(training_info, list)
            self.assertEqual(len(training_info), 7)

    def test_get_training_details(self):
        # Test get_training_details function
        training_details = database.get_training_details(training_id=1)
        self.assertIsInstance(training_details, list)
        for exercise_info in training_details:
            self.assertIsInstance(exercise_info, dict)
            self.assertIn('name', exercise_info)
            self.assertIn('start_date', exercise_info)
            self.assertIn('start_hour', exercise_info)
            self.assertIn('duration', exercise_info)
            self.assertIn('repetitions_number', exercise_info)
            self.assertIn('calories', exercise_info)

    def test_get_trainings_client(self):
        # Check if the view returns trainings
        data = {'client_id': 1}
        response = self.client.post('/client/client_trenings/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('trenings', content)

    def test_get_trening_details(self):
        # Check if the view returns training's details
        data = {'training_id': 1}
        response = self.client.post('/client/trening_details/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('details', content)

    def tearDown(self):
        # Clean up after each test if necessary
        models.ExerciseHistory.objects.all().delete()
        models.GymVisit.objects.all().delete()
        models.Client.objects.all().delete()
        models.Exercise.objects.all().delete()

class GymTicketFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Create sample instances for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym)
        gym_ticket_offer = models.GymTicketOffer.objects.create(gym_ticket_offer_id=1, name='Test Offer', duration=30, price=50, type='Dniowy')
        discount = models.Discount.objects.create(discount_id=1, name='Test Discount', start_date=timezone.now().date(), stop_date=timezone.now().date() + timedelta(days=30), discount_percentages=10, gym_ticket_offer=gym_ticket_offer)
        gym_ticket_history = models.GymTicketHistory.objects.create(gym_ticket_history_id=1, purchase_date=timezone.now().date(), activation_date=timezone.now().date(), gym_ticket_offer=gym_ticket_offer, discount=discount, client=client)

    def test_get_gym_ticket_client(self):
        # Test get_gym_ticket_client function
        tickets_list = database.get_gym_ticket_client(client_id=1)
        self.assertEqual(len(tickets_list), 1)
        ticket_info = tickets_list[0]
        self.assertEqual(ticket_info['ticket_name'], 'Test Offer')
        self.assertEqual(ticket_info['type'], 'Dniowy')
        self.assertEqual(ticket_info['duration'], 30)
        self.assertIsNotNone(ticket_info['status'])
        self.assertEqual(ticket_info['discount_name'], 'Test Discount')
        self.assertEqual(ticket_info['discount'], 10)
        self.assertEqual(ticket_info['price'], dc.calculate_price_after_discount(50, 10))
        self.assertIsNotNone(ticket_info['end_date'])

    def test_gym_ticket_details(self):
        # Test gym_ticket_details function
        ticket_details = database.gym_ticket_details(ticket_id=1)
        self.assertEqual(ticket_details['ticket_name'], 'Test Offer')
        self.assertEqual(ticket_details['type'], 'Dniowy')
        self.assertEqual(ticket_details['duration'], 30)
        self.assertIsNotNone(ticket_details['status'])
        self.assertEqual(ticket_details['price_before'], 50)
        self.assertIsNotNone(ticket_details['activation_date'])
        self.assertEqual(ticket_details['discount_name'], 'Test Discount')
        self.assertEqual(ticket_details['discount'], 10)
        self.assertEqual(ticket_details['price_after'], dc.calculate_price_after_discount(50, 10))
        self.assertIsNotNone(ticket_details['end_date'])
        self.assertIsNotNone(ticket_details['days_to_end'])

    def test_get_gym_tickets_client_history(self):
        # Check if the view returns client's gym tickets
        data = {'client_id': 1}
        response = self.client.post('/client/gym_tickets_history/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('tickets', content)

    def test_get_gym_tickets_details(self):
        # Check if the view returns client's gym ticket's details
        data = {'ticket_id': 1}
        response = self.client.post('/client/gym_tickets_details/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('details', content)

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.Client.objects.all().delete()
        models.GymTicketOffer.objects.all().delete()
        models.Discount.objects.all().delete()
        models.GymTicketHistory.objects.all().delete()

class ClientDataTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Create sample instances for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        training_goal = models.TrainingGoal.objects.create(training_goal_id=1, name='Test Goal')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym, training_goal=training_goal, phone_number='123123123')
        models.ClientDataHistory.objects.create(client_data_history_id=1, weight=70, measurement_date='2023-01-01', client=client)

    def test_get_client_data(self):
        # Test get_client_data function
        client_data = database.get_client_data(client_id=1)
        self.assertEqual(client_data['login'], 'testuser')
        self.assertEqual(client_data['email'], 'testuser@example.com')
        self.assertEqual(client_data['phone_number'], '123123123')
        self.assertEqual(client_data['name'], 'John')
        self.assertEqual(client_data['surname'], 'Doe')
        self.assertEqual(client_data['gender'], 'Male')
        self.assertEqual(client_data['height'], None)
        self.assertEqual(client_data['birth_year'], '1990-01-01')
        self.assertEqual(client_data['advancement'], None)
        self.assertEqual(client_data['target_weight'], None)
        self.assertEqual(client_data['training_frequency'], None)
        self.assertEqual(client_data['training_time'], None)
        self.assertEqual(client_data['training_goal'], 'Test Goal')
        self.assertEqual(client_data['gym'], 'Gym 1')
        self.assertEqual(client_data['current_weight'], 70)

    def test_get_client_data(self):
        # Check if the view returns client's data
        data = {'client_id': 1}
        response = self.client.post('/client/client_data/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('client_data', content)

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.TrainingGoal.objects.all().delete()
        models.Client.objects.all().delete()
        models.ClientDataHistory.objects.all().delete()


class TrainerFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Set up necessary data for testing
        gym = models.Gym.objects.create(
            gym_id=1,
            name='Gym 1'
        )
        trainer1 = models.Employee.objects.create(
            employee_id=1,
            login='trainer1',
            password_hash='hashed_password',
            email='trainer@example.com',
            phone_number='123456789',
            name='John',
            surname='Doe',
            gender='M',
            type='trener',
            gym=gym
        )
        trainer2 = models.Employee.objects.create(
            employee_id=2,
            login='trainer2',
            password_hash='hashed_password',
            email='trainer2@example.com',
            phone_number='123456729',
            name='John2',
            surname='Doe2',
            gender='M',
            type='trener',
            gym=gym
        )

    def test_get_trainer_by_gym(self):
        # Test get_trainer_by_gym function
        gym_id = 1
        result = database.get_trainer_by_gym(gym_id)
        self.assertIsInstance(result, list)
        for trainer in result:
            self.assertIsInstance(trainer, list)
            self.assertEqual(len(trainer), 3)
            self.assertIsInstance(trainer[0], int)
            self.assertIsInstance(trainer[1], str)
            self.assertIsInstance(trainer[2], str)
        expected_trainers = [
            [1, 'John', 'Doe'],
            [2, 'John2', 'Doe2'],
        ]
        self.assertEqual(result, expected_trainers)

    def test_get_trainer_by_gym(self):
        # Check if the view returns list of trainers
        data = {'gym_id': 1}
        response = self.client.post('/client/gym_trainers/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('trainers', content)

class GymClassesFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Set up necessary data for testing
        gym = models.Gym.objects.create(
            gym_id=1,
            name='Gym 1',
            city='City 1',
            street='Street 1',
            house_number='123'
        )
        trainer = models.Employee.objects.create(
            employee_id=1,
            login='trainer1',
            password_hash='hashed_password',
            email='trainer@example.com',
            phone_number='123456789',
            name='John',
            surname='Doe',
            gender='M',
            type='Trainer',
            gym=gym
        )
        gym_class1 = models.GymClasse.objects.create(
            gym_classe_id=1,
            name='Class 1',
            price=20,
            duration=60
        )
        gym_class2 = models.GymClasse.objects.create(
            gym_classe_id=2,
            name='Class 2',
            price=25,
            duration=45
        )
        week_schedule1 = models.WeekSchedule.objects.create(
            week_schedule_id=1,
            week_day='Monday',
            start_time='10:00',
            gym_classe=gym_class1,
            trainer=trainer
        )

        week_schedule2 = models.WeekSchedule.objects.create(
            week_schedule_id=2,
            week_day='Wednesday',
            start_time='15:00',
            gym_classe=gym_class2,
            trainer=trainer
        )

    def test_get_gym_classes(self):
        # Test get_gym_classes function
        gym_id = 1
        result = database.get_gym_classes(gym_id)
        self.assertIsInstance(result, list)
        for gym_class in result:
            self.assertIsInstance(gym_class, list)
            self.assertEqual(len(gym_class), 2)
            self.assertIsInstance(gym_class[0], int)
            self.assertIsInstance(gym_class[1], str)
        expected_classes = [
            [1, 'Class 1'],
            [2, 'Class 2'],
        ]
        self.assertEqual(result, expected_classes)

    def test_get_gym_classes(self):
        # Check if the view returns gym classes
        data = {'gym_id': 1}
        response = self.client.post('/client/gym_classes/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('classes', content)

class FreeGymClassesFunctionsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # Set up necessary data for testing
        gym = models.Gym.objects.create(
            gym_id=1,
            name='Gym 1',
            city='City 1',
            street='Street 1',
            house_number='123'
        )
        client = models.Client.objects.create(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
            name='John',
            surname='Doe',
            gender='Male',
            birth_year='1990-01-01',
            gym=gym,
            phone_number='123123123'
        )


        trainer = models.Employee.objects.create(
            employee_id=1,
            login='trainer1',
            password_hash='hashed_password',
            email='trainer@example.com',
            phone_number='123456789',
            name='John',
            surname='Doe',
            gender='M',
            type='Trainer',
            gym=gym

        )

        gym_class = models.GymClasse.objects.create(
            gym_classe_id=1,
            name='Class 1',
            price=20,
            duration=60,
            max_people=2
        )

        week_schedule = models.WeekSchedule.objects.create(
            week_schedule_id=1,
            week_day='Monday',
            start_time='10:00',
            gym_classe=gym_class,
            trainer=trainer
        )

    def test_get_free_trainings(self):
        # Test get_free_trainings function
        trainer_id = 1
        start_date = timezone.now().date()
        client_id = 1
        result = database.get_free_trainings(trainer_id, str(start_date), client_id)
        self.assertIsInstance(result, list)
        for training in result:
            self.assertIsInstance(training, list)
            self.assertEqual(len(training), 9)

    def test_get_free_places_gym_classe(self):
        # Test get_free_places_gym_classe function
        classe_date = timezone.now().date()
        week_schedule_id = 1
        result = database.get_free_places_gym_classe(classe_date, week_schedule_id)
        self.assertIsInstance(result, int)