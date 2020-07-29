# coding: utf-8
"""[summary]Unitary tests for result.views file
functions.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from desk.models import Desk, Ticket, Candidate
from vote.models import Vote
from account.models import Account
from common.config import TESTS


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
            school=TESTS['school'],
            school_class=TESTS['name1'],
            opening_vote=TESTS['time1'],
            closing_vote=TESTS['time1'],
            status=TESTS['statusCreate'],
            winners=TESTS['winners'],
            number_voters=TESTS['number1']+1,
            tickets_amount=TESTS['number1']
            )
        self.ticket = Ticket.objects.create(
            ticket_number=TESTS['number1'],
            ticket_code=TESTS['number1']+1,
            desk_tickets=self.desk
            )
        self.candidate = Candidate.objects.create(
            first_name=TESTS['name1'],
            last_name=TESTS['name1'],
            school=TESTS['school'],
            classroom=TESTS['name2']
        )
        self.candidate.save()
        self.user = User.objects.create_user(
            username=TESTS['name1'],
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'],
            first_name=TESTS['name1'],
            last_name=TESTS['name1']
            )
        self.account = Account.objects.create(
            user=self.user,
            school=TESTS['school'],
            departement=TESTS['departement'],
            )
        self.vote = Vote.objects.create(
            ballot="['{cand}', '1'], ['{cand}', '1']".format(
                cand=self.candidate.id),
            desk_votes=self.desk,
            )

    def test_access_unlog_result_page(self):
        """Test access on the page result of a
        connected user with GET method and right args
        """
        desk = self.desk
        response = self.client.get(reverse('result:result',  args=(desk.id, )))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_result_page(self):
        """Test access on the page result of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        candidate = self.candidate
        desk.candidates.add(candidate)
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('result:result', args=(desk.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertIsInstance(response.context['message'], int)
        self.assertIsInstance(response.context['winners_list'], list)

    def test_access_unlog_result_details_page(self):
        """Test access on the page result_details of a
        connected user with GET method and right args
        """
        desk = self.desk
        response = self.client.get(
            reverse(
                'result:result_details',
                args=(desk.id, )
            )
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_result_details_page(self):
        """Test access on the page result_details of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        candidate = self.candidate
        desk.candidates.add(candidate)
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse(
                'result:result_details',
                args=(desk.id, )
            )
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])
