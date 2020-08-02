# coding: utf-8
"""Run the views for Command APP.
Views:
-adding_cand(request):
"""
import json
import random
import string
from django.shortcuts import HttpResponse
from desk.models import Desk, Ticket, Candidate
from desk.forms import AddCandidateForm


def adding_cand(request):
    number_candidate = ""
    if request.method == "POST":
        form = AddCandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            desk_id = request.POST["desk_id"]
            desk_control = Desk.objects.filter(id=desk_id)

            if not desk_control:
                message = "Erreur: Aucun bureau\
                        de vote de ce nom n'a été trouvé"
            else:
                desk = desk_control[0]
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
                    number_candidate = len(Candidate.objects.filter(desk=desk))
                    message = "Le candidat {} {} a bien été ajouté".format(
                        new_candidate.first_name, new_candidate.last_name)
                else:
                    new_candidate = candidate_control[0]
                    number_candidate = len(Candidate.objects.filter(desk=desk))
                    message = "Le candidat {} {} a déjà été ajouté".format(
                        new_candidate.first_name, new_candidate.last_name)

        else:
            message = 'Invalid formular'
    else:
        message = 'Methode not allowed'
    message = json.dumps(
        {
            'message': message,
            'number_candidate': number_candidate})
    return HttpResponse(message)


def adding_tickets(request):
    number_tickets = ""
    if request.method == "POST":
        new_amount = int(request.POST["new_amount"])
        desk_id = request.POST["desk_id"]
        desk_control = Desk.objects.filter(id=desk_id)

        if not desk_control:
            message = "Erreur: Aucun bureau\
                    de vote de ce nom n'a été trouvé"
        else:
            desk = desk_control[0]
            ticket_control = Ticket.objects.filter(desk_tickets=desk)
            cursor = 0
            tickets_number = len(ticket_control)
            for ticket in range(new_amount):
                cursor += 1
                base_ticket_code = "".join(
                    random.choices(
                        string.ascii_letters + string.digits,
                        k=12
                    )
                )
                new_ticket = Ticket.objects.create(
                    ticket_number=tickets_number,
                    ticket_code="".join(
                        [
                            base_ticket_code,
                            str(tickets_number+cursor),
                            str(desk_id)
                        ]
                    ),
                    desk_tickets=desk
                )
                new_ticket.save()
            number_tickets = len(
                    Ticket.objects.all().filter(desk_tickets=desk))
            desk.tickets_amount = number_tickets
            desk.save()
            message = "Les tickets ont bien été ajoutés.\n"+\
                "Vous disposez de {} tickets pour ce bureau".format(
                    number_tickets-1)
    else:
        message = 'Methode not allowed'
    message = json.dumps(
        {
            'message': message,
            'number_tickets': number_tickets})
    return HttpResponse(message)