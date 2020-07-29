# coding: utf-8
"""Run the views for Desk APP.
Views:
-result(request, desk_id): @login_required
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from vote.models import Vote
from desk.models import Desk, Candidate
from result.result_process import candidates_duals, lists_for_template


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

    template_lists = lists_for_template(
        victories_matrix, vote_matrix, candidates_names_list
        )

    context = {
        "vote_matrix": template_lists[0],
        "victories_matrix": template_lists[1],
        "candidates_list": candidates_list,
        "total_score_list": template_lists[2],
        "total_victories_list": template_lists[3],
        "winners_list": winner_list,
        "message": len(winner_list),
    }

    return render(request, 'result/result_details.html', context)
