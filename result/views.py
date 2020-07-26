# coding: utf-8
"""Run the views for Desk APP.
Views:
-result(request, desk_id): @login_required
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from vote.models import Vote
from desk.models import Desk, Candidate
from result.result_process import candidates_duals


@login_required
def result(request, desk_id):
    """Define the winners of the election.
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- result/result.html
    -context ("winners_list", "message".)
    """
    desk = get_object_or_404(Desk, id=desk_id)
    votes_list = Vote.objects.filter(desk_votes=desk)
    candidates_list = Candidate.objects.filter(desk=desk)
    id_candidates_list = []
    for candidate in candidates_list:
        id_candidates_list.append(candidate.id)

    vote_matrix, victories_matrix, winner_list = candidates_duals(
        votes_list, len(candidates_list)
    )
    for candidate in winner_list:
        candidate[1] = "{} _ {}".format(
            candidates_list[candidate[1]].first_name.capitalize(),
            candidates_list[candidate[1]].last_name.upper()
        )

    desk.winners = winner_list
    desk.save()

    context = {
        "winners_list": winner_list,
        "message": len(winner_list),
    }

    return render(request, 'result/result.html', context)


@login_required
def result_details(request, desk_id):
    """Détails all the aspects of a closed
    election's desk results.
    .
    Arguments:
    -request {GET}
    -desk_id {int}
    Returns:
    -template -- result/result_details.html
    -context ("winners_list",)
    """
    desk = get_object_or_404(Desk, id=desk_id)
    votes_list = Vote.objects.filter(desk_votes=desk)
    candidates_list = Candidate.objects.filter(desk=desk)
    id_candidates_list = []
    for candidate in candidates_list:
        id_candidates_list.append(candidate.id)

    vote_matrix, victories_matrix, winner_list = candidates_duals(
        votes_list, len(candidates_list))

    for candidate in winner_list:
        candidate[1] = "{} _ {}".format(
            candidates_list[candidate[1]].first_name.capitalize(),
            candidates_list[candidate[1]].last_name.upper()
        )
    desk.winners = winner_list
    desk.save()

    candidates_names_list = []
    for candidate in candidates_list:
        candidates_names_list.append("{} {}".format(
            candidate.first_name.capitalize(),
            candidate.last_name.upper()
            )
        )

    victories_matrix = victories_matrix.tolist()
    for element in victories_matrix:
        candidate_name = candidates_names_list[victories_matrix.index(element)]
        element.insert(0, candidate_name)

    vote_matrix = vote_matrix.tolist()
    for element in vote_matrix:
        candidate_name = candidates_names_list[vote_matrix.index(element)]
        element.insert(0, candidate_name)

    context = {
        "vote_matrix": vote_matrix,
        "victories_matrix": victories_matrix,
        "candidates_list": candidates_list,
        "winners_list": winner_list,
        "message": len(winner_list),
    }

    return render(request, 'result/result_details.html', context)
