# coding: utf-8
""" Module managing urls of
account APP for Django program.
"""
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('create_desk/', views.create_desk, name='create_desk'),
    path('add_candidates/<desk_id>/', views.add_candidates, name='add_candidates'),
    path('create_tickets/<desk_id>/', views.create_tickets, name='create_tickets'),
    path('open_desk/<desk_id>/', views.open_desk, name='open_desk'),
    path('close_desk/<desk_id>/', views.close_desk, name='close_desk'),
    path('delete_desk/<desk_id>/', views.delete_desk, name='delete_desk'),
    path('delete_candidate/<candidate_id>/<desk_id>/', views.delete_candidate, name='delete_candidate'),
     path('add_voters/<desk_id>/', views.add_voters, name='add_voters'),
    path('display_desk_list/', views.display_desk_list, name='display_desk_list'),
    path('display_active_desk/<desk_id>/', views.display_active_desk, name='display_active_desk'),  
]