# coding: utf-8
""" Module managing urls of
common APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
    path('error400/', views.error400, name='error400'),
    path('error500/', views.error400, name='error500'),
    path('error404/', views.error400, name='error404'),
]
