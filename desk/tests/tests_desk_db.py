# coding: utf-8
"""[summary]Unitary tests for desk app's
models.
Tests:
-test_vote_table_args(self)
-test_candidate_table_args(self)
-test_ticket_table_args(self)
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from common.config import TESTS
from desk.models import Desk, Ticket, Candidate
from desk.models import Desk
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
            school = TESTS['school'],
            school_class = TESTS['name1'],
            opening_vote = TESTS['time1'],
            closing_vote = TESTS['time1'],
            status = TESTS['statusCreate'],
            winners = TESTS['winners'],
            number_voters = TESTS['number1']+1,
            tickets_amount = TESTS['number1']
            )
        self.ticket = Ticket.objects.create(
            ticket_number = TESTS['number1'],
            ticket_code = TESTS['number1']+1,
            desk_tickets = self.desk
            )
        self.candidate = Candidate.objects.create(
            first_name = TESTS['name1'],
            last_name = TESTS['name1'],
            school = TESTS['school'],
            classroom = TESTS['name2']
        )


    def test_desk_table_args(self):
        """[Tests 'Desk_desk' table arguments and its links with
        'Desk_candidate' table.]
        """
        candidate = self.candidate
        desk = self.desk
        desk.candidates.add(candidate)
        desk_candidates = list(desk.candidates.all())
        
        self.assertEqual(desk.school, TESTS['school'])
        self.assertEqual(desk.school_class, TESTS['name1'])
        self.assertEqual(desk.opening_vote, TESTS['time1'])
        self.assertEqual(desk.closing_vote, TESTS['time1'])
        self.assertEqual(desk.status, TESTS['statusCreate'])
        self.assertEqual(desk.winners, TESTS['winners'])
        self.assertEqual(desk.number_voters, TESTS['number1']+1)
        self.assertEqual(desk.tickets_amount, TESTS['number1'])
        self.assertEqual(desk_candidates[0], candidate)

    def test_candidate_table_args(self):
        """[Tests 'Desk_candidate' table arguments.]
        """
        candidate = self.candidate
        desk = self.desk
        
        self.assertEqual(candidate.first_name, TESTS['name1'])
        self.assertEqual(candidate.last_name, TESTS['name1'])
        self.assertEqual(candidate.school, TESTS['school'])
        self.assertEqual(candidate.classroom, TESTS['name2'])

    def test_ticket_table_args(self):
        """[Tests 'Desk_ticket' table arguments and its
        links with 'Desk_desk' table.]
        """
        ticket = self.ticket
        desk = self.desk
        
        self.assertEqual(ticket.ticket_number, TESTS['number1'])
        self.assertEqual(ticket.ticket_code, TESTS['number1']+1)
        self.assertEqual(ticket.desk_tickets, desk)

def test_candidate_display_args(self):
        """Test the way a candidate object is displayed.
        """
        candidate = self.candidate
        self.assertEqual(str(candidate), "candidate: {0}".format(self.first_name))

def test_desk_display_args(self):
        """Test the way a desk object is displayed.
        """
        desk = self.desk
        self.assertEqual(str(desk), "Desk ID: {0}".format(self.id))

def test_ticket_display_args(self):
        """Test the way a ticket object is displayed.
        """
        ticket = self.ticket
        self.assertEqual(str(ticket), "Ticket number: {0}".format(self.ticket_number))
