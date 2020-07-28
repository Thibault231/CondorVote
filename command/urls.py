# coding: utf-8
""" Module managing urls of
command APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path(
        'add_candidates/<desk_id>/',
        views.add_candidates,
        name='add_candidates'),
]