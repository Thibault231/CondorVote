# coding: utf-8
""" Module managing urls of
account APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('connexion/', views.connexion, name='connexion'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path(
        'account_creation/',
        views.account_creation, name='account_creation'),
    path(
        'modify_account/',
        views.modify_account, name='modify_account'),
    path(
        'delete_confirmation/',
        views.delete_confirmation, name='delete_confirmation'),
]
