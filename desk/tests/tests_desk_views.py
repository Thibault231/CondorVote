# coding: utf-8
"""Unitary tests for desk APP's
functions of views.py.
Tests:
-test_vote_table_args(self)
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from account.models import Account
from desk.models import Desk, Ticket, Candidate
from common.config import TESTS3, TESTS


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

    def test_access_log_desk_creation_page(self):
        """Test access on the page desk_creation of an
        anonymous user with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('desk:create_desk'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_desk_creation_page(self):
        """Test access on the page desk_creation of a
        connected user with GET method and right args
        """
        response = self.client.get(reverse('desk:create_desk'))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_right_desk_creation_page(self):
        """Test the creation of a new desk for a
        connected user with GET method and right args.
        Views: create_desk.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.post(reverse('desk:create_desk'), {
            'school': TESTS['school'],
            'school_class': TESTS['name1'],
            'tickets_amount': TESTS['number1'],
            'number_candidate': TESTS['number1'],
            'opening_vote': 1,
            })
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_log_display_desk_list_page(self):
        """Test access on the page desk_creation of an
        anonymous user with GET method and right args
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('desk:display_desk_list'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_display_desk_list_page(self):
        """Test access on the page desk_creation of a
        connected user with GET method and right args
        """
        response = self.client.get(reverse('desk:display_desk_list'))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_add_candidate_page(self):
        """Test access on the page desk_creation of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:add_candidates', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_add_candidate_page(self):
        """Test access on the page desk_creation of a
        connected user with GET method and right args
        """
        desk = self.desk
        response = self.client.get(
            reverse('desk:add_candidates', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_rightadd_candidate_page(self):
        """Test adding candidate to a specific desk of a
        connected user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:add_candidates', args=(desk.id, )),
            {
                'first_name': TESTS['name2'],
                'last_name': TESTS['name2'],
            }
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_log_create_tickets_page(self):
        """Test access on the page desk_creation of a
        loged user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:create_tickets', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_create_tickets_page(self):
        """Test access on the page desk_creation of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        response = self.client.get(
            reverse('desk:create_tickets', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_delete_desk_page(self):
        """Test access on the page delete_desk of a
        loged user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:delete_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_delete_desk_page(self):
        """Test access on the page delete_desk of an
        anonymous user with GET method and right args
        """
        desk = self.desk
        response = self.client.get(
            reverse('desk:delete_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_open_desk_page(self):
        """Test access on the page open_desk of a
        loged user with GET method and right args.
        """
        desk = self.desk
        desk.status = TESTS3['StatusCreate']
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('desk:open_desk', args=(desk.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(response.context["desk_status"], TESTS3['StatusOpen'])

    def test_access_unlog_open_desk_page(self):
        """Test access on the page open_desk of a
        anonymous user with GET method and right args
        """
        desk = self.desk
        desk.status = TESTS3['StatusCreate']
        response = self.client.get(reverse('desk:open_desk', args=(desk.id, )))
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_wrongStatus_open_desk_page(self):
        """Test access on the page open_desk of a
        connected user and a wrong desk_status.
        Use GET method and right args.
        """
        desk = self.desk
        desk.status = TESTS3['StatusClose']
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('desk:open_desk', args=(desk.id, )))
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(
            response.context["desk_status"], TESTS3['StatusClose']
        )

    def test_access_log_close_desk_page(self):
        """Test access on the page close_desk of a
        loged user with GET method and right args.
        """
        desk = self.desk
        desk.status = TESTS3['StatusOpen']
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:close_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(
            response.context["desk_status"], TESTS3['StatusClose']
        )

    def test_access_unlog_close_desk_page(self):
        """Test access on the page close_desk of an
        annonymous user with GET method and right args.
        """
        desk = self.desk
        desk.status = TESTS3['StatusOpen']
        response = self.client.get(
            reverse('desk:close_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_wrongStatus_close_desk_page(self):
        """Test access on the page close_desk of a
        connected user and a wrong desk_status.
        Use GET method and right args.
        """
        desk = self.desk
        desk.status = TESTS3['StatusCreate']
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:close_desk', args=(desk.id, ))
        )
        self.assertEqual(
            response.status_code, TESTS['RightStatus']
        )
        self.assertEqual(
            response.context["desk_status"], TESTS3['StatusCreate']
        )

    def test_access_log_display_active_desk_page(self):
        """Test access on the page display_active_desk of a
        loged user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:display_active_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_display_active_desk_page(self):
        """Test access on the page display_active_desk of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        response = self.client.get(
            reverse('desk:display_active_desk', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_access_log_add_voters_page(self):
        """Test access on the page add_voters of a
        loged user with GET method and right args.
        """
        desk = self.desk
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:add_voters', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_add_voters_page(self):
        """Test access on the page add_voters of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        response = self.client.get(
            reverse('desk:add_voters', args=(desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])

    def test_Tickets_add_voters_page(self):
        """Test the modification of tickets_amount
        for the desk modify by add_voters.
        Need a loged user with GET method and right args.
        """
        desk = self.desk
        desk.tickets_amount = TESTS['number1']
        desk.save()
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:add_voters', args=(desk.id, )),
            {'tickets_amount': TESTS['number1']+1}
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])
        self.assertEqual(
            response.context["desk"].tickets_amount, TESTS['number1']
        )

    def test_access_log_delete_candidate_page(self):
        """Test access on the page delete_candidate of a
        loged user with GET method and right args.
        """
        desk = self.desk
        candidate = self.candidate
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(
            reverse('desk:delete_candidate', args=(candidate.id, desk.id, ))
        )
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_access_unlog_delete_candidate_page(self):
        """Test access on the page delete_candidate of an
        anonymous user with GET method and right args.
        """
        desk = self.desk
        candidate = self.candidate
        response = self.client.get(
            reverse(
                'desk:delete_candidate',
                args=(candidate.id, desk.id, )
            )
        )
        self.assertEqual(response.status_code, TESTS['WrongStatus'])
