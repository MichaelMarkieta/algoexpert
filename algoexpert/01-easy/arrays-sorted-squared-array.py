# Solution 1
# def sortedSquaredArray(array):
#     squared = list(map(square, array))
#     squared.sort()
#     return squared

# def square(val):
#     return pow(val, 2)
  
# Solution 2
def sortedSquaredArray(array):
    sortedSquared = []

    a = 0
    b = len(array) - 1

    for i, x in enumerate(array):
        if i == len(array):
            sortedSquared.insert(0, pow(array[a], 2))
        elif abs(array[a]) > abs(array[b]):
            sortedSquared.insert(0, pow(array[a], 2))
            a += 1
        else:
            sortedSquared.insert(0, pow(array[b], 2))
            b -= 1
            
    return sortedSquared
