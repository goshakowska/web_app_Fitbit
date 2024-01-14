from django.test import SimpleTestCase, TestCase
import client.discount_calculate as dc
import client.database as database
import database_models.models as models
from datetime import datetime, timedelta

class DiscountTest(SimpleTestCase):
    def test_calculate_price_after_discount_one_percent(self):
        self.assertEqual(dc.calculate_price_after_discount(100, 1), 99)

    def test_calculate_price_after_discount_ten_percent(self):
        self.assertEqual(dc.calculate_price_after_discount(100, 10), 90)

    def test_calculate_price_after_discount_fraction_with_tens_part(self):
        self.assertEqual(dc.calculate_price_after_discount(10, 88), 1.2)

    def test_calculate_price_after_discount_fraction_with_hundredth_part(self):
        self.assertEqual(dc.calculate_price_after_discount(99, 7), 92.07)


class RegistrationTest(TestCase):
    def test_registration(self):
        login = 'testuser'
        password_hash = 'hashedpassword'
        email = 'testuser@example.com'
        phone_number = '123456789'
        name = 'John'
        surname = 'Doe'
        gender = 'M'
        height = 180
        birth_date = '1990-01-01'
        advancement = 'Intermediate'
        target_weight = 70
        training_frequency = 3
        training_time = 60
        training_goal_id = 1
        gym_id = 1
        current_weight = 75

        # Ensure that no client with the given login exists before registration
        self.assertFalse(models.Client.objects.filter(login=login).exists())

        # Call the registration function
        database.registration(
            login, password_hash, email, phone_number, name, surname, gender,
            height, birth_date, advancement, target_weight, training_frequency,
            training_time, training_goal_id, gym_id, current_weight
        )

        # Check if the client has been added to the database
        self.assertTrue(models.Client.objects.filter(login=login).exists())

        # Retrieve the client and check if the data matches the input
        client = models.Client.objects.get(login=login)
        self.assertEqual(client.login, login)
        self.assertEqual(client.password_hash, password_hash)
        self.assertEqual(client.email, email)
        self.assertEqual(client.phone_number, phone_number)
        self.assertEqual(client.name, name)
        self.assertEqual(client.surname, surname)
        self.assertEqual(client.gender, gender)
        self.assertEqual(client.height, height)
        self.assertEqual(client.birth_year, datetime.strptime(birth_date, '%Y-%m-%d').date())
        self.assertEqual(client.advancement, advancement)
        self.assertEqual(client.target_weight, target_weight)
        self.assertEqual(client.training_frequency, training_frequency)
        self.assertEqual(client.training_time, training_time)
        self.assertEqual(client.training_goal_id, training_goal_id)
        self.assertEqual(client.gym_id, gym_id)

        # Check if client data history has been added
        self.assertTrue(models.ClientDataHistory.objects.filter(client=client, weight=current_weight).exists())

        # Check if the measurement date is today
        today = datetime.now().date()
        history_entry = models.ClientDataHistory.objects.get(client=client, weight=current_weight)
        self.assertEqual(history_entry.measurement_date, today)

        # Cleanup: Delete the created client and data history
        client.delete()
        history_entry.delete()