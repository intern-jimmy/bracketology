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
    # bracket = createTournament() # un comment to make random
    teams = getRankings()
    print(teams)
    bracket = babycup(teams)
    roundOne = getRoundOneResults()
    roundTwo = getRoundTwoResults()
    roundThree = getRoundThreeResults()
    roundFour = getRoundFourResults()
    roundFive = getRoundFiveResults()
    championship = getChampionshipResults()
    data = json.dumps({"teams": bracket, "results": [roundOne, roundTwo, roundThree, roundFour, roundFive, championship ]})
    print(json.dumps(data))
    return HttpResponse(template.render({'data': data}))

def multiBracket(request):
    template = loader.get_template('mysecond.html')
    
    """ 
        1. Get ranking
        2. Create the tournament
        3. Split it in half
            a. First tournament on left
            b. Second tournament on right
            c. Finals a thrid tournament
    """
    teamsRanked = getRankings()
    tournamentRoundOne = babycup(teamsRanked)
    half = int(len(tournamentRoundOne) / 2)
    leftBracket = tournamentRoundOne[0:half]
    rightBracket = tournamentRoundOne[half:len(tournamentRoundOne)]
    #round 1 results
    roundOneResults = getRoundOneResults()
    leftR1Result = roundOneResults[0:half]
    rightR1Result = roundOneResults[half:len(roundOneResults)]
    #round 2 results
    roundTwoResults = getRoundTwoResults()
    leftR2Results = roundTwoResults[0:int(len(roundTwoResults)/2)]
    rightR2Results = roundTwoResults[int(len(roundTwoResults)/2):]
    #round 3 results
    roundThreeResults = getRoundThreeResults()
    leftR3Results = roundThreeResults[0:int(len(roundThreeResults)/2)]
    rightR3Results = roundThreeResults[int(len(roundThreeResults)/2):]

    #round 4 results
    roundFourResults = getRoundFourResults()
    leftR4Results = roundFourResults[0:int(len(roundFourResults)/2)]
    rightR4Results = roundFourResults[int(len(roundFourResults)/2):]

    #Round 5 results 
    roundFiveResults = getRoundFiveResults()
    leftR5Results = [[1, 0]]
    rightR5Results = [[0, 1]]

    #Championship Round
    championshipMatchup = ["Pouring", "Franz"]
    results = [[2,1]]

    #Consulation Round
    consulation = ["Guykid", "Kory"]
    results = [[1,2]]

    data = json.dumps({"left": {"teams":leftBracket, "results": [leftR1Result, leftR2Results, leftR3Results, leftR4Results, leftR5Results]}, 
                       "right": {"teams":rightBracket, "results": [rightR1Result, rightR2Results, rightR3Results, rightR4Results, rightR5Results]}, 
                       "championship":{"teams": [championshipMatchup], "results":[[2,1]]}, 
                       "consulation":{"teams": [consulation], "results":[[1, 2]]} 
                    })
    return HttpResponse(template.render({'data': data}))

def vinnyBracket(request):
    template = loader.get_template('vinny.html')
    data = {}
    return HttpResponse(template.render({'data': data}))

def createTournament():
    numberOfTeams = randint(2, 64)

    bracket = seed(numberOfTeams)
    print('maybe?')
    teams = []
    for x in bracket:
        if(x[1] != 0):
            teams.append(["team " + str(x[0]), "team " + str(x[1])])
        else:
            teams.append(["team " + str(x[0]), None])
    return teams

def babycup(teams):
    print("teams: " + str(len(teams)))
    numberOfTeams = len(teams)
    bracket = seed(numberOfTeams)

    matchups = []
    for x in bracket:
        try:
            
            if(x[1] != 0):
                matchups.append([teams[x[0]-1],teams[x[1]-1]])
            else:
                matchups.append([teams[x[0]-1], None])
        except: 
            print('exception')
    return matchups

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

def reseed(n):
    pairings = []

    return pairings

def getRankings():
    return [
        "Pouring","Kory", "Franz", "AP", "GuyKid", "Rapd[adfk]", "MeanMachine",
        "Starbuck","Hope 🔥", "Victor2194", "CryptoGrady", "BoB Nothing", "Sereen | DFK is here to stay",
        "mattypesq", "Mosh", "SgtFilthyMcNasty || Team Goose", "JusticeBeaver04", 
        "K3VO", "aaperon", "Dlay", "Activice", "9dorf", "Itwasntme", "malotru", "ItTolls4Thee",
        "Bolon Soron", "FRI FRI", "Dreaddshots", "zabu 🥔 Valar Morghulis 🥔", 
        "cryptnerd3", "KeepPounding", "DareOevil", "TTSGear", "BraiSto", "Bondosu",
        "erexere", "rock808", "hodl4lyfe", "fooof🍄", "Benforce", "kanjooo", "Luke_Ethwalker",
        "AroundCloud7 || Team Goose", "DixT", "jazcrypto", "JDub"]

def getRoundOneResults():
    return [[None, None], [1, 0], [None, None], [None, None], 
            [None, None], [1, 0], [None, None], [1, 0], 
            [None, None], [0, 1], [None, None], [1, 0],
            [None, None], [0, 1], [None, None], [1, 0],
            [None, None], [1, 0], [None, None], [None, None],
            [None, None], [0, 1], [None, None], [1, 0],
            [None, None], [1, 0], [None, None], [0, 1],
            [None, None], [1, 0], [None, None], [0, 1]]

def getRoundTwoResults():
    return [[1, 0], [1, 0], [0, 1] , [1, 0], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0 ], [1, 0]]

def getRoundThreeResults():
    return[[1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]

def getRoundFourResults():
    return[[1, 0], [0, 1], [1, 0], [1, 0]]

def getRoundFiveResults():
    return[[1, 0], [0, 1]]

def getChampionshipResults():
    return [[2,1], [0, 1]]