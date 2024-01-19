from django.test import TestCase, Client
from django.contrib.auth.hashers import make_password
import json

import database_models.models as m
import simulation.database as db
import portier.database as portier


class TestGetAllClients(TestCase):
    def setUp(self):
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

    def test_get_all_clients(self):
        # register visit for both clients
        portier.entry(self.client1.client_id, self.employee.employee_id)
        portier.entry(self.client2.client_id, self.employee.employee_id)

        correct_result_1 = [
            self.client1.client_id,
            self.client1.name,
            self.client1.surname
        ]

        correct_result_2 = [
            self.client2.client_id,
            self.client2.name,
            self.client2.surname,
        ]

        result = db.get_all_clients(self.gym.gym_id)

        self.assertIn(correct_result_1, result)
        self.assertIn(correct_result_2, result)

    def test_view_get_all_clients(self):
        # register visit for both clients
        portier.entry(self.client1.client_id, self.employee.employee_id)
        portier.entry(self.client2.client_id, self.employee.employee_id)
        correct_result_1 = [
            self.client1.client_id,
            self.client1.name,
            self.client1.surname
        ]

        correct_result_2 = [
            self.client2.client_id,
            self.client2.name,
            self.client2.surname,
        ]
        data = {'gym_id': self.gym.gym_id}
        response = self.client.post('/simulation/all_clients/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn(correct_result_1, data['clients'])
        self.assertIn(correct_result_2, data['clients'])


class TestGetAllGyms(TestCase):
    def setUp(self):
        self.client = Client()

        self.gym1 = m.Gym.objects.create(gym_id=1, name='test_gym1')
        self.gym2 = m.Gym.objects.create(gym_id=2, name='test_gym2')

    def test_get_all_gyms(self):
        correct_result_1 = [
            self.gym1.gym_id,
            self.gym1.name
        ]

        correct_result_2 = [
            self.gym2.gym_id,
            self.gym2.name
        ]

        result = db.get_all_gyms()

        self.assertIn(correct_result_1, result)
        self.assertIn(correct_result_2, result)

    def test_view_get_all_gyms(self):
        correct_result_1 = [
            self.gym1.gym_id,
            self.gym1.name
        ]

        correct_result_2 = [
            self.gym2.gym_id,
            self.gym2.name
        ]
        response = self.client.post('/simulation/all_gyms/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn(correct_result_1, data['gyms'])
        self.assertIn(correct_result_2, data['gyms'])


class TestGetAllExercises(TestCase):
    def setUp(self):
        self.client = Client()
        self.exercise_no_parameters = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description'
            )

        self.exercise_parameters = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )

        self.parameter = m.Parameter.objects.create(
            parameter_id=1,
            name='parameter',
            units='unit'
        )
        self.parameter_value = m.StandardParameterValue.objects.create(
            standard_parameter_value_id=1,
            value=3,
            parameter=self.parameter,
            exercise=self.exercise_parameters
        )

    def test_get_all_exercises_no_parameter(self):
        result = db.get_all_exercises()

        expected_result = {
            'id': 1,
            'name': 'Exercise 1',
            'parameters': []
        }
        self.assertIn(expected_result, result)

    def test_get_all_exercises_parameter(self):
        result = db.get_all_exercises()

        expected_result = {
            'id': 2,
            'name': 'Exercise 2',
            'parameters': [[1, 'parameter']]
        }
        self.assertIn(expected_result, result)

    def test_view_get_all_exercises(self):
        expected_result1 = {
            'id': 1,
            'name': 'Exercise 1',
            'parameters': []
        }

        expected_result2 = {
            'id': 2,
            'name': 'Exercise 2',
            'parameters': [[1, 'parameter']]
        }
        response = self.client.post('/simulation/all_exercises/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn(expected_result1, data['exercises'])
        self.assertIn(expected_result2, data['exercises'])


class TestGetEquipmentsByGymAndExercise(TestCase):
    def setUp(self):
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')
        self.equipment = m.Equipment.objects.create(equipment_id=1, name='equipment')
        self.gym_equ = m.GymEquipment.objects.create(
            gym_equipment_id=1,
            gym=self.gym,
            equipment=self.equipment
        )

        self.exercise = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description',
            equipment=self.equipment
            )

    def test_get_equipments_by_gym_and_exercise(self):
        result = db.get_equipments_by_gym_and_exercise(self.gym.gym_id, self.exercise.exercise_id)

        expected_result = [
            [1, 'equipment']
        ]
        self.assertEqual(result, expected_result)

    def test_get_equipments_by_gym_and_exercise_no_equipment(self):
        # Use an exercise_id that doesn't exist
        result = db.get_equipments_by_gym_and_exercise(gym_id=1, exercise_id=42)

        self.assertEqual(result, [])

    def test_get_equipments_by_gym_and_exercise_no_gym_equipment(self):
        # gym_id that doesn't exist
        result = db.get_equipments_by_gym_and_exercise(gym_id=42, exercise_id=1)

        self.assertEqual(result, [])

    def test_view_get_equipments_by_gym_and_exercise(self):
        expected_result = [1, 'equipment']
        data = {'gym_id': self.gym.gym_id, 'exercise_id': self.exercise.exercise_id}
        response = self.client.post('/simulation/all_equipments/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn(expected_result, data['equipments'])


class TestInsertExerciseHistory(TestCase):
    def setUp(self):
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')
        self.equipment = m.Equipment.objects.create(equipment_id=1, name='equipment')
        self.gym_equ = m.GymEquipment.objects.create(
            gym_equipment_id=1,
            gym=self.gym,
            equipment=self.equipment
        )

        self.exercise1 = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description',
            equipment=self.equipment
            )

        self.exercise_parameters = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )

        self.parameter = m.Parameter.objects.create(
            parameter_id=1,
            name='parameter',
            units='unit'
        )
        self.parameter_value = m.StandardParameterValue.objects.create(
            standard_parameter_value_id=1,
            value=3,
            parameter=self.parameter,
            exercise=self.exercise_parameters
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

    def test_insert_exercise_history(self):
        exercise_date = '2024-01-01'
        duration = 20
        repetitions_number = 2
        gym_id = self.gym.gym_id
        exercise_id = self.exercise1.exercise_id
        equipment_id = self.gym_equ.gym_equipment_id
        client_id = self.client1.client_id
        calories = 20

        result = db.insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories)

        # check if ExerciseHistory was created
        history = m.ExerciseHistory.objects.all().filter(exercise_history_id=result).first()
        self.assertEqual(history.duration, duration)
        self.assertEqual(history.repetitions_number, repetitions_number)
        self.assertEqual(history.calories, calories)
        self.assertEqual(history.exercise, self.exercise1)
        self.assertEqual(history.client, self.client1)
        self.assertEqual(history.gym, self.gym)
        self.assertEqual(history.gym_equipment, self.gym_equ)

    def test_insert_params_history(self):
        exercise_date = '2024-01-01'
        duration = 20
        repetitions_number = 2
        gym_id = self.gym.gym_id
        exercise_id = self.exercise1.exercise_id
        equipment_id = None
        client_id = self.client1.client_id
        calories = 20

        exercise_history_id = db.insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories)
        params = {'1': 10}

        db.insert_params_history(exercise_history_id, params)

        param_history = m.ExerciseHistoryParamValue.objects.all().filter(exercise_history_id=exercise_history_id).first()
        self.assertEqual(param_history.value, 10)
        self.assertEqual(param_history.parameter, self.parameter)

    def test_view_insert_exercise_history(self):
        exercise_date = '2024-01-01'
        duration = 20
        repetitions_number = 2
        gym_id = self.gym.gym_id
        exercise_id = self.exercise1.exercise_id
        equipment_id = None
        client_id = self.client1.client_id
        calories = 20
        params = {'1': 10}

        data = {'exercise_date': exercise_date,
                'duration': duration,
                'repetitions_number': repetitions_number,
                'gym_id': gym_id,
                'exercise_id': exercise_id,
                'equipment_id': equipment_id,
                'client_id': client_id,
                'calories': calories,
                'params': params,

                }
        response = self.client.post('/simulation/insert_exercise_history/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn("Insert successful", data['message'])

