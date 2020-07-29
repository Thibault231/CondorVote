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

    def test_get_adding_cand(self):
        """Test access on API add_cand with GET
        method.
        """
        response = self.client.get(
            reverse('command:adding_cand'))
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(message['message'], 'Methode not allowed')

    def test_post_wrong_formular_adding_cand(self):
        """Test access on API add_cand with POST
        method and no formular.
        """
        response = self.client.post(
            reverse('command:adding_cand'))
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(message['message'], 'Invalid formular')

    def test_post_right_adding_cand(self):
        """Test access on API add_cand with POST
        method.
        """
        desk = self.desk
        response = self.client.post(
            reverse('command:adding_cand'),
            {
                'first_name': TESTS['name2'],
                'last_name': TESTS['name2'],
                'desk_id': desk.id,
            })
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertTrue(
            message['message'].__contains__('a bien été ajouté'))
        self.assertEqual(message['number_candidate'], 1)

    def test_post_wrong_desk_adding_cand(self):
        """Test access on API add_cand with POST
        method and wrong desk.
        """
        desk = self.desk
        response = self.client.post(
            reverse('command:adding_cand'),
            {
                'first_name': TESTS['name2'],
                'last_name': TESTS['name2'],
                'desk_id': desk.id+1,
            })
        message = json.loads(response.content)
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(
            message['message'],
            "Erreur: Aucun bureau\
                        de vote de ce nom n'a été trouvé")

    def test_post_wrong_cand_adding_cand(self):
        """Test access on API add_cand with POST
        method and wrong desk.
        """
        desk = self.desk
        response = self.client.post(
            reverse('command:adding_cand'),
            {
                'first_name': TESTS['name1'],
                'last_name': TESTS['name1'],
                'desk_id': desk.id,
            })
        message = json.loads(response.content)
        self.assertEqual(
            response.status_code,
            TESTS['RightStatus']
        )
        self.assertTrue(message['message'].__contains__("a déjà été ajouté"))
