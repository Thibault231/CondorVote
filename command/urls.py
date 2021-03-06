# coding: utf-8
""" Module managing urls of
command APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path(
        'adding_cand/',
        views.adding_cand,
        name='adding_cand'),
    path(
        'adding_tickets/',
        views.adding_tickets,
        name='adding_tickets'),
    path(
        'deleting_tickets/',
        views.deleting_tickets,
        name='deleting_tickets')
]
