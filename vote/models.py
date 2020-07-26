# coding: utf-8
"""Defines models for vote APP.

Models:
-Vote
"""
from django.db import models
from django.contrib.auth.models import User
from desk.models import Desk

# Create your models here.
class Vote(models.Model):
    """Model Vote
    Arguments:
    models {Model}
    Attributs:
    -ballot = list of ordered best liked candidates.
    """
    ballot = models.CharField(max_length=100)
    desk_votes = models.ForeignKey(Desk, on_delete=models.CASCADE)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "vote"

    def __str__(self):
        """Return name when Vote object
        is called
        Returns:
            [str] -- attribute name
        """
        return "Vote ID: {0}".format(self.id)
