# coding: utf-8
""" Module managing urls of
result APP for Django program.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('result//<desk_id>/', views.result, name='result'),
    path(
        'result_details//<desk_id>/',
        views.result_details,
        name='result_details'),
]
