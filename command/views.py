# coding: utf-8
"""Run the views for Command APP.
Views:
-adding_cand(request):
"""
import json
from django.shortcuts import HttpResponse
from desk.models import Desk, Candidate
from desk.forms import AddCandidateForm


def adding_cand(request):
    number_candidate = ""
    if request.method == "POST":
        form = AddCandidateForm(request.POST)
        if request.is_ajax():
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
