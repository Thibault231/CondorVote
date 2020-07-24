# coding: utf-8
"""Create formular for Desk
templates and views.
"""
from django import forms

class EnterTicketForm(forms.Form):
    """Formular Class Form.
    Used in index template and vote APP templates and views
    for a vote object creation.
    """
    ticket = forms.CharField(max_length=75)