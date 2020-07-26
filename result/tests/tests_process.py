# coding: utf-8
"""[summary]Unitary tests for result.result_process file
functions.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import numpy as np
from vote.models import Vote
from desk.models import Desk
from common.config import TESTS2, TESTS
from result.result_process import candidates_duals
# from common.config import TESTS


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
        x1 = "[a, 1, a, 2, a, 3, a, 4, a, 5, a, 6]"
        x2 = "[a, 2, a, 4, a, 3, a, 3, a, 1, a, 6]"
        x3 = "[a, 6, a, 6, a, 6, a, 1, a, 2, a, 3]"
        x4 = "[a, 2, a, 1, a, 3, a, 3, a, 4, a, 5]"
        x5 = "[a, 1, a,1, a, 3, a, 3, a, 4, a, 5]"

        self.vote1 = Vote.objects.create(
            ballot=x1, 
            desk_votes=self.desk,
            ) 
        
        self.vote2 = Vote.objects.create(
            ballot=x2, 
            desk_votes=self.desk,
            )
        self.vote3 = Vote.objects.create(
            ballot=x3, 
            desk_votes=self.desk,
            )
        self.vote4 = Vote.objects.create(
            ballot=x4, 
            desk_votes=self.desk,
            )
        self.vote5 = Vote.objects.create(
            ballot=x5, 
            desk_votes=self.desk,
            )
        self.vote_list = [self.vote1, self.vote2, self.vote3, self.vote4, self.vote5]
        self.n_candidates = 6 
    
    def test_matrixs_args(self):
        """[Tests that the central algorythme
        of condorvote application caculate the 
        correct winner of Condorcet election.]
        """
        vote_list = self.vote_list
        n_candidates = self.n_candidates
        vote_matrix, victories_matrix, winner_list = candidates_duals(
            vote_list, n_candidates)
        
        np.testing.assert_array_equal(vote_matrix, TESTS2['vote_matrix'])
        np.testing.assert_array_equal(victories_matrix, TESTS2['victories_matrix'])
        np.testing.assert_array_equal(winner_list, TESTS2['winner_matrix'])
