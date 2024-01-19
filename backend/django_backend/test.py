from django.test import TestCase, Client
from django.contrib.auth.hashers import make_password
import json

from database_models.models import Employee, Gym
from views import employee_validate_login


class EmployeeLoginTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()

        # create gym
        gym = Gym(gym_id=1, name='test_gym')
        gym.save()

        # create employee
        self.login = 'test_employee'
        self.password = 'test_password'

        self.employee = Employee(
            login=self.login,
            password_hash=make_password(self.password),
            name='test_name',
            type='trener',
            employee_id=1,
            email='a@a',
            phone_number='1',
            surname='test_surname',
            gender='M',
            gym=Gym(gym_id=1, name='test')
        )

        self.employee.save()

    def test_database_employee_validate_login_correct(self):
        employee_id, name, type = employee_validate_login(self.login, self.password)
        self.assertEqual(employee_id, self.employee.employee_id)
        self.assertEqual(name, self.employee.name)
        self.assertEqual(type, self.employee.type)

    def test_database_employee_validate_login_incorrect_password(self):
        employee_id, name, type = employee_validate_login(self.login, 'incorrect_password')
        self.assertIsNone(employee_id)
        self.assertIsNone(name)
        self.assertIsNone(type)

    def test_database_employee_validate_login_incorrect_login(self):
        employee_id, name, type = employee_validate_login('incorrect_login', self.password)
        self.assertIsNone(employee_id)
        self.assertIsNone(name)
        self.assertIsNone(type)

    def test_view_employee_login_correct(self):
        data = {'login': self.login, 'password': self.password}
        response = self.client.post('/employee/login/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['id'], self.employee.employee_id)
        self.assertEqual(data['name'], self.employee.name)
        self.assertEqual(data['type'], self.employee.type)

    def test_view_employee_login_incorrect_password(self):
        data = {'login': self.login, 'password': 'incorrect_password'}
        response = self.client.post('/employee/login/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('Incorrect employee login or password', data['message'])

    def test_view_employee_login_incorrect_login(self):
        data = {'login': 'incorrect_login', 'password': self.password}
        response = self.client.post('/employee/login/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('Incorrect employee login or password', data['message'])
