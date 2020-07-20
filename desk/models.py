# coding: utf-8
"""Defines models for Desk APP.

Models:
-Desk
-Candidate
-Ticket
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidate(models.Model):
    """Model Candidate, contain all candidates of all desks.
    Arguments:
    -first_name 
    -last_name 
    -school
    -classroom 
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "candidate"

    def __str__(self):
        """Return name when Candidate object
        is called
        Returns:
            [str] -- attribute name
        """
        return "candidate: {0}".format(self.candidate.last_name)

class Desk(models.Model):
    """Model Desk, define the objet that rule a classroom
    election.

    Arguments:
    -school = school name
    -school_class = classroom name
    -opening_vote = date from starting election
    -closing_vote = date of stopping election
    -status = create, open, close
    -winners = list of winners
    -number_voters = number of voters who have voted
    -tickets_amount = number of voters
    -candidates = link one to many. List of candidates
    -tickets = link one to many. List of tickets
    -votes = link one to many. List of ballots
    """
    school = models.CharField(max_length=50)
    school_class = models.CharField(max_length= 20)
    opening_vote = models. DateTimeField()
    closing_vote = models. DateTimeField()
    status = models.CharField(max_length=1)
    winners = models.CharField(max_length=100)
    number_voters = models.IntegerField()
    tickets_amount = models.IntegerField()
    candidates = models.ManyToManyField(Candidate)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "desk"

    def __str__(self):
        """Return name when Desk object
        is called
        Returns:
            [str] -- attribute name
        """
        return "Desk ID: {0}".format(self.desk.id)


class Ticket(models.Model):
    """Model Account
    Arguments:
    models {Model}
    Attributs:
    -desk (oneToMany link)
    -history
    """
    ticket_number = models.IntegerField()
    ticket_code = models.CharField(max_length=20)
    desk_tickets = models.ForeignKey(Desk, on_delete=models.CASCADE)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "ticket"

    def __str__(self):
        """Return name when Ticket object
        is called
        Returns:
            [str] -- attribute name
        """
        return "Ticket number: {0}".format(self.ticket.ticket_number)
