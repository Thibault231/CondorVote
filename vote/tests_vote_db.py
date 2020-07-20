# coding: utf-8
"""[summary]Unitary tests for vote app's
functions.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from common.config import TESTS
from vote.models import Vote
from desk.models import Desk
# from common.config import TESTS


class AccountTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -test_desk_table_args(self)

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
            number_voters = TESTS['number1'],
            tickets_amount = TESTS['number1']
            )
        self.vote = Vote.objects.create(
            ballot = TESTS['ballot'],
            desk_votes = self.desk
            )


    def test_desk_table_args(self):
        """[Tests 'Vote_vote' table arguments and its
        links with 'Desk_desk' table.]
        """
        vote = self.vote
        desk = self.desk
        
        self.assertEqual(vote.ballot, TESTS['ballot'])
        self.assertEqual(vote.desk_votes, desk)
