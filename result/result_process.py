# coding: utf-8
import numpy as np


def create_ballots_list(votes_list):
    ballots_list = []
    for vote in votes_list:
        if vote.ballot == "0":
            vote.delete()
        else:
            vote_ballot = vote.ballot
            vote_ballot = vote_ballot.replace(
                "[", "").replace(
                    "]", "").replace(
                        "'", "").replace(" ", "")
            vote_ballot = vote_ballot.split(',')
            new_ballot = []
            for element in vote_ballot:
                if vote_ballot.index(element) % 2:
                    new_ballot.append(int(element))
            ballots_list.append(new_ballot)
    return ballots_list


def create_table(n_candidates):
    """[Creaye a zeros matrix sized n_candidates*n_candidates
    that wil be used to store vote's results.]

    Args:
        n_candidates ([int]): [number of candidates]

    Returns:
        [matrix]: [zeros matrix sized n_candidates*n_candidates ]
    """
    vote_matrix = np.zeros(shape=(n_candidates, n_candidates))
    return vote_matrix


def calculate_duals(vote, vote_matrix):
    """[calculate from all ballots the numbers of victories for
    candidates vs each others.]

    Args:
        vote ([list]): [list of all ballots]
        vote_matrix ([numpy matrix]): [zeros matrix with rows:candidates
        and column: adversaries]

    Returns:
        [matrix]: [matrix of candidates scores vs other each candidates]
    """
    candidate_rank = 0
    for candidate in vote[:-2]:
        challenger_rank = candidate_rank + 1
        for challenger in vote[(candidate_rank+1):]:
            if candidate < challenger:
                vote_matrix[candidate_rank, challenger_rank] += 1
                vote_matrix[challenger_rank, candidate_rank] -= 1

            elif candidate > challenger:
                vote_matrix[candidate_rank, challenger_rank] -= 1
                vote_matrix[challenger_rank, candidate_rank] += 1

            elif candidate == challenger:
                vote_matrix[challenger_rank, candidate_rank] += 0
                vote_matrix[candidate_rank, challenger_rank] -= 0
            challenger_rank += 1
        candidate_rank += 1
    return (vote_matrix)


def calculate_victories(vote_matrix):
    """[Recalculate the vote_matrix to give the general result of each
    dual for candidates vs each others.
    1=victory, 0=equality, -1=defeat ]

    Args:
        vote_matrix ([matrix]): [matrix of candidates scores vs other
        each candidates]

    Returns:
        [matrix]: [matrix of candidates victories vs each others]
    """
    victories_matrix = np.copy(vote_matrix)
    victories_matrix[victories_matrix < 0] = -1
    victories_matrix[victories_matrix > 0] = 1
    return victories_matrix


def calculate_winner(victories_matrix, vote_matrix):
    """[Calculate the list of winners from the number of their
    victories ]
    Args:
        victories_matrix ([matrix]): [matrix of candidates
                                    victories vs each others]
        vote_matrix ([matrix]): [matrix of candidates scores vs each others]

    Returns:
        [list]: [list of tupples. Each tupple give
        (number of victories,candidate-number,
        candidate-score) for each winner.]
    """
    winner_list = []
    result_list = []

    victories_matrix = victories_matrix.tolist()
    for row in victories_matrix:
        candidate_score = row.count(1)
        result_list.append(candidate_score)
    if result_list:
        winner_score = max(result_list)

    for rank, score in enumerate(result_list):
        if score == winner_score:
            total_votes = sum(vote_matrix[rank])
            winner_list.append([int(score), int(rank), int(total_votes)])
    winner_list = sorted(winner_list, key=lambda column: column[2])

    return(winner_list)


def candidates_duals(votes_list, n_candidates):
    """[Main function that rules the calculation of the result
    for Condorcet vote  from the ballots list.]

    Args:
        vote_list ([list]): [list of all ballots]
        n_candidates ([int]): [number of candidates]

    Returns:
        [matrix]: [matrix of candidates scores vs each others]
        [matrix]: [matrix of candidates victories vs each others]
        [list]: [list of tupples. Each tupple give
        (number of victories,candidate-number,
        candidate-score) for each winner.]
    """

    vote_matrix = create_table(n_candidates)
    ballots_list = create_ballots_list(votes_list)
    for vote in ballots_list:
        vote_matrix = calculate_duals(vote, vote_matrix)
    victories_matrix = calculate_victories(vote_matrix)
    winner_list = calculate_winner(victories_matrix, vote_matrix)

    return vote_matrix, victories_matrix, winner_list


def lists_for_template(victories_matrix, vote_matrix, candidates_names_list):
    """Function that rules transform matrix to list
    and add candidate's names.
    It also convert numéric result in letters.

    Args:
        vote_list ([list]): [list of all ballots]
        n_candidates ([int]): [number of candidates]

    Returns:
        [list]: [List of lists. Each list give
        dual result vs each winner.]
        [list]: [List of lists. Each list give
        score of a candidate vs each others.]
        [list]: [List of total score for each
        candidate.]
    """

    victories_matrix = victories_matrix.tolist()
    for element in victories_matrix:
        candidate_name = candidates_names_list[victories_matrix.index(element)]
        element.insert(0, candidate_name)

    victories_list = []
    for row in victories_matrix:
        victories_list_element = []
        for element in row:
            if element == 1:
                victories_list_element.append('V')
            elif element == 0:
                victories_list_element.append('N')
            elif element == -1:
                victories_list_element.append('D')
            else:
                victories_list_element.append(element)
        victories_list.append(victories_list_element)

    total_victories_list = []
    for row in victories_list:
        total_victories_list.append(row.count('V'))

    vote_list = vote_matrix.tolist()
    total_score_list = []
    for element in vote_list:
        total_score_list.append(sum(element))
        candidate_name = candidates_names_list[vote_list.index(element)]
        element.insert(0, candidate_name)

    return victories_list, vote_list, total_score_list, total_victories_list
