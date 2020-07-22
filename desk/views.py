# coding: utf-8
"""Run the views for Desk APP.
Views:
-create_desk(request):@login_required
-modify_desk(request):@login_required
-start_desk(request):@login_required
-close_desk(request):@login_required
-delete_desk(request):@login_required
-display_desk_list(request):@login_required
-display_active_desk(request):@login_required
"""
import random, string

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from desk.models import Desk, Ticket, Candidate
from account.models import Account
from desk.forms import DeskCreationForm, AddCandidateForm

@login_required
def create_desk(request):
    """Front page of web site.
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
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
            number_candidate = form.cleaned_data["number_candidate"]
            open_vote = form.cleaned_data["opening_vote"]
            
            
            desk_control = Desk.objects.filter(school=school, school_class=school_class)
            if not desk_control:
                new_desk = Desk.objects.create(
                    school = school,
                    school_class = school_class,
                    closing_vote = timezone.now(),
                    opening_vote = timezone.now(),
                    winners = "(0,0,0)",
                    number_voters = 0,
                    tickets_amount = tickets_amount,
                    status = "C"
                )
                if open_vote==1:
                    new_desk.status.add("O")
                
                user.account.desk_link.add(new_desk)

                new_desk.save()
                user.account.save()
                new_desk_id = new_desk.id
                adding_candidate = True
                desk_complete = True
            else:
                existing_desk = True    
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
    """Front page of web site.
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
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
                first_name = first_name, last_name = last_name,
                school=desk.school, classroom=desk.school_class)

            if not candidate_control:
                new_candidate = Candidate.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    school = desk.school,
                    classroom = desk.school_class
                )
                new_candidate.save()
                desk.candidates.add(new_candidate)
                desk.save()
                adding_candidate = True
            else:
                desk_control = Desk.objects.filter(
                candidates=candidate_control[0])
                if not desk_control:
                    new_candidate = candidate_control[0]
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
        "double_candidate":double_candidate,
        "adding_candidate": adding_candidate,
        "new_candidate": new_candidate,
        "desk_id": desk_id,
        "number_candidate": number_candidates,
    }
    return render(request, 'desk/add_candidates.html', context)

@login_required
def create_tickets(request, desk_id):
    """Front page of web site.
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
    """
    desk = get_object_or_404(Desk, id=desk_id)
    existing_tickets = len(Ticket.objects.filter(desk_tickets=desk))
    zero_ticket = False
    to_much_tickets = False
    ticket_number = 0
    tickets_list = []
    if existing_tickets==0:
        for ticket in range(desk.tickets_amount):
            ticket_number += 1
            base_ticket_code = "".join(random.choices(string.ascii_letters + string.digits, k=12))

            new_ticket = Ticket.objects.create(
                ticket_number = ticket_number,
                ticket_code = "".join([base_ticket_code, str(ticket_number), str(desk_id)]),
                desk_tickets = desk
            )
            new_ticket.save()
            tickets_list.append(new_ticket)
            existing_tickets = len(Ticket.objects.all().filter(desk_tickets=desk))
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
    user = request.user
    desk_list = [Desk.objects.filter(account=user.id)]
    print(desk_list[0])
    context = {
        "desk_list": desk_list,
        "desk_number": len(desk_list),
    }
    return render(request, 'desk/display_desk_list.html', context)

@login_required
def modify_desk(request):
    pass

@login_required
def start_desk(request):
    pass

@login_required
def close_desk(request):
    pass

@login_required
def delete_desk(request):
    pass

@login_required
def display_active_desk(request):
    pass