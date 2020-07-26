# coding: utf-8
""" Module managing urls of
documentation APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('voter_infos/', views.voter_infos, name='voter_infos'),
    path('organizer_infos/', views.organizer_infos, name='organizer_infos'),
    path('condorcet_infos/', views.condorcet_infos, name='condorcet_infos'),
]
