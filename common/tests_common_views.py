# coding: utf-8
"""Unitary tests for common.views.py functions which don't need
user's loging.
"""
from django.test import TestCase
from django.urls import reverse
from common.config import TESTS


class ViewsTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -test_index_page(self)
    -test_legal_page(self)
    """

    def test_index_page(self):
        """Test right view for *:index.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_legal_page(self):
        """Test right view for common:legal_mentions.
        """
        response = self.client.get(reverse('common:legal_mentions'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
    
    def test_error400_page(self):
        """Test access to template 400.html.
        """
        response = self.client.get(reverse('common:error400'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
    
    def test_error404_page(self):
        """Test access to template 404.html.
        """
        response = self.client.get(reverse('common:error404'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_error500_page(self):
        """Test access to template 500.html.
        """
        response = self.client.get(reverse('common:error500'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])