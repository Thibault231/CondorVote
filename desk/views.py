# coding: utf-8
"""Run the views for Desk APP.
Views:
-create_desk(request)
-vote(request)
-enter_ticket(request)
"""
import random
import string
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from desk.models import Desk, Ticket, Candidate
from desk.forms import DeskCreationForm, AddCandidateForm, AddVotersForm


@login_required
def create_desk(request):
    """Create a new desk for a connected
    user.
    Arguments:
    -request {GET}
    Returns:
    -template -- create_desk.html
    -context ("form", "new_desk",
        "existing_desk","desk_complete")
    """
    desk_complete = False
    user = request.user
    existing_desk = False
    new_desk_id = None

    if request.method == "POST":
        form = DeskCreationForm(request.POST)
        if form.is_valid():
            school = form.cleaned_data["school"]
            school_class = form.cleaned_data["school_class"]
            tickets_amount = form.cleaned_data["tickets_amount"]
            open_vote = form.cleaned_data["opening_vote"]

            desk_control = Desk.objects.filter(
                school=school,
                school_class=school_class
            )
            if not desk_control:
                new_desk = Desk.objects.create(
                    school=school,
                    school_class=school_class,
                    closing_vote=timezone.now(),
                    opening_vote=timezone.now(),
                    winners="(0,0,0)",
                    number_voters=0,
                    tickets_amount=tickets_amount,
                    status="C"
                )
                if int(open_vote) == 1:
                    new_desk.status = "O"
                    new_desk.save()

                user.account.desk_link.add(new_desk)
                user.account.save()
                new_desk_id = new_desk.id
                desk_complete = True
                return redirect(
                    '/desk/add_candidates/{}/'.format(new_desk.id)
                )
            else:
                old_desk = desk_control[0]
                existing_desk = True
                return redirect(
                    '/desk/add_candidates/{}/'.format(old_desk.id)
                )

    else:
        form = DeskCreationForm()
    context = {
        "form": form,
        "new_desk": new_desk_id,
        "existing_desk": existing_desk,
        "desk_complete": desk_complete,
    }

    return render(request, 'desk/create_desk.html', context)


@login_required
def add_candidates(request, desk_id):
    """Add candidates to a specific desk
    for a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/add_candidates.html
    -context {"form", "double_candidate",
        "adding_candidate", "new_candidate",
        "desk_id","number_candidate"}
    """
    adding_candidate = False
    double_candidate = False
    new_candidate = None
    desk = get_object_or_404(Desk, id=desk_id)

    if request.method == "POST":
        form = AddCandidateForm(request.POST)
        double_candidate = False

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            candidate_control = Candidate.objects.filter(
                first_name=first_name, last_name=last_name,
                school=desk.school, classroom=desk.school_class)

            if not candidate_control:
                new_candidate = Candidate.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    school=desk.school,
                    classroom=desk.school_class
                )
                new_candidate.save()
                desk.candidates.add(new_candidate)
                desk.save()
                adding_candidate = True
            else:
                new_candidate = candidate_control[0]
                double_candidate = True
                adding_candidate = False

    form = AddCandidateForm()
    number_candidates = len(Candidate.objects.all().filter(desk=desk))

    context = {
        "form": form,
        "double_candidate": double_candidate,
        "adding_candidate": adding_candidate,
        "new_candidate": new_candidate,
        "desk_id": desk_id,
        "number_candidate": number_candidates,
    }
    return render(request, 'command/add_candidates.html', context)


@login_required
def create_tickets(request, desk_id):
    """Create a specifif amount of tickets for
    a specific desk. Need a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/create_tickets.html
    -context {"desk", "tickets_list", "existing_tickets",
        "zero_ticket", "to_much_tickets"}
    """
    desk = get_object_or_404(Desk, id=desk_id)
    existing_tickets = len(Ticket.objects.filter(desk_tickets=desk))
    zero_ticket = False
    to_much_tickets = False
    ticket_number = 0
    tickets_list = []

    if existing_tickets == 0:
        for ticket in range(desk.tickets_amount):
            ticket_number += 1
            base_ticket_code = "".join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=12
                )
            )

            new_ticket = Ticket.objects.create(
                ticket_number=ticket_number,
                ticket_code="".join(
                    [
                        base_ticket_code,
                        str(ticket_number),
                        str(desk_id)
                    ]
                ),
                desk_tickets=desk
            )
            new_ticket.save()
            tickets_list.append(new_ticket)
            existing_tickets = len(
                Ticket.objects.all().filter(desk_tickets=desk)
            )
    else:
        tickets_list = Ticket.objects.all().filter(desk_tickets=desk)

    context = {
        "desk": desk,
        "tickets_list": tickets_list,
        "existing_tickets": existing_tickets,
        "zero_ticket": zero_ticket,
        "to_much_tickets": to_much_tickets,
    }
    return render(request, 'desk/create_tickets.html', context)


@login_required
def display_desk_list(request):
    """Display an ordered list of the user's
    desks. Need a loged user.
    Arguments:
    -request {GET}
    Returns:
    -template -- desk/display_desk_list.html
    -context {desk_list_c", "desk_list_o",
        "desk_list_e", "desk_number"}
    """
    user = request.user
    desk_list = Desk.objects.filter(account=user.account.id)

    context = {
        "desk_list": desk_list,
        "desk_number": len(desk_list),
    }
    return render(request, 'desk/display_desk_list.html', context)


@login_required
def delete_desk(request, desk_id):
    """Delete a specific desk of a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/display_desk_list.html
    -context {"desk_school", "desck_school_class"}
    """
    desk = Desk.objects.filter(id=desk_id)
    if desk:
        desk = desk[0]
        desk.delete()

    user = request.user
    desk_list = Desk.objects.filter(account=user.account.id)

    context = {
        "desk_list": desk_list,
        "desk_number": len(desk_list),
        "message": "Le bureau de vote a bien été supprimé!",
    }
    return render(request, 'desk/display_desk_list.html', context)


@login_required
def open_desk(request, desk_id):
    """Open a created unopend desk to voters.
    Need a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/display_desk_list.html
    -context {""desk_list_c": desk_list_c,
        "desk_list_o", "desk_list_e", "desk_number""}
    """
    desk = get_object_or_404(Desk, id=desk_id)
    if desk.status == "C":
        desk.status = "O"
        desk.opening_vote = timezone.now()
        desk.save()

    user = request.user
    desk_list = Desk.objects.filter(account=user.account.id)

    context = {
        "desk_list": desk_list,
        "desk_number": len(desk_list),
        "desk_status": desk.status,
    }
    return render(request, 'desk/display_desk_list.html', context, )


@login_required
def close_desk(request, desk_id):
    """Close an opened desk to voters.
    Need a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/display_desk_list.html
    -context {""desk_list_c": desk_list_c,
        "desk_list_o", "desk_list_e", "desk_number""}
    """
    desk = get_object_or_404(Desk, id=desk_id)
    if desk.status == "O":
        desk.status = "E"
        desk.closing_vote = timezone.now()
        desk.save()

    user = request.user
    desk_list = Desk.objects.filter(account=user.account.id)

    context = {
        "desk_list": desk_list,
        "desk_number": len(desk_list),
        "desk_status": desk.status,
    }
    return render(request, 'desk/display_desk_list.html', context)


@login_required
def display_active_desk(request, desk_id):
    """Displays all details of a specific desk.
    Need a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/display_active_desk.html
    -context {"desk": desk, "winners", "status",
        "tickets_list", "candidates_list"}
    """
    desk = get_object_or_404(Desk, id=desk_id)
    candidates_list = Candidate.objects.filter(desk=desk_id)
    tickets_list = Ticket.objects.filter(desk_tickets=desk_id)
    winners = desk.winners

    if desk.status == "C":
        status = "Créé/Non ouvert"
    elif desk.status == "O":
        status = "Ouvert"
    elif desk.status == "E":
        status = "clôturé"

    context = {
        "desk": desk,
        "winners": winners,
        "status": status,
        "tickets_list": tickets_list,
        "remaining_tickets": len(tickets_list),
        "candidates_list": candidates_list
    }
    return render(request, 'desk/display_active_desk.html', context)


@login_required
def delete_candidate(request, candidate_id, desk_id):
    """Delete a specific candidate of a specific desk.
    Need a connected user.
    Arguments:
    -request {GET}
    -candidate_id {int}
    -desk_id {int}
    Returns:
    -template -- desk/display_active_desk.html
    -context {"desk", "winners", "status", "candidates_list"}
    """
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.delete()

    desk = get_object_or_404(Desk, id=desk_id)
    candidates_list = Candidate.objects.filter(desk=desk_id)
    tickets_list = Ticket.objects.filter(desk_tickets=desk_id)

    if desk.status == "C":
        status = "Créé/Non ouvert"
    elif desk.status == "O":
        status = "Ouvert"
    elif desk.status == "E":
        status = "clôturé"

    context = {
        "desk": desk,
        "status": status,
        "winners": desk.winners,
        "tickets_list": tickets_list,
        "remaining_tickets": len(tickets_list),
        "candidates_list": candidates_list
    }
    return render(request, 'desk/display_active_desk.html', context)


@login_required
def add_voters(request, desk_id):
    """Change the tickets_amount parameter
    of a specific desk and generate new tickets.
    Need a connected user.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- desk/add_voters.html
    -context {"desk", "form", "adding_voters",
        "message"}
    """
    desk = get_object_or_404(Desk, id=desk_id)
    adding_voters = False
    message = ""

    if request.method == "POST":
        form = AddVotersForm(request.POST)
        if form.is_valid():
            tickets_amount = form.cleaned_data["tickets_amount"]
            if tickets_amount > 0:
                desk.tickets_amount = tickets_amount
                desk.save()
                existing_tickets_list = Ticket.objects.filter(
                    desk_tickets=desk
                )
                for ticket in existing_tickets_list:
                    ticket.delete()
                adding_voters = True
            else:
                message = "Veuillez indiquer un nombre supérieur à zéro"
                form = AddVotersForm()
        else:
            message = "Formulaire non valide"
            form = AddVotersForm()
    else:
        form = AddVotersForm()

    context = {
        "desk": desk,
        "form": form,
        "adding_voters": adding_voters,
        "message": message,
    }
    return render(request, 'desk/add_voters.html', context)
