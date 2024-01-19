from django.test import TestCase, Client
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
import json
from unittest.mock import patch, MagicMock
from freezegun import freeze_time

import database_models.models as m
import trainer.views as v
import trainer.database as db


class CurrentWeekTestCase(TestCase):
    @freeze_time("2024-01-03 12:00:00")
    def test_current_week(self):
        week_dates = db._current_week()

        # Mocked date 03.01.2024
        expected_beginning_of_week = datetime(2024, 1, 1).date()  # Monday of the current week
        expected_end_of_week = datetime(2024, 1, 7).date()  # Sunday of the current week

        self.assertEqual(week_dates, [expected_beginning_of_week, expected_end_of_week])


class AddMinutesTestCase(TestCase):

    def test_add_minutes(self):
        start_time = "12:30"
        minutes_to_add = 45

        result = db._add_minutes(start_time, minutes_to_add)

        expected_result = "13:15"
        self.assertEqual(result, expected_result)

    def test_add_minutes_zero_minutes(self):
        start_time = "08:00"
        minutes_to_add = 0

        result = db._add_minutes(start_time, minutes_to_add)

        # The result should be the same as the start time when adding zero minutes
        self.assertEqual(result, start_time)

    def test_add_minutes_negative_minutes(self):
        start_time = "14:45"
        minutes_to_add = -30

        result = db._add_minutes(start_time, minutes_to_add)

        # The result should be the time before the start time when adding negative minutes
        expected_result = "14:15"
        self.assertEqual(result, expected_result)


class ConvertToDatetimeTestCase(TestCase):

    @freeze_time("2024-01-01 12:00:00")
    def test_convert_to_datetime_future_weekday(self):
        # Test when the desired week day is in the future
        week = "ŚRODA"
        start_time = "14:30"

        result = db._convert_to_datetime(week, start_time)

        expected_datetime = datetime(2024, 1, 3, 14, 30)  # Wednesday at 14:30
        self.assertEqual(result, expected_datetime)

    @freeze_time("2024-01-03 12:00:00")
    def test_convert_to_datetime_past_weekday(self):
        # Test when the desired week day is in the past
        week = "WTOREK"
        start_time = "10:00"

        result = db._convert_to_datetime(week, start_time)

        expected_datetime = datetime(2024, 1, 2, 10, 0)  # Tuesday at 10:00
        self.assertEqual(result, expected_datetime)


