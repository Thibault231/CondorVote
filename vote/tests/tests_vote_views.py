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
from common.config import TESTS, TESTS2


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
        self.ticket = Ticket.objects.create(
            ticket_number = TESTS['number1'],
            ticket_code = TESTS['number1']+1,
            desk_tickets = self.desk
            )
        self.candidate = Candidate.objects.create(
            first_name = TESTS['name1'],
            last_name = TESTS['name1'],
            school = TESTS['school'],
            classroom = TESTS['name2']
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
        self.vote = Vote.objects.create(
            ballot="0", 
            desk_votes=self.desk,
            )
        
    def test_accessGET_log_enter_ticket_page(self):
        """Test access on the page enter_tickets of an
        anonymous user with GET method and right args.
        """
        response = self.client.get(reverse('vote:enter_ticket'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
 
    def test_rightPOST_log_enter_ticket_page(self):
        """Test access on the page enter_tickets of an
        anonymous user with POST method and right args.
        Enter a right ticket number.
        """
        response = self.client.post(reverse('vote:enter_ticket'), {'ticket': TESTS['number1']+1})
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(response.context['message'], "Votre ticket est validé. Vous pouvez voter.")
    
    def test_wrongPOST_log_enter_ticket_page(self):
        """Test access on the page enter_tickets of an
        anonymous user with POST method and right args.
        Enter a wrong ticket number.
        """
        response = self.client.post(reverse('vote:enter_ticket'), {'ticket': TESTS['number1']})
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(response.context['message'], "Aucun bureau de vote ne correspond à votre ticket.")

    def test_accessGET_log_vote_page(self):
        """Test access on the page vote of a
        connected user with GET method and right args.
        The user's ballot has already been completed.
        """
        vote = self.vote
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('vote:vote', args=(vote.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_accessGET2_log_vote_page(self):
        """Test access on the page vote of a
        connected user with GET method and right args.
        The user's ballot has never been completed.
        """
        vote = self.vote
        vote.ballot = 1
        vote.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('vote:vote', args=(vote.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(response.context['message'], "Vous avez déjà utilisé votre ticket pour voter.")

    def test_accessPOST_log_vote_page(self):
        """Test access on the page vote of a
        connected user with POST method and right args.
        """
        vote = self.vote
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(reverse('vote:vote', args=(vote.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(response.context['message'], "Votre vote a bien été enregistré.")
    
    def test_access_unlog_vote_page(self):
        """Test access on the page vote of an
        ananymous user with GET method and right args
        """
        vote = self.vote
        response = self.client.get(reverse('vote:vote', args=(vote.id+1, )))
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])