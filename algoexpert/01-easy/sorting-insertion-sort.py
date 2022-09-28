# Solution 1
# def insertionSort(array):
#     sorted = [array[0]]
#     for x in array[1:]:
#         if x > sorted[-1]:
#             sorted.append(x)
#         else:
#             sorted.append(x)
#             for i in range(1, len(sorted)):
#                 if sorted[-i] < sorted[-i - 1]:
#                     sorted[-i], sorted[-i - 1] = sorted[-i - 1], sorted[-i]
#                 else:
#                     break

#     return sorted


# Solution 2
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array
