# coding: utf-8
""" Module managing urls of
vote APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('enter_ticket/', views.enter_ticket, name='enter_ticket'),
    path('vote/<vote_id>/', views.vote, name='vote'),
]
