# coding: utf-8
"""Define global variables
for food_selector APP program.
"""
from django.utils import timezone
import numpy as np

TESTS = {
    "name1": "impossible",
    "name2": "hellfest",
    "school": "impossible2",
    "departement":31,
    "number1": 123,
    "statusCreate":"C",
    "winners":"(0,0,0)",
    "time1":timezone.now(),
    "ballot":"0:0",
    
    "RightStatus": 200,
    "UnfoundStatus": 404,
    "WrongStatus": 302,
}

TESTS2 = {
    "winner_matrix":[(5,0,12)],
    "vote_matrix":np.array(
        [[ 0,  1,  4,  3,  1,  3],
        [-1,  0,  2,  1,  1,  3],
        [-4, -2,  0,  0,  1,  3],
        [-3, -1,  0,  0,  3,  5],
        [-1, -1, -1, -3,  0,  0],
        [-3, -3, -3, -5,  0,  0]]),
    "victories_matrix":np.array(
        [[ 0,  1,  1,  1,  1,  1],
        [-1,  0,  1,  1,  1,  1],
        [-1, -1,  0,  0,  1,  1],
        [-1, -1,  0,  0,  1,  1],
        [-1, -1, -1, -1,  0,  0],
        [-1, -1, -1, -1,  0,  0]])
}

TESTS3 = {
    "StatusCreate": "C",
    "StatusOpen": "O",
    "StatusClose": "E",
}