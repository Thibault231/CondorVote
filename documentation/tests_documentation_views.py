# coding: utf-8
"""Unitary tests for documentation.views.py functions which don't need
user's loging.
"""
from django.test import TestCase
from django.urls import reverse
from common.config import TESTS


class ViewsTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -test_voter_infos_page(self)
    -test_organizer_infos_page(self)
    -test_condorcet_infos_page(self)
    """

    def test_voter_infos_page(self):
        """Test right view for documentation:voter_infos.
        """
        response = self.client.get(reverse('documentation:voter_infos'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
    
    def test_organizer_infos_page(self):
        """Test right view for documentation:organizer_infos.
        """
        response = self.client.get(reverse('documentation:organizer_infos'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_condorcet_infos_page(self):
        """Test right view for documentation:condorcet_infos.
        """
        response = self.client.get(reverse('documentation:condorcet_infos'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
