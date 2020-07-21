# coding: utf-8
""" Module managing urls of
common APP for Django program.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('legal_mentions/', views.legal_mentions, name='legal_mentions')
]
