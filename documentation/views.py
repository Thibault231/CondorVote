# coding: utf-8
"""Run the views for documentation APP.
Views:
-voter_infos(request)
-organizer_infos(request)
-condorcet_infos(request)
"""
from django.shortcuts import render


def voter_infos(request):
    """Displays informations windows
    for FAC for voters.
    Arguments:
    -request {GET}
    Returns:
    -template -- documentation/voter_infos.html
    """
    return render(request, 'documentation/voter_infos.html')


def organizer_infos(request):
    """Displays informations windows
    for FAC for organizers.
    -request {GET}
    Returns:
    -template -- documentation/organizer_infos.html
    """
    return render(request, 'documentation/organizer_infos.html')


def condorcet_infos(request):
    """Displays informations windows
    for FAC about Condorcet's election.
    Arguments:
    -request {GET}
    Returns:
    -template -- documentation/voter_infos.html
    """
    return render(request, 'documentation/condorcet_infos.html')
