# Solution 1
def nonConstructibleChange(coins):
    minChangeCreatable = 0
    coins.sort()
    if len(coins) == 0:
        return minChangeCreatable + 1
    for i, x in enumerate(coins):
        if x > minChangeCreatable + 1:
            return minChangeCreatable + 1
        minChangeCreatable += x
    return minChangeCreatable + 1
