# coding: utf-8
"""[summary]Unitary tests for account app's
functions.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from common.config import TESTS
from account.models import Account
from desk.models import Desk
# from common.config import TESTS


class AccountTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -test_user_table_args(self)
    -test_account_table_args(self)

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


    def test_user_table_args(self):
        """[Tests the user's account creation with
        module django.author.]
        """
        user = self.user
        self.assertEqual(user.username, TESTS['name1'])
        self.assertEqual(user.first_name, TESTS['name1'])
        self.assertEqual(user.last_name, TESTS['name1'])
        self.assertEqual(user.email, TESTS['name1']+'@gmail.com')

    def test_account_table_args(self):
        """[Tests the links between user account and 
        'Account_account' table.]
        """
        user = self.user
        account = self.account
        desk = self.desk
        account.desk_link.add(desk)
        desk_list = list(account.desk_link.all())
        
        self.assertEqual(account.user, user)
        self.assertEqual(account.school, TESTS['school'])
        self.assertEqual(account.departement, TESTS['departement'])
        self.assertEqual(desk_list[0], desk)

def test_account_display_args(self):
        """Test the way an account object is displayed.
        """
        account = self.account
        self.assertEqual(str(account), "Account of: {0}".format(self.user.username))