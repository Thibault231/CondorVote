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
from django.shortcuts import render, get_object_or_404
from desk.models import Desk, Ticket, Candidate
from vote.models import Vote
from vote.forms import EnterTicketForm


def enter_ticket(request):
    """Display a window  to log
    a desk with a ticket.
    user.
    Arguments:
    -request {GET}
    Returns:
    -template -- vote/enter_ticket.html
    -context ("form", "message", "new_vote",
        "validate_ticket")
    """
    message = ""
    validate_ticket = False
    new_vote = None

    if request.method == "POST":
        form = EnterTicketForm(request.POST)
        if form.is_valid():
            ticket = form.cleaned_data["ticket"]
            right_ticket = Ticket.objects.filter(ticket_code=ticket)
            if right_ticket:
                right_ticket = right_ticket[0]
                desk = Desk.objects.get(ticket=right_ticket.id)
                new_vote = Vote.objects.create(
                    ballot="0",
                    desk_votes=desk,
                )
                new_vote.save()
                desk.number_voters += 1
                desk.save()
                message = "Votre ticket est validé. Vous pouvez voter."
                validate_ticket = True
                right_ticket.delete()
            else:
                message = "Aucun bureau de vote ne correspond à votre ticket."

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
    -vote_id (int)
    Returns:
    -template -- vote/create_vote.html
    -context ("new_ballot", "message", "candidates_list",
        "number_candidates")
    """
    new_ballot = False
    new_vote = get_object_or_404(Vote, id=vote_id)
    candidates_list = Candidate.objects.filter(desk=new_vote.desk_votes)
    message = ""

    if request.method == "POST":
        ballot = []
        message = "Votre vote a bien été enregistré."
        for element in request.POST:
            ballot.append([element, request.POST.get(element)])
        ballot = ballot[1:]
        new_vote.ballot = list.copy(ballot)
        new_vote.save()
        new_ballot = True
    elif new_vote.ballot == "0":
        message = "Indiquez une valeur\
            entre 1 et {} pour chaque candidat.".format(
                len(candidates_list))
    else:
        message = "Vous avez déjà utilisé votre ticket pour voter."
        new_ballot = True

    context = {
        "new_ballot": new_ballot,
        "message": message,
        "candidates_list": candidates_list,
        "number_candidates": len(candidates_list),
    }
    return render(request, 'vote/vote.html', context)
