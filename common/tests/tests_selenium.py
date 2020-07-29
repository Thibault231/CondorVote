# coding: utf-8
"""Fonctionals tests on localhost for
condorvote_project.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase, RequestFactory
from django.contrib.auth.models import User
from account.models import Account
from desk.models import Desk, Ticket, Candidate
from vote.models import Vote
from common.config import TESTS4, TESTS


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

    def test_create_user_desk_vote(self):
        driver = self.driver

        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS4['UrlApp'])

        # create account
        wait.until(EC.element_to_be_clickable((By.ID, "create_account")))
        first_url = driver.current_url
        driver.find_element(By.ID, 'create_account').click()
        
        wait.until(EC.element_to_be_clickable((By.ID, "formular_account")))
        second_url = driver.current_url
        driver.find_element(
            By.ID, 'id_username').send_keys(TESTS['name2'] )
        driver.find_element(
            By.ID, 'id_first_name').send_keys(TESTS['name2'])
        driver.find_element(
            By.ID, 'id_last_name').send_keys(TESTS['name2'])
        driver.find_element(
            By.ID, 'id_email').send_keys(TESTS['name2']+'@gmail.com' )
        driver.find_element(
            By.ID, 'id_school').send_keys(TESTS['name2'])    
        driver.find_element(
            By.ID, 'id_departement').send_keys(TESTS['number1'])   
        driver.find_element(
            By.ID, 'id_password1').send_keys(TESTS['name2'])
        driver.find_element(
            By.ID, 'id_password2').send_keys(TESTS['name2'] + Keys.RETURN)

        # create desk
        wait.until(EC.element_to_be_clickable((By.ID, 'create_desk')))
        third_url = driver.current_url
        driver.find_element(By.ID, 'create_desk').click()

        wait.until(EC.element_to_be_clickable((By.ID, "formular_desk")))
        forth_url = driver.current_url
        driver.find_element(
            By.ID, 'id_school').send_keys(TESTS['name2'])
        driver.find_element(
            By.ID, 'id_school_class').send_keys(TESTS['name2'])
        driver.find_element(By.ID, 'id_opening_vote_1').click()
        driver.find_element(
            By.ID, 'id_tickets_amount').send_keys('1' + Keys.RETURN)
        
        wait.until(EC.element_to_be_clickable((By.ID, "end_add_candidate")))
        fifth_url = driver.current_url 
        driver.find_element(By.ID, 'end_add_candidate').click()

        wait.until(EC.presence_of_element_located((By.ID, "ticket_code")))
        sixth_url = driver.current_url
        ticket = driver.find_element(By.ID, 'ticket_code').get_attribute('value')

        #vote
        wait.until(EC.element_to_be_clickable((By.ID, "vote")))
        seventh_url = driver.current_url
        driver.find_element(By.ID, 'vote').click()

        wait.until(EC.element_to_be_clickable((By.ID, "validate_ticket")))
        eighth_url = driver.current_url
        driver.find_element(
            By.ID, 'id_ticket').send_keys( ticket + Keys.RETURN)
        
        wait.until(EC.element_to_be_clickable((By.ID, "validate_ballot")))
        nineth_url = driver.current_url
        driver.find_element(By.ID, "validate_ballot").click()

        wait.until(EC.element_to_be_clickable((By.ID, "end_vote")))
        tenth_url = driver.current_url

        self.assertEqual(TESTS4['UrlApp'], first_url)
        self.assertEqual(TESTS4['UrlCreateAccount'], second_url)
        self.assertEqual(TESTS4['UrlCreateAccount'], third_url)
        self.assertEqual(TESTS4['UrlCreateDesk'], forth_url)
        self.assertTrue(fifth_url.__contains__(TESTS4['UrlCandidates']))
        self.assertTrue(sixth_url.__contains__(TESTS4['UrlTickets']))
        self.assertTrue(nineth_url.__contains__(TESTS4['UrlVote']))
        self.assertTrue(tenth_url.__contains__(TESTS4['UrlVote']))


    def test_user_connect_delete(self):
        driver = self.driver

        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS4['UrlApp'])

        wait.until(EC.element_to_be_clickable((By.ID, "djHideToolBarButton")))
        driver.find_element(By.ID, "djHideToolBarButton").click()
        
        wait.until(EC.element_to_be_clickable((By.ID, "connection")))
        first_url = driver.current_url
        driver.find_element(By.ID, 'connection').click()

        wait.until(EC.element_to_be_clickable((By.ID, "formular_connection")))
        second_url = driver.current_url
        driver.find_element(
            By.ID, 'id_email').send_keys(TESTS['name2']+'@gmail.com' ) 
        driver.find_element(
            By.ID, 'id_password').send_keys(TESTS['name2'] + Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.ID, "authenticate")))
        third_url = driver.current_url
        wait.until(EC.element_to_be_clickable((By.ID, "my_account2")))
        driver.find_element(By.ID, 'my_account2').click()

        wait.until(EC.element_to_be_clickable((By.ID, "delete_account")))
        forth_url = driver.current_url
        driver.find_element(By.ID, 'delete_account').click()

        wait.until(EC.element_to_be_clickable((By.ID, "delete_confirm")))
        fifth_url = driver.current_url
        driver.find_element(By.ID, 'delete_confirm').click()

        wait.until(EC.element_to_be_clickable((By.ID, "create_account")))
        sixth_url = driver.current_url

        self.assertEqual(TESTS4['UrlApp'], first_url)
        self.assertEqual(TESTS4['UrlConnection'], second_url)
        self.assertEqual(TESTS4['UrlConnection'], third_url)
        self.assertEqual(TESTS4['UrlMyAccount'], forth_url)
        self.assertEqual(TESTS4['UrlDeleteConfirm'], fifth_url)
        self.assertEqual(TESTS4['UrlDeleteUser'], sixth_url)
