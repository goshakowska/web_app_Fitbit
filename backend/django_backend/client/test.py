from django.test import SimpleTestCase, TestCase
import client.discount_calculate as dc
from django.contrib.auth.hashers import make_password
import client.database as database
import database_models.models as models
from datetime import datetime, timedelta
from django.utils import timezone
import pytz

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
        # Test str_date with a valid date object
        date_obj = datetime(2022, 1, 15)
        formatted_date = dc.str_date(date_obj)
        self.assertEqual(formatted_date, "2022-01-15")

    def test_str_date_invalid_date(self):
        # Test str_date with an invalid date object (None)
        formatted_date = dc.str_date(None)
        self.assertIsNone(formatted_date)

    def test_str_hour_valid_time(self):
        # Test str_hour with a valid time object
        time_obj = datetime(1900, 1, 1, 14, 30, 0)
        formatted_time = dc.str_hour(time_obj)
        self.assertEqual(formatted_time, "14:30:00")

    def test_str_hour_invalid_time(self):
        # Test str_hour with an invalid time object (None)
        formatted_time = dc.str_hour(None)
        self.assertIsNone(formatted_time)


class RegistrationTestCase(TestCase):
    def setUp(self):
        # Create necessary related objects before running the tests
        # Ensure that valid data is used for foreign keys
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

    def test_registration(self):
        database.registration(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
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
        self.assertTrue(models.Client.objects.filter(login='testuser').exists())
        self.assertTrue(models.ClientDataHistory.objects.filter(client__login='testuser', weight=75).exists())

    def test_user_login(self):
        database.registration(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
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
        authenticated_client = database.user_login('testuser', 'testpassword')
        self.assertIsNotNone(authenticated_client)

    def test_user_login_invalid_credentials(self):
        database.registration(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
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
        authenticated_client = database.user_login('testuser', 'wrongpassword')
        self.assertIsNone(authenticated_client)

    def test_is_busy_login(self):
        database.registration(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
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
        self.assertTrue(database.is_busy_login('testuser'))
        self.assertFalse(database.is_busy_login('nonexistentuser'))

    def test_is_busy_email(self):
        database.registration(
            login='testuser',
            password_hash=make_password('testpassword'),
            email='testuser@example.com',
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
        self.assertTrue(database.is_busy_email('testuser@example.com'))
        self.assertFalse(database.is_busy_email('nonexistent@example.com'))


class TrainingGoalsTestCase(TestCase):
    def setUp(self):
        # Create instances of TrainingGoal for testing
        models.TrainingGoal.objects.create(training_goal_id=1, name='Weight Loss')
        models.TrainingGoal.objects.create(training_goal_id=2, name='Muscle Gain')

    def test_training_goals(self):
        # Test the training_goals function
        goals_list = database.training_goals()

        # Ensure that the result is a list
        self.assertIsInstance(goals_list, list)

        # Ensure that each item in the list is also a list with two elements
        for goal in goals_list:
            self.assertIsInstance(goal, list)
            self.assertEqual(len(goal), 2)

        # Ensure that the expected goals are present in the result
        self.assertIn([1, 'Weight Loss'], goals_list)
        self.assertIn([2, 'Muscle Gain'], goals_list)

    def tearDown(self):
        # Clean up after each test if necessary
        models.TrainingGoal.objects.all().delete()


class GymTicketOfferTestCase(TestCase):
    def setUp(self):
        # Create instances of GymTicketOffer for testing
        models.GymTicketOffer.objects.create(gym_ticket_offer_id=1, name='Standard Ticket', duration=30, price=50, type='Standard')
        models.GymTicketOffer.objects.create(gym_ticket_offer_id=2, name='Premium Ticket', duration=60, price=100, type='Premium')

        # Create instances of Discount for testing
        models.Discount.objects.create(discount_id=1, name='Discount 1', start_date=datetime.now().date(), stop_date=datetime.now().date() + timedelta(days=15), discount_percentages=10, gym_ticket_offer_id=1)
        models.Discount.objects.create(discount_id=2, name='Discount 2', start_date=datetime.now().date(), stop_date=datetime.now().date() + timedelta(days=20), discount_percentages=20, gym_ticket_offer_id=2)

    def test_standard_gym_ticket_offer(self):
        # Test standard_gym_ticket_offer function
        ticket_offers = database.standard_gym_ticket_offer()

        # Ensure that the result is a list
        self.assertIsInstance(ticket_offers, list)

        # Ensure that each item in the list is also a list with four elements
        for ticket_offer in ticket_offers:
            self.assertIsInstance(ticket_offer, list)
            self.assertEqual(len(ticket_offer), 4)

    def test_gym_ticket_offer_with_discount(self):
        # Test gym_ticket_offer_with_discount function
        tickets_with_discount = database.gym_ticket_offer_with_discount()

        # Ensure that the result is a list
        self.assertIsInstance(tickets_with_discount, list)

        # Ensure that each item in the list is also a list with eight elements
        for ticket_with_discount in tickets_with_discount:
            self.assertIsInstance(ticket_with_discount, list)
            self.assertEqual(len(ticket_with_discount), 9)

    def tearDown(self):
        # Clean up after each test if necessary
        models.GymTicketOffer.objects.all().delete()
        models.Discount.objects.all().delete()


class GymFunctionsTestCase(TestCase):
    def setUp(self):
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

        # Ensure that the result is a list
        self.assertIsInstance(gyms_list, list)

        # Ensure that each item in the list is also a list with five elements
        for gym_info in gyms_list:
            self.assertIsInstance(gym_info, list)
            self.assertEqual(len(gym_info), 5)

    def test_change_default_gym_client(self):
        # Test change_default_gym_client function
        database.change_default_gym_client(client_id=1, gym_id=2)

        # Retrieve the updated client and check if the default gym has been changed
        updated_client = models.Client.objects.get(client_id=1)
        self.assertEqual(updated_client.gym.gym_id, 2)

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.Client.objects.all().delete()

class GymClassFunctionsTestCase(TestCase):
    def setUp(self):
        # Create instances of Gym, Trainer, GymClass, Client for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        trainer = models.Employee.objects.create(employee_id=1, login='trainer1', password_hash='hashed_password', email='trainer@example.com', phone_number='123456789', name='John', surname='Doe', gender='M', type='Trainer', gym=gym)
        gym_class = models.GymClasse.objects.create(gym_classe_id=1, name='Class 1', price=20, duration=60)
        week_schedule = models.WeekSchedule.objects.create(week_schedule_id=1, gym_classe=gym_class, trainer=trainer, start_time='10:00:00', week_day='Monday')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym)

        # Create instances of OrderedSchedule for testing
        models.OrderedSchedule.objects.create(ordered_schedule_id=1, client_user=client, week_schedule=week_schedule, schedule_date=datetime.now().date(), payment_date=datetime.now().date())

    def test_get_ordered_classes_client(self):
        # Test get_ordered_classes_client function
        classes_list = database.get_ordered_classes_client(client_id=1, start_date='2022-01-01')

        # Ensure that the result is a list
        self.assertIsInstance(classes_list, list)

        # Ensure that each item in the list is also a list with seven elements
        for gym_class_info in classes_list:
            self.assertIsInstance(gym_class_info, list)
            self.assertEqual(len(gym_class_info), 7)

    def test_get_ordered_gym_classe_details(self):
        # Test get_ordered_gym_classe_details function
        details = database.get_ordered_gym_classe_details(classe_id=1)

        # Ensure that the result is a list
        self.assertIsInstance(details, list)

        # Ensure that the list has 10 elements
        self.assertEqual(len(details), 9)

    def test_get_week_schedule_details(self):
        # Test get_week_schedule_details function
        details = database.get_week_schedule_details(week_schedule_id=1)

        # Ensure that the result is a list
        self.assertIsInstance(details, list)

        # Ensure that the list has 8 elements
        self.assertEqual(len(details), 8)

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
        # Create a client and gym visit for testing
        gym = models.Gym.objects.create(gym_id=1, name='Gym 1', city='City 1', street='Street 1', house_number='123')
        client = models.Client.objects.create(login='testuser', password_hash=make_password('testpassword'), email='testuser@example.com', name='John', surname='Doe', gender='Male', birth_year='1990-01-01', gym=gym)
        gym_visit = models.GymVisit.objects.create(gym_visit_id=1, client_user=client, entry_time=datetime.now(pytz.timezone('Europe/Warsaw')), gym_gym=gym)
        # Create an exercise history entry for testing
        exercise = models.Exercise.objects.create(exercise_id=1, name='Exercise 1', type='type 1', calories=1, duration=12, advancement_level='Beginner', repetitions_number=0, description='abc')
        models.ExerciseHistory.objects.create(exercise_history_id=1, client=client, exercise=exercise, exercise_date=datetime.now(pytz.timezone('Europe/Warsaw')), duration=30, repetitions_number=10, calories=150, gym=gym)

    def test_get_training_history(self):
        # Test get_training_history function
        training_history = database.get_training_history(client_id=1)

        # Ensure that the result is a list
        self.assertIsInstance(training_history, list)

        # Ensure that each item in the list is also a list with seven elements
        for training_info in training_history:
            self.assertIsInstance(training_info, list)
            self.assertEqual(len(training_info), 7)

    def test_get_training_details(self):
        # Test get_training_details function
        training_details = database.get_training_details(training_id=1)

        # Ensure that the result is a list
        self.assertIsInstance(training_details, list)

        # Ensure that each item in the list is a dictionary with the expected keys
        for exercise_info in training_details:
            self.assertIsInstance(exercise_info, dict)
            self.assertIn('name', exercise_info)
            self.assertIn('start_date', exercise_info)
            self.assertIn('start_hour', exercise_info)
            self.assertIn('duration', exercise_info)
            self.assertIn('repetitions_number', exercise_info)
            self.assertIn('calories', exercise_info)

    def tearDown(self):
        # Clean up after each test if necessary
        models.ExerciseHistory.objects.all().delete()
        models.GymVisit.objects.all().delete()
        models.Client.objects.all().delete()
        models.Exercise.objects.all().delete()

class GymTicketFunctionsTestCase(TestCase):
    def setUp(self):
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

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.Client.objects.all().delete()
        models.GymTicketOffer.objects.all().delete()
        models.Discount.objects.all().delete()
        models.GymTicketHistory.objects.all().delete()

class ClientDataTestCase(TestCase):
    def setUp(self):
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

    def tearDown(self):
        # Clean up after each test if necessary
        models.Gym.objects.all().delete()
        models.TrainingGoal.objects.all().delete()
        models.Client.objects.all().delete()
        models.ClientDataHistory.objects.all().delete()