# Solution 1
# def twoNumberSum(array, targetSum):
#     arrayLength = len(array)
#     for i, x in enumerate(array):
#         for y in range(i + 1, arrayLength):
#             sum = x + array[y]
#             if sum == targetSum:
#                 return [x, array[y]]
#     return []

# Solution 2
def twoNumberSum(array, targetSum):
    ht = dict()
    for i, x in enumerate(array):
        ht[x] = None
        y = targetSum - x
        if y in ht and y != x:
            return [x, y]
    return []
