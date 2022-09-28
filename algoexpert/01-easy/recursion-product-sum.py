# Solution 1
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, sum=0, level=1):

    for x in array:
        if type(x) == list:
            sum += (level + 1) * productSum(x, 0, level + 1)
        else:
            sum += x

    return sum
