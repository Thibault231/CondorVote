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
]