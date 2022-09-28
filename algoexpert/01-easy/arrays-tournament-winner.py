# Solution 1
# def tournamentWinner(competitions, results):
#     scorecard = dict()

#     for i, x in enumerate(competitions):
#         if results[i] == 1:
#             if x[0] not in scorecard:
#                 scorecard[x[0]] = 3
#             else:
#                 scorecard[x[0]] += 3
#         else:
#             if x[1] not in scorecard:
#                 scorecard[x[1]] = 3
#             else:
#                 scorecard[x[1]] += 3

#     winner = max(scorecard, key=scorecard.get)
#     return winner

# Solution 2
def tournamentWinner(competitions, results):
    scorecard = dict()
    bestTeam = ""
    scorecard[bestTeam] = 0

    for i, x in enumerate(competitions):
        if results[i] == 1:
            if x[0] not in scorecard:
                scorecard[x[0]] = 3
            else:
                scorecard[x[0]] += 3

            if scorecard[x[0]] > scorecard[bestTeam]:
                bestTeam = x[0]
        else:
            if x[1] not in scorecard:
                scorecard[x[1]] = 3
            else:
                scorecard[x[1]] += 3

            if scorecard[x[1]] > scorecard[bestTeam]:
                bestTeam = x[1]

    return bestTeam
