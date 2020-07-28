from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from desk.models import Desk, Ticket, Candidate
from desk.forms import AddCandidateForm


@api_view(['POST'])
def adding_cand(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        form = AddCandidateForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            desk_id = form.cleaned_data["desk_id"]

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
                message = "Le candidat {} {} a bien été ajouté".format(new_candidate.first_name, new_candidate.last_name)
            else:
                desk_control = Desk.objects.filter(
                    candidates=candidate_control[0]
                )
                if not desk_control:
                    new_candidate = candidate_control[0]
                    desk.candidates.add(new_candidate)
                    desk.save()
                    message = "Erreur: Aucun bureau de vote de ce nom n'a été trouvé"
                else:
                    new_candidate = candidate_control[0]
                    message = "Le candidat {} {} a déjà été ajouté".format(new_candidate.first_name, new_candidate.last_name)
                    
            return Response({'message': message})
        else:
            return Response({'message': 'Not found'})
        return Response({'message':'Not found'})
    return Response({'message':'Not found'})

