# coding: utf-8
""" Module managing urls of
account APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('create_desk/', views.create_desk, name='create_desk'),
    path('add_candidates/(?P<desk_id>[0-9]+)/', views.add_candidates, name='add_candidates'),
    path('create_tickets/(?P<desk_id>[0-9]+)/', views.create_tickets, name='create_tickets'),
    path('modify_desk', views.modify_desk, name='modify_desk'),
    path('start_desk/', views.start_desk, name='start_desk'),
    path('close_desk/', views.close_desk, name='close_desk'),
    path('delete_desk/', views.delete_desk, name='delete_desk'),
    path('display_desk_list/', views.display_desk_list, name='display_desk_list'),
    path('display_active_desk/', views.display_active_desk, name='display_active_desk'),
    
]