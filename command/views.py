# coding: utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from desk.models import Desk, Ticket, Candidate
from desk.forms import DeskCreationForm, AddCandidateForm, AddVotersForm

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
                desk_control = Desk.objects.filter(
                    candidates=candidate_control[0]
                )
                if not desk_control:
                    new_candidate = candidate_control[0]
                    desk.candidates.add(new_candidate)
                    desk.save()
                    adding_candidate = True
                else:
                    new_candidate = candidate_control[0]
                    double_candidate = True
                    adding_candidate = False
            return HttpResponseRedirect('/command/add_candidates/{}'.format(desk.id))

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


