# Solution 1
# import re

# def isValidSubsequence(array, sequence):
#     regex = ".*" + ".*".join(list(map(convertToRegexMatch, sequence)))
#     r = re.compile(regex)
#     test = "".join(list(map(str, array)))
#     match = r.match(test)

#     if match:
#         return True
#     else:
#         return False

# def convertToRegexMatch(selector):
#     return f'({selector})'

# Solution 2
def isValidSubsequence(array, sequence):
    currentSequenceIndex = 0
    for i, x in enumerate(array):
        if x == sequence[currentSequenceIndex]:
            currentSequenceIndex += 1
        if currentSequenceIndex == len(sequence):
            return True
    return False
