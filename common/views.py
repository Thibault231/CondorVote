# coding: utf-8
"""Run the views for fcommon APP.
Views:
-index
-legal_mentions
"""
from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
    """Front page of web site.
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
    """
    return render(request, 'common/index.html')


def legal_mentions(request):
    pass
