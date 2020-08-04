# coding: utf-8
"""Unitary tests for desk APP's
functions of views.py.
Tests:
-test_vote_table_args(self)
"""
import json
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from account.models import Account
from desk.models import Desk, Ticket, Candidate
from common.config import TESTS


class AccountTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -test_desk_table_args(self)
    -test_candidate_table_args(self)
    -test_ticket_table_args(self)

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.factory = RequestFactory()
        self.desk = Desk.objects.create(
            school=TESTS['school'],
            school_class=TESTS['name1'],
            opening_vote=TESTS['time1'],
            closing_vote=TESTS['time1'],
            status=TESTS['statusCreate'],
            winners=TESTS['winners'],
            number_voters=TESTS['number1']+1,
            tickets_amount=TESTS['number1']
            )
        self.ticket = Ticket.objects.create(
            ticket_number=TESTS['number1'],
            ticket_code=TESTS['number1']+1,
            desk_tickets=self.desk
            )
        self.candidate = Candidate.objects.create(
            first_name=TESTS['name1'],
            last_name=TESTS['name1'],
            school=TESTS['school'],
            classroom=TESTS['name1']
        )
        self.user = User.objects.create_user(
            username=TESTS['name1'],
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'],
            first_name=TESTS['name1'],
            last_name=TESTS['name1']
            )
        self.account = Account.objects.create(
            user=self.user,
            school=TESTS['school'],
            departement=TESTS['departement'],
            )

    def test_get_adding_users(self):
        """Test access on API adding_tickets with GET
        method.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('command:adding_tickets'))
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(message['message'], 'Methode not allowed')

    def test_get_deleting_users(self):
        """Test access on API deleting_tickets  with GET
        method.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('command:deleting_tickets'))
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(message['message'], 'Methode not allowed')
    
    def test_post_right_adding_tickets(self):
        """Test access on API adding_tickets with POST
        method and no formular.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:adding_tickets'),
            {
                'new_amount': TESTS['number1'],
                'desk_id': desk.id,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
                'Les tickets ont bien été ajoutés.\nVous disposez de'))

    def test_post_right_deleting_tickets(self):
        """Test access on API deleting_tickets with POST
        method and no formular.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:deleting_tickets'),
            {
                'new_amount': 1,
                'desk_id': desk.id,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
            'Les tickets ont bien été supprimés.\n'))

    def test_post_wrong_desk_adding_tickets(self):
        """Test access on API adding_tickets with POST
        method and no formular.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:adding_tickets'),
            {
                'new_amount': TESTS['number1'],
                'desk_id': desk.id,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
                'Les tickets ont bien été ajoutés.\nVous disposez de'))

    def test_post_wrong_desk_adding_tickets(self):
        """Test access on API adding_tickets with POST
        method and no formular.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:deleting_tickets'),
            {
                'new_amount': TESTS['number1'],
                'desk_id': desk.id+1,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
                "Erreur: Aucun bureau"))

    def test_post_wrong_desk_deleting_tickets(self):
        """Test access on API deleting_tickets with POST
        method and no formular.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:deleting_tickets'),
            {
                'new_amount': '1',
                'desk_id': desk.id+1,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
                "Erreur: Aucun bureau"))

    def test_post_wrong_tomuch_deleting_tickets(self):
        """Test access on API deleting_tickets with POST
        method and to much tickets to delete.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(
            reverse('command:deleting_tickets'),
            {
                'new_amount': TESTS['number1']+3,
                'desk_id': desk.id,
            }
            )
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__(
            "La quantité à supprimer dépasse la quantité disponible."))