from django.test import TestCase, Client
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
import json
from unittest.mock import patch, MagicMock
from freezegun import freeze_time

import database_models.models as m
import manager.database as db


class TestTicketPopularity(TestCase):
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

        ticket1 = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=1,
            name='Standard Ticket',
            duration=30,
            price=50,
            type='Standard')
        ticket2 = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=2,
            name='Premium Ticket',
            duration=60,
            price=100,
            type='Premium')

        # Create GymTicketHistory entries for the last month
        current_date = datetime.now().date()
        last_day = current_date - timedelta(days=current_date.day)
        self.purchase_date_1 = last_day - timedelta(days=5)
        self.purchase_date_2 = last_day - timedelta(days=10)

        m.GymTicketHistory.objects.create(
            gym_ticket_history_id=1,
            purchase_date=self.purchase_date_1,
            gym_ticket_offer=ticket1,
            client=self.client1)
        m.GymTicketHistory.objects.create(
            gym_ticket_history_id=2,
            purchase_date=self.purchase_date_2,
            gym_ticket_offer=ticket2,
            client=self.client1)

    def test_count_ticket_popularity(self):
        count, ticket_types = db.count_ticket_popularity()

        expected_count = [1, 1]
        expected_types = ['Standard (30)', 'Premium (60)']
        self.assertEqual(count, expected_count)
        self.assertEqual(ticket_types, expected_types)

    def test_ticket_popularity(self):
        result = db.ticket_popularity_month()
        self.assertIsNotNone(result)

    def test_view_ticket_popularity(self):
        response = self.client.post('/manager/ticket_popularity_week/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNotNone(data['plot'])


class TestDiscountPopularity(TestCase):
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

        ticket1 = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=1,
            name='Standard Ticket',
            duration=30,
            price=50,
            type='Standard')
        ticket2 = m.GymTicketOffer.objects.create(
            gym_ticket_offer_id=2,
            name='Premium Ticket',
            duration=60,
            price=100,
            type='Premium')

        # Create GymTicketHistory entries for the last month
        current_date = datetime.now().date()
        last_day = current_date - timedelta(days=current_date.day)
        first_day = last_day - timedelta(days=31)
        self.purchase_date_1 = last_day - timedelta(days=5)
        self.purchase_date_2 = last_day - timedelta(days=10)

        discount1 = m.Discount.objects.create(
            discount_id=1,
            name='Discount 1',
            start_date=first_day,
            discount_percentages=10,
            gym_ticket_offer=ticket1)

        discount2 = m.Discount.objects.create(
            discount_id=2,
            name='Discount 2',
            start_date=first_day,
            discount_percentages=10,
            gym_ticket_offer=ticket2)

        m.GymTicketHistory.objects.create(
            gym_ticket_history_id=1,
            purchase_date=self.purchase_date_1,
            gym_ticket_offer=ticket1,
            client=self.client1,
            discount=discount1)

        m.GymTicketHistory.objects.create(
            gym_ticket_history_id=2,
            purchase_date=self.purchase_date_2,
            gym_ticket_offer=ticket2,
            client=self.client1,
            discount=discount2)

    def test_count_discount_popularity(self):
        result, discount_types = db.count_discount_popularity()

        expected_result = [1, 1]
        self.assertEqual(result, expected_result)

        expected_discount_types = ['Discount 1', 'Discount 2']
        self.assertEqual(discount_types, expected_discount_types)

    def test_discount_popularity(self):
        result = db.discount_popularity_month()
        self.assertIsNotNone(result)

    def test_view_discount_popularity(self):
        response = self.client.post('/manager/discount_popularity_week/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNotNone(data['plot'])
