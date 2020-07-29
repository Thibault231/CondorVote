# coding: utf-8
"""Run the views for Command APP.
Views:
-adding_cand(request):
"""
from django.shortcuts import HttpResponse
from desk.models import Desk, Candidate
from desk.forms import AddCandidateForm


def adding_cand(request):
    if request.method == 'GET':
        return HttpResponse({'message': 'Methode not allowed'})
    elif request.method == "POST":
        form = AddCandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            desk_id = form.cleaned_data["desk_id"]

            desk = Desk.objects.filter(id=desk_id)
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
                message = "Le candidat {} {} a bien été ajouté".format(
                    new_candidate.first_name, new_candidate.last_name)
            else:
                desk_control = Desk.objects.filter(
                    candidates=candidate_control[0]
                )
                if not desk_control:
                    new_candidate = candidate_control[0]
                    desk.candidates.add(new_candidate)
                    desk.save()
                    message = "Erreur: Aucun bureau\
                         de vote de ce nom n'a été trouvé"
                else:
                    new_candidate = candidate_control[0]
                    message = "Le candidat {} {} a déjà été ajouté".format(
                        new_candidate.first_name, new_candidate.last_name)

            return HttpResponse({'message': message})
        else:
            return HttpResponse({'message': 'Not found'})
        return HttpResponse({'message': 'Not found'})
    return HttpResponse({'message': 'Not found'})
