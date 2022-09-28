# Solution 1
def selectionSort(array):
    replacing = 0

    while replacing < len(array) - 1:
        smallest = [float("inf"), None]

        for i, x in enumerate(array[replacing:]):
            if x < smallest[0]:
                smallest[0] = x
                smallest[1] = i + replacing

        array[replacing], array[smallest[1]] = smallest[0], array[replacing]
        replacing += 1

    return array
