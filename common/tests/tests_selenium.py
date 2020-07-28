# coding: utf-8
"""Fonctionals tests on localhost for
condorvote_project.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from ..config import TESTS


class TestUserTakesTheTest(LiveServerTestCase):
    """Class LiveServerTestCase for tests functions.
    Functions:
    -setUp(self)
    -tearDown(self)
    -test_user_voting(self)
    -test_user_creating_account(self)
    -test_user_modifying_account(self)
    -test_user_creating_desk(self)
    -test_user_modifying_desk(self)

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.driver = webdriver.Firefox()

    def tearDown(self):
        """delete self objects after the running tests
        """
        self.driver.quit()

    def test_user_voting(self):
        driver = self.driver
        b = 1
        D = b
        self.assertEqual(D, 1)

    def test_user_creating_account(self):
        pass

    def test_user_modifying_account(self):
        pass

    def test_user_creating_desk(self):
        pass

    def test_user_modifying_desk(self):
        pass
