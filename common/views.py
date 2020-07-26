# coding: utf-8
"""Run the views for common APP.
Views:
-index(request)
-legal_mentions(request)
-error400(request)
-error404(request)
-error500(request)
"""
from django.shortcuts import render


def index(request):
    """Front page of web site.
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
    """
    return render(request, 'common/index.html')


def legal_mentions(request):
    """Rule the legal notice of the website;
    Arguments:
    -request {GET}
    Returns:
    -template -- legal_mentions.html
    """
    return render(request, 'common/legal_mentions.html')


def error400(request):
    """Specific function for testing error templates:
    400.htlm;
    Arguments:
    -request {GET}
    Returns:
    -template -- legal_mentions.html
    """
    return render(request, '400.html')


def error404(request):
    """Specific function for testing error templates:
    404.htlm;
    Arguments:
    -request {GET}
    Returns:
    -template -- legal_mentions.html
    """
    return render(request, '404.html')


def error500(request):
    """Specific function for testing error templates:
    500.htlm;
    Arguments:
    -request {GET}
    Returns:
    -template -- legal_mentions.html
    """
    return render(request, '500.html')
