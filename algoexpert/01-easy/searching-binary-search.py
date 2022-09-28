# Solution 1
import math

def binarySearch(array, target, baseIndex = 0):
    if len(array) == 1:
        return -1 if array[0] != target else baseIndex

    mid = math.floor(len(array)/2)

    if target == array[mid]:
        return baseIndex + mid
    if target < array[mid]:
        baseIndex = binarySearch(array[0:mid], target, baseIndex)
    else:
        baseIndex += mid
        baseIndex = binarySearch(array[mid:], target, baseIndex)
    
    return baseIndex
