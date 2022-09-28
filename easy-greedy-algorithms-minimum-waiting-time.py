# Solution 1
def minimumWaitingTime(queries):
    queries.sort()
    waitingTime = 0
    for i, x in enumerate(queries):
        queriesLeft = len(queries) - (i + 1)
        waitingTime += x * queriesLeft
    return waitingTime
