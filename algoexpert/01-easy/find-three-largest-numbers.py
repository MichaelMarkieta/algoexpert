# Solution 1
def findThreeLargestNumbers(array):
    neginf = -float("inf")
    top3 = [neginf, neginf, neginf]

    for x in array:
        top3 = replaceIfLarger(x, top3)

    return top3


def replaceIfLarger(replacement, top3):
    top3.insert(0, replacement)

    for i in range(0, len(top3) - 1):
        if top3[i] > top3[i + 1]:
            top3[i], top3[i + 1] = top3[i + 1], top3[i]

    return top3[1:]