class GetClassesForTrainerTestCase(TestCase):

    def setUp(self):
        # Create necessary objects for testing
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='trener',
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
        self.gym_class_group = m.GymClasse.objects.create(
            gym_classe_id=1,
            name='Zajęcia grupowe',
            duration=60,
            price=50,
            )
        self.gym_class_train = m.GymClasse.objects.create(
            gym_classe_id=2,
            name='Trening indywidualny',
            duration=60,
            price=50,
            )

        self.week_schedule_train = m.WeekSchedule.objects.create(
            week_schedule_id=1,
            trainer=self.employee,
            gym_classe=self.gym_class_train,
            week_day='poniedziałek',
            start_time='10:00',
        )

        self.ordered_schedule = m.OrderedSchedule.objects.create(
            ordered_schedule_id=1,
            week_schedule=self.week_schedule_train,
            client_user=self.client1,
            schedule_date=datetime(2024, 1, 1),
        )

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 10, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 11, 0))
    def test_get_classes_for_trainer_individual_ordered(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):

        result = db.get_classes_for_trainer(trainer_id=self.employee.employee_id)

        # Check the result
        expected_result = [{
            'class_id': self.gym_class_train.gym_classe_id,
            'id': self.gym_class_train.gym_classe_id,
            'title': self.gym_class_train.name,
            'class_day': 'poniedziałek',
            'client_id': self.client1.client_id,
            'client_name': self.client1.name,
            'start': '2024-01-01T10:00:00',
            'end': '2024-01-01T10:00:00',
        }]

        self.assertEqual(result, expected_result)

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 10, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 11, 0))
    def test_get_classes_for_trainer_individual_ordered_future_week(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):
        # Change the ordered schedule date to a future week
        self.ordered_schedule.schedule_date = datetime(2024, 1, 15).date()
        self.ordered_schedule.save()

        result = db.get_classes_for_trainer(trainer_id=self.employee.employee_id)

        # Check the result
        expected_result = [{
            'class_id': self.gym_class_train.gym_classe_id,
            'id': self.gym_class_train.gym_classe_id,
            'title': self.gym_class_train.name,
            'class_day': 'poniedziałek',
            'client_id': None,
            'client_name': None,
            'start': '2024-01-01T10:00:00',
            'end': '2024-01-01T10:00:00',
        }]

        self.assertEqual(result, expected_result)

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 10, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 11, 0))
    def test_get_classes_for_trainer_past_week(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):
        # Change the ordered schedule date to a past week
        self.ordered_schedule.schedule_date = datetime(2023, 12, 25).date()
        self.ordered_schedule.save()

        result = db.get_classes_for_trainer(trainer_id=self.employee.employee_id)

        # Check the result
        expected_result = [{
            'class_id': self.gym_class_train.gym_classe_id,
            'id': self.gym_class_train.gym_classe_id,
            'title': self.gym_class_train.name,
            'class_day': 'poniedziałek',
            'client_id': None,
            'client_name': None,
            'start': '2024-01-01T10:00:00',
            'end': '2024-01-01T10:00:00',
        }]

        self.assertEqual(result, expected_result)

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 10, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 11, 0))
    def test_get_classes_for_trainer_individual_not_ordered(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):
        # Remove the ordered schedule
        self.ordered_schedule.delete()

        result = db.get_classes_for_trainer(trainer_id=self.employee.employee_id)

        # Check the result
        expected_result = [{
            'class_id': self.gym_class_train.gym_classe_id,
            'id': self.gym_class_train.gym_classe_id,
            'title': self.gym_class_train.name,
            'class_day': 'poniedziałek',
            'client_id': None,
            'client_name': None,
            'start': '2024-01-01T10:00:00',
            'end': '2024-01-01T10:00:00',
        }]

        self.assertEqual(result, expected_result)

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 12, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 13, 0))
    def test_get_classes_for_trainer_group(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):
        # Remove the ordered schedule
        self.ordered_schedule.delete()
        self.week_schedule_train.delete()
        self.week_schedule_group = m.WeekSchedule.objects.create(
            week_schedule_id=2,
            trainer=self.employee,
            gym_classe=self.gym_class_group,
            week_day='poniedziałek',
            start_time='12:00',
        )

        result = db.get_classes_for_trainer(trainer_id=self.employee.employee_id)

        # Check the result
        expected_result = [{
            'class_id': self.gym_class_group.gym_classe_id,
            'id': self.gym_class_group.gym_classe_id,
            'title': self.gym_class_group.name,
            'class_day': 'poniedziałek',
            'client_id': None,
            'client_name': None,
            'start': '2024-01-01T12:00:00',
            'end': '2024-01-01T12:00:00',
        }]

        self.assertEqual(result, expected_result)

    @patch('trainer.database._current_week', return_value=(datetime(2024, 1, 1), datetime(2024, 1, 7)))
    @patch('trainer.database._convert_to_datetime', return_value=datetime(2024, 1, 1, 12, 0))
    @patch('trainer.database._add_minutes', return_value=datetime(2024, 1, 1, 13, 0))
    def test_view_get_classes_for_trainer(self, mock_current_week, mock_convert_to_datetime, mock_add_minutes):
        self.ordered_schedule.delete()
        self.week_schedule_train.delete()
        self.week_schedule_group = m.WeekSchedule.objects.create(
            week_schedule_id=2,
            trainer=self.employee,
            gym_classe=self.gym_class_group,
            week_day='poniedziałek',
            start_time='12:00',
        )
        expected_result = [{
            'class_id': self.gym_class_group.gym_classe_id,
            'id': self.gym_class_group.gym_classe_id,
            'title': self.gym_class_group.name,
            'class_day': 'poniedziałek',
            'client_id': None,
            'client_name': None,
            'start': '2024-01-01T12:00:00',
            'end': '2024-01-01T12:00:00',
        }]

        data = {'trainer_id': self.employee.employee_id}
        response = self.client.post('/trainer/timetable/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(expected_result, data['classes'])


class DescribeGroupClassTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.gym_class_group = m.GymClasse.objects.create(
            gym_classe_id=1,
            name='Group class',
            duration=60,
            price=50,
            description='test description'
            )

    def test_describe_existing_group_class(self):
        class_id = self.gym_class_group.gym_classe_id
        result = db.describe_group_class(class_id)
        expected_result = ('Group class', 'test description')
        self.assertEqual(result, expected_result)

    def test_view_describe_group_class_existing(self):
        class_id = self.gym_class_group.gym_classe_id
        data = {'class_id': class_id}
        response = self.client.post('/trainer/describe_group_class/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual('Group class', data['name'])
        self.assertEqual('test description', data['description'])

    def test_describe_nonexistent_group_class(self):
        class_id = 999  # Non-existent ID
        result = db.describe_group_class(class_id)
        expected_result = (None, None)
        self.assertEqual(result, expected_result)

    def test_view_describe_nonexistent_group_class(self):
        data = {'class_id': 999}
        response = self.client.post('/trainer/describe_group_class/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Wrong class id", data['error'])

    def test_describe_group_class_with_no_description(self):
        self.gym_class_group.description = ''   # empty description
        self.gym_class_group.save()
        class_id = self.gym_class_group.gym_classe_id
        result = db.describe_group_class(class_id)
        expected_result = ('Group class', '')
        self.assertEqual(result, expected_result)


class DescribeClientTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.training_goal = m.TrainingGoal.objects.create(
            training_goal_id=1,
            name='Weight Loss',
        )

        self.client1 = m.Client.objects.create(
            client_id=1,
            name='John',
            surname='Doe',
            email='john.doe@example.com',
            phone_number='123456789',
            height=180,
            training_frequency=3,
            training_time=30,
            birth_year='1990-01-01',
            gender='Male',
            target_weight=75,
            training_goal=self.training_goal
        )

        # Client's weight history
        m.ClientDataHistory.objects.create(
            client_data_history_id=1,
            client=self.client1,
            weight=80,
            measurement_date='2023-01-01'
        )

    def test_describe_existing_client(self):
        client_id = self.client1.client_id
        result = db.describe_client(client_id)
        expected_result = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '123456789',
            'height': 180,
            'weight': {'weight': 80},
            'training_frequency': 3,
            'training_time': 30,
            'birth_year': '01.01.1990',
            'gender': 'Male',
            'target_goal': 'Weight Loss',
            'target_weight': 75,
        }
        self.assertEqual(result, expected_result)

    def test_view_describe_existing_client(self):
        client_id = self.client1.client_id
        expected_result = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '123456789',
            'height': 180,
            'weight': {'weight': 80},
            'training_frequency': 3,
            'training_time': 30,
            'birth_year': '01.01.1990',
            'gender': 'Male',
            'target_goal': 'Weight Loss',
            'target_weight': 75,
        }
        data = {'client_id': client_id}
        response = self.client.post('/trainer/describe_client/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(expected_result, data['description'])

    def test_describe_nonexistent_client(self):
        client_id = 999  # Non-existent ID
        result = db.describe_client(client_id)
        self.assertIsNone(result)

    def test_view_describe_nonexistent_client(self):
        data = {'client_id': 999}
        response = self.client.post('/trainer/describe_client/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Wrong client id", data['error'])


class GetExercisesForTrainingTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='trener',
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

        self.gym_class_train = m.GymClasse.objects.create(
            gym_classe_id=2,
            name='Trening indywidualny',
            duration=60,
            price=50,
            )

        self.week_schedule_train = m.WeekSchedule.objects.create(
            week_schedule_id=1,
            trainer=self.employee,
            gym_classe=self.gym_class_train,
            week_day='poniedziałek',
            start_time='10:00',
        )

        self.ordered_schedule = m.OrderedSchedule.objects.create(
            ordered_schedule_id=1,
            week_schedule=self.week_schedule_train,
            client_user=self.client1,
            schedule_date=timezone.localtime(timezone.now())+timezone.timedelta(days=1),
        )

        self.exercise_plan = m.ExercisePlan.objects.create(
            exercise_plan_id=1,
            ordered_id=self.ordered_schedule.ordered_schedule_id)

        # Create exercise plan positions
        exercise1 = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description'
            )
        m.ExercisePlanPosition.objects.create(
            exercise_plan_position_id=1,
            exercise_plan=self.exercise_plan,
            exercise=exercise1,
            position=1,
            repetitions_number=10,
            duration=10
        )

        exercise2 = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )
        m.ExercisePlanPosition.objects.create(
            exercise_plan_position_id=2,
            exercise_plan=self.exercise_plan,
            exercise=exercise2,
            position=2,
            duration=60,  # in seconds
            repetitions_number=0
        )

    def test_get_exercises_for_training(self):
        client_id = self.client1.client_id
        employee_id = self.employee.employee_id

        exercises, exercise_plan_id = db.get_exercises_for_training(employee_id, client_id)

        # Expected results
        expected_exercises = [
            {
                'exercise_id': 1,
                'position': 1,
                'name': 'Exercise 1',
                'rep': 10,
                'duration': None,
            },
            {
                'exercise_id': 2,
                'position': 2,
                'name': 'Exercise 2',
                'rep': None,
                'duration': 60,
            },
        ]

        expected_exercise_plan_id = self.exercise_plan.exercise_plan_id

        self.assertEqual(exercises, expected_exercises)
        self.assertEqual(exercise_plan_id, expected_exercise_plan_id)

    def test_view_get_exercises_for_training(self):
        client_id = self.client1.client_id
        employee_id = self.employee.employee_id
        # Expected results
        expected_exercises = [
            {
                'exercise_id': 1,
                'position': 1,
                'name': 'Exercise 1',
                'rep': 10,
                'duration': None,
            },
            {
                'exercise_id': 2,
                'position': 2,
                'name': 'Exercise 2',
                'rep': None,
                'duration': 60,
            },
        ]
        expected_exercise_plan_id = self.exercise_plan.exercise_plan_id

        data = {'trainer_id': employee_id, 'client_id': client_id}
        response = self.client.post('/trainer/incoming_training/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(expected_exercises, data['exercises'])
        self.assertEqual(expected_exercise_plan_id, data['training_id'])

    def test_get_exercises_for_training_no_plan(self):
        # non existing id
        exercises, exercise_plan_id = db.get_exercises_for_training(999, 999)

        expected_exercises = None
        expected_exercise_plan_id = None

        self.assertEqual(exercises, expected_exercises)
        self.assertEqual(exercise_plan_id, expected_exercise_plan_id)

    def test_view_get_exercises_for_training_no_plan(self):
        data = {'trainer_id': 999, 'client_id': 999}
        response = self.client.post('/trainer/incoming_training/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("No plan in database for this training", data['error'])


class AddExerciseTestCase(TestCase):

    def setUp(self):
        # Create sample data for testing
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='trener',
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

        self.gym_class_train = m.GymClasse.objects.create(
            gym_classe_id=2,
            name='Trening indywidualny',
            duration=60,
            price=50,
            )

        self.week_schedule_train = m.WeekSchedule.objects.create(
            week_schedule_id=1,
            trainer=self.employee,
            gym_classe=self.gym_class_train,
            week_day='poniedziałek',
            start_time='10:00',
        )

        self.ordered_schedule = m.OrderedSchedule.objects.create(
            ordered_schedule_id=1,
            week_schedule=self.week_schedule_train,
            client_user=self.client1,
            schedule_date=datetime(2024, 1, 1),
        )

        self.exercise_plan = m.ExercisePlan.objects.create(
            exercise_plan_id=1,
            ordered_id=self.ordered_schedule.ordered_schedule_id)

        # Create exercises
        self.exercise1 = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description'
            )

        self.exercise2 = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )

        self.measured_repetitions = 2
        self.measured_duration = 10  # in seconds


    def test_add_repetition_exercise(self):

        result = db.add_exercise(
            training_id=self.exercise_plan.exercise_plan_id,
            exercise_id=self.exercise1.exercise_id,
            measured=self.measured_repetitions,
            position=None
        )

        expected_result = True

        self.assertEqual(result, expected_result)

        # Check if the ExercisePlanPosition was created
        exercise_plan_position = m.ExercisePlanPosition.objects.filter(exercise_plan=self.exercise_plan).first()
        self.assertIsNotNone(exercise_plan_position)
        self.assertEqual(exercise_plan_position.position, 1)
        self.assertEqual(exercise_plan_position.duration, self.measured_duration)
        self.assertEqual(exercise_plan_position.repetitions_number, self.measured_repetitions)
        self.assertEqual(exercise_plan_position.exercise, self.exercise1)

    def test_add_duration_exercise(self):

        result = db.add_exercise(
            training_id=self.exercise_plan.exercise_plan_id,
            exercise_id=self.exercise2.exercise_id,
            measured=self.measured_duration,
            position=None,
        )

        expected_result = True

        self.assertEqual(result, expected_result)

        # Check if the ExercisePlanPosition was created
        exercise_plan_position = m.ExercisePlanPosition.objects.filter(exercise_plan=self.exercise_plan).first()
        self.assertIsNotNone(exercise_plan_position)
        self.assertEqual(exercise_plan_position.position, 1)
        self.assertEqual(exercise_plan_position.duration, self.measured_duration)
        self.assertEqual(exercise_plan_position.repetitions_number, 0)  # Duration-based exercise
        self.assertEqual(exercise_plan_position.exercise, self.exercise2)

    def test_add_exercise_two(self):
        # first exercise
        result = db.add_exercise(
            training_id=self.exercise_plan.exercise_plan_id,
            exercise_id=self.exercise1.exercise_id,
            measured=self.measured_repetitions,
            position=None
        )

        expected_result = True

        self.assertEqual(result, expected_result)

        # second exercise
        result = db.add_exercise(
            training_id=self.exercise_plan.exercise_plan_id,
            exercise_id=self.exercise1.exercise_id,
            measured=self.measured_repetitions,
            position=None
        )

        expected_result = True

        self.assertEqual(result, expected_result)

        # Check if the ExercisePlanPosition was created
        exercise_plan_position = m.ExercisePlanPosition.objects.filter(exercise_plan=self.exercise_plan)
        self.assertEqual(len(exercise_plan_position), 2)

    def test_add_exercise_not_found(self):
        result = db.add_exercise(
            training_id=self.exercise_plan.exercise_plan_id,
            exercise_id=999,  # Non-existent exercise ID
            measured=self.measured_repetitions,
            position=None,
        )

        expected_result = None

        self.assertEqual(result, expected_result)

    def test_view_add_exercise(self):
        training_id = self.exercise_plan.exercise_plan_id
        exercise_id = self.exercise1.exercise_id
        measured = self.measured_repetitions

        data = {'training_id': training_id, 'exercise_id': exercise_id, 'measured': measured}
        response = self.client.post('/trainer/add_exercise/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual("Exercise added", data['message'])

    def test_view_add_exercise_not_existing(self):
        training_id = self.exercise_plan.exercise_plan_id
        measured = self.measured_repetitions
        data = {'training_id': training_id, 'exercise_id': 999, 'measured': measured}
        response = self.client.post('/trainer/add_exercise/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Error during adding exercise", data['error'])


class TestAllExercises(TestCase):
    def setUp(self):
        self.client = Client()

        # Create exercises
        self.exercise1 = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description'
            )

        self.exercise2 = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )

    def test_all_exercises(self):
        result = db.all_exercises()

        expected_result = [
            {'exercise_id': 1, 'name': 'Exercise 1', 'rep': 2, 'duration': None},
            {'exercise_id': 2, 'name': 'Exercise 2', 'rep': None, 'duration': 10}
        ]
        self.assertEqual(result, expected_result)

    def test_view_all_exercises(self):
        expected_result = [
            {'exercise_id': 1, 'name': 'Exercise 1', 'rep': 2, 'duration': None},
            {'exercise_id': 2, 'name': 'Exercise 2', 'rep': None, 'duration': 10}
        ]

        response = self.client.post('/trainer/all_exercises/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(expected_result, data['exercises'])


class TestSaveExercises(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.client = Client()

        self.gym = m.Gym.objects.create(gym_id=1, name='test_gym')

        self.employee = m.Employee.objects.create(
            login='test_employee',
            password_hash=make_password('test_password'),
            name='test_name',
            type='trener',
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

        self.gym_class_train = m.GymClasse.objects.create(
            gym_classe_id=2,
            name='Trening indywidualny',
            duration=60,
            price=50,
            )

        self.week_schedule_train = m.WeekSchedule.objects.create(
            week_schedule_id=1,
            trainer=self.employee,
            gym_classe=self.gym_class_train,
            week_day='poniedziałek',
            start_time='10:00',
        )

        self.ordered_schedule = m.OrderedSchedule.objects.create(
            ordered_schedule_id=1,
            week_schedule=self.week_schedule_train,
            client_user=self.client1,
            schedule_date=datetime(2024, 1, 1),
        )

        self.exercise_plan = m.ExercisePlan.objects.create(
            exercise_plan_id=1,
            ordered_id=self.ordered_schedule.ordered_schedule_id)

        # Create exercises
        self.exercise1 = m.Exercise.objects.create(
            exercise_id=1,
            name='Exercise 1',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=2,
            description='description'
            )

        self.exercise2 = m.Exercise.objects.create(
            exercise_id=2,
            name='Exercise 2',
            type='test type',
            calories=10,
            duration=10,
            advancement_level='level',
            repetitions_number=0,
            description='description'
            )

    def test_save_exercises(self):
        data = [
            {
                'exercise_id': 1,
                'rep': 5,
                'duration': None,
                'position': 1
            },
            {
                'exercise_id': 2,
                'rep': None,
                'duration': 30,
                'position': 2
            }
        ]
        exercise_plan_id = self.exercise_plan.exercise_plan_id

        result = db.save_exercises(data, exercise_plan_id)

        self.assertTrue(result)

        # Check if the ExercisePlanPosition was created
        exercise_plan_position = m.ExercisePlanPosition.objects.filter(exercise_plan=self.exercise_plan)
        self.assertIsNotNone(exercise_plan_position)
        self.assertEqual(exercise_plan_position[0].position, 1)
        self.assertEqual(exercise_plan_position[0].repetitions_number, 5)
        self.assertEqual(exercise_plan_position[0].exercise, self.exercise1)

        self.assertEqual(exercise_plan_position[1].position, 2)
        self.assertEqual(exercise_plan_position[1].duration, 30)
        self.assertEqual(exercise_plan_position[1].exercise, self.exercise2)

    def test_view_save_exercises(self):
        exercise_plan_id = self.exercise_plan.exercise_plan_id
        exercises = [
            {
                'exercise_id': 1,
                'rep': 5,
                'duration': None,
                'position': 1
            },
            {
                'exercise_id': 2,
                'rep': None,
                'duration': 30,
                'position': 2
            }
        ]

        data = {'training_id': exercise_plan_id, 'exercise': exercises}
        response = self.client.post('/trainer/save_exercises/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual("Exercises saved", data['message'])

    def test_save_exercise_error(self):
        data = [
            {
                'exercise_id': 3,
                'rep': 5,
                'duration': None,
                'position': 1
            },
        ]
        exercise_plan_id = self.exercise_plan.exercise_plan_id

        result = db.save_exercises(data, exercise_plan_id)

        self.assertIsNone(result)

    def test_view_save_exercise_error(self):
        exercise_plan_id = self.exercise_plan.exercise_plan_id
        exercises = [
            {
                'exercise_id': 3,
                'rep': 5,
                'duration': None,
                'position': 1
            },
        ]
        data = {'training_id': exercise_plan_id, 'exercise': exercises}
        response = self.client.post('/trainer/save_exercises/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn("Error during saving exercises", data['error'])

