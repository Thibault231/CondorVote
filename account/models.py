# coding: utf-8
"""Defines models for account APP.

Models:
-Account
"""
from django.db import models
from django.contrib.auth.models import User
from desk.models import Desk

# Create your models here.
class Account(models.Model):
    """Model Account
    Arguments:
    models {Model}
    Attributs:
    -user = name of user.
    -school = name of school.
    -departement = departement of school.
    -desk_link = link ManyToMany. Desks linked to the account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    departement = models.IntegerField()
    desk_link = models.ManyToManyField(Desk)

    class Meta:
        """Define verbose_name
        """
        verbose_name = "account"

    def __str__(self):
        """Return name when Account object
        is called
        Returns:
            [str] -- attribute name
        """
        return "Account of: {0}".format(self.user.username)


