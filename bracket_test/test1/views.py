from math import log
from venv import create
from django.http import HttpResponse
from django.template import loader
from random import randint
from math import log, ceil
import json
import numpy as np


def index(request):
    template = loader.get_template('myfirst.html')
    bracket = createTournament()
    data = json.dumps({"teams": bracket, "results": []})
    print(json.dumps(data))
    return HttpResponse(template.render({'data': data}))


def createTournament():
    numberOfTeams = randint(2, 64)
    rounds = log(numberOfTeams/2, 2)

    print(numberOfTeams)
    print(rounds)

    bracket = seed(numberOfTeams)

    teams = []
    for x in bracket:
        if(x[1] != 0):
            teams.append(["team " + str(x[0]), "team " + str(x[1])])
        else:
            teams.append(["team " + str(x[0]), None])
    return teams


def seed(n):
    """ returns list of n in standard tournament seed order
    Note that n need not be a power of 2 - 'byes' are returned as zero
    """
    pairings = []
    ol = [1]
    for i in range(ceil(log(n) / log(2))):
        l = 2*len(ol) + 1
        ol = [e if e <= n else 0 for s in [[el, l-el]
                                           for el in ol] for e in s]

    pairings = np.array_split(ol, len(ol)/2)
    return pairings
