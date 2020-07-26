# coding: utf-8
"""Create formular for account
templates and views.
"""
from django import forms


class ConnexionForm(forms.Form):
    """Formular Class Form.
    Used in account templates and views for login.
    """
    email = forms.CharField(label="E-mail:", max_length=30)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)


class CountCreationForm(forms.Form):
    """Formular Class Form.
    Used in account templates and views for account creation.
    """
    username = forms.CharField(label="Pseudo:", max_length=30)
    first_name = forms.CharField(label="Prénom:", max_length=50)
    last_name = forms.CharField(label="Nom:", max_length=50)
    email = forms.EmailField(label="E-mail:")
    school = forms.CharField(label="Ecole:", max_length=75)
    departement = forms.IntegerField(label="Département:")
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repeat Password:", widget=forms.PasswordInput)


class CountModificationForm(forms.Form):
    """Formular Class Form.
    Used in account templates and views for account modification.
    """
    username = forms.CharField(label="Pseudo:", max_length=30)
    first_name = forms.CharField(label="Prénom:", max_length=50)
    last_name = forms.CharField(label="Nom:", max_length=50)
    school = forms.CharField(label="Ecole:", max_length=75)
    departement = forms.IntegerField(label="Département:")
