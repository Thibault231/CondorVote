# coding: utf-8
"""[summary]Unitary tests for result.result_process file
functions.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
import numpy as np
from common.config import TESTS2
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
        x1 = [1, 2, 3, 4, 5, 6]
        x2 = [2, 4, 3, 3, 1, 6]
        x3 = [6, 6, 6, 1, 2, 3]
        x4 = [2, 1, 3, 3, 4, 5]
        x5 = [1, 1, 3, 3, 4, 5]
        self.vote_list = [x1, x2, x3, x4, x5]
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
