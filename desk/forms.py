# coding: utf-8
"""Create formular for Desk
templates and views.
"""
from django import forms

CHOICES = [('1', 'Oui'), ('2', 'Non')]

class DeskCreationForm(forms.Form):
    """Formular Class Form.
    Used in account templates and views for Desk creation.
    """
    school = forms.CharField(label="Etablissement scolaire:", max_length=75)
    school_class = forms.CharField(label="Nom du bureau de vote: ", max_length=75)
    tickets_amount = forms.IntegerField(label="Nombre de votants:     ")
    number_candidate = forms.IntegerField(label="Nombre de candidats:   ")
    opening_vote = forms.ChoiceField(label="Ouvrir le bureau maintenant: ", widget=forms.RadioSelect, choices=CHOICES)

class AddCandidateForm(forms.Form):
    """Formular Class Form.
    Used in account templates and views for adding candidates to desk.
    """
    first_name = forms.CharField(label="Prénom:", max_length=75)
    last_name = forms.CharField(label="Nom: ", max_length=75)
