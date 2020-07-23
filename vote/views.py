# coding: utf-8
"""Run the views for Desk APP.
Views:
-create_vote(request):@login_required
-vote(request, desk_id):@login_required
-create_tickets(request, desk_id):@login_required
-display_desk_list(request):@login_required
-delete_desk(request, desk_id):@login_required
-open_desk(request, desk_id):@login_required
-close_desk(request, desk_id):@login_required
-display_active_desk(request, desk_id):@login_required
-delete_candidate(request, candidate_id, desk_id):@login_required
-add_voters(request, desk_id):@login_required
"""
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from desk.models import Desk, Ticket, Candidate
from vote.models import Vote
from vote.forms import EnterTicketForm, VoteForm

def enter_ticket(request):
    """Display a window  to log
    a desk with a ticket.
    user.
    Arguments:
    -request {GET}
    Returns:
    -template -- vote/enter_ticket.html
    -context ()
    """
    message = ""
    validate_ticket = False
    new_vote = None

    if request.method == "POST":
        form = EnterTicketForm(request.POST)
        if form.is_valid():
            ticket = form.cleaned_data["ticket"]
            right_ticket = Ticket.objects.get(ticket_code=ticket)
            if right_ticket:
                desk = Desk.objects.get(ticket=right_ticket.id)
                new_vote = Vote.objects.create(
                    ballot = "0",
                    desk_votes = desk,
                )
                new_vote.save()
                message = "Votre ticket est validé. Vous pouvez voter."
                validate_ticket = True
            else:
                message = "Aucun bureau de vote ne correspond à votre ticket."
            right_ticket.delete()
    else:
        form = EnterTicketForm()
    context = {
        "form": form,
        "message": message,
        "new_vote": new_vote,
        "validate_ticket": validate_ticket,
    }
    return render(request, 'vote/enter_ticket.html', context)

def vote(request, vote_id):
    """Create a new vote formular for a voter
    who gives a correct ticket.
    user.
    Arguments:
    -request {GET}
    Returns:
    -template -- vote/create_vote.html
    -context ()
    """
    new_ballot = True
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            ticket = form.cleaned_data["ticket"]
        else:
            form = VoteForm()
    else:
            form = VoteForm()
    context = {
        "new_ballot": new_ballot,
    }
    return render(request, 'vote/vote.html', context)