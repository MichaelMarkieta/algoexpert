# Solution 1
def firstNonRepeatingCharacter(string):
    if len(string) == 0:
        return -1
    
    lookup = dict()
    firstIndex = dict()
    
    for i, x in enumerate(string):
        lookup[x] = lookup.get(x, 0) + 1

    for i, x in enumerate(string):
        if lookup[x] == 1:
            return i

    return -1
