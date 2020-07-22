# coding: utf-8
"""[summary]Unitary tests for views.py of account app's
functions which need user's loging.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from account.models import Account
from desk.models import Desk
from common.config import TESTS


class AccountTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -test_right_connexion_log_page(self)
    -test_wrong_connexion_log_page(self)
    -test_connexion_page(self)
    -test_deconnexion_log_page(self)
    -test_deconnexion_unlog_page(self)
    -test_myaccount_log_page(self)
    -test_myaccount_unlog_page(self)
    -test_account_creation_account_page(self)
    -test_right_account_creation_page(self)
    -test_right_delete_confirmation_page(self)
    -test_wrong_delete_confirmation_page(self)
    -test_wrong_delete_user_page(self)
    -test_right_delete_user_page(self)
    -test_modify_account_unlog_page(self)
    -test_right_account_modification_page(self)
    -test_partial_account_modification_page(self)

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
        self.user = User.objects.create_user(
            username=TESTS['name1'],
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'],
            first_name=TESTS['name1'],
            last_name=TESTS['name1']
            )
        self.account = Account.objects.create(
            user=self.user,
            school = TESTS['school'],
            departement = TESTS['departement'],
            )

    def test_right_connexion_log_page(self):
        """Test login method with right args.
        """
        response = self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        self.assertIs(response, True)

    def test_wrong_connexion_log_page(self):
        """Test login method with wrong args.
        """
        response = self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name2'])
        self.assertIsNot(response, True)

    def test_connexion_page(self):
        """Test account to the page Connexion with
        GET method and right args.
        """
        response = self.client.get(reverse('account:connexion'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_deconnexion_log_page(self):
        """Test deaccount of a loged user with the view deconnexion
        with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:deconnexion'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_deconnexion_unlog_page(self):
        """Test deaccount of an unloged user with the view deconnexion
        with GET method and right args.
        """
        response = self.client.get('account:deconnexion')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_myaccount_log_page(self):
        """Test account to the page Myaccount of a connected user
        with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:myaccount'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_myaccount_unlog_page(self):
        """Test account to the page Myaccount of an anonymous
        user with GET method and right args.
        """
        response = self.client.get('account:deconnexion')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_account_creation_account_page(self):
        """Test account creation on the page Account_creation of an
        anonymous user with GET method and right args.
        """
        response = self.client.get(reverse('account:account_creation'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_right_account_creation_page(self):
        """Test account creation on the page Account_creation of an
        anonymous user with GET method and wrong args.
        """
        response = self.client.post(reverse('account:account_creation'), {
            'username': TESTS['name2'],
            'email': TESTS['name2']+'@gmail.com',
            'password1': TESTS['name2'],
            'password2': TESTS['name2']})
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_right_delete_confirmation_page(self):
        """Test account deletion on the page Delete_confirmation of a loged
        user with GET method and wrong args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:delete_confirmation'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_wrong_delete_confirmation_page(self):
        """Test account deletion on the page Delete_confirmation of an
        anonymous user with GET method and wrong args.
        """
        response = self.client.get('account:delete_confirmation')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_wrong_delete_user_page(self):
        """Test account deletion on the page Delete_done of an
        anonymous user with GET method and wrong args.
        """
        response = self.client.get('account:delete_user')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_right_delete_user_page(self):
        """Test account deletion on the page Delete_done of a loged
        user with GET method and wrong args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:delete_user'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_modify_account_log_page(self):
        """Test account creation on the page Account_creation of an
        anonymous user with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:modify_account'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_modify_account_unlog_page(self):
        """Test account creation on the page modify_account of an
        anonymous user.
        """
        response = self.client.get('account:modify_account')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_right_account_modification_page(self):
        """Test account creation on the page modify_account of an
        connected user with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(reverse('account:modify_account'), {
            'username': TESTS['name2'],
            'first_name': TESTS['name2'],
            'last_name': TESTS['name2'],
            'school': TESTS['name1'],
            'departement': TESTS['departement']+1,
        })
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_partial_account_modification_page(self):
        """Test account creation on the page modify_account of an
        connected user with GET method and uncompleted args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(reverse('account:modify_account'), {
            'first_name': TESTS['name2'],
            'last_name': TESTS['name2'],
            'school': TESTS['name1'],
            'departement': TESTS['departement']+1,
        })
        self.assertEqual(response.status_code, TESTS['RightStatus'])
