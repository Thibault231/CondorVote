# coding: utf-8
"""[summary]Unitary tests for vote app's
functions.
"""
from django.test import RequestFactory, TestCase
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
            school=TESTS['school'],
            school_class=TESTS['name2'],
            opening_vote=TESTS['time1'],
            closing_vote=TESTS['time1'],
            status=TESTS['statusCreate'],
            winners=TESTS['winners'],
            number_voters=TESTS['number1'],
            tickets_amount=TESTS['number1']
            )
        self.vote = Vote.objects.create(
            ballot=TESTS['ballot'],
            desk_votes=self.desk
            )

    def test_vote_table_args(self):
        """[Tests 'Vote_vote' table arguments and its
        links with 'Desk_desk' table.]
        """
        vote = self.vote
        desk = self.desk

        self.assertEqual(vote.ballot, TESTS['ballot'])
        self.assertEqual(vote.desk_votes, desk)

    def test_vote_display_args(self):
        """Test the way a vote object is displayed.
        """
        vote = self.vote
        self.assertEqual(str(vote), "Vote ID: {0}".format(vote.id))
