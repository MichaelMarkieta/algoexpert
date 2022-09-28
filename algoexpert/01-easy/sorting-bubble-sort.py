# Solution 1
def bubbleSort(array):
    if len(array) == 1:
        return array

    while True:
        sorted = True
        for i, x in enumerate(array):
            if i == len(array) - 1:
                continue
            
            if array[i] > array[i + 1]:
                a = array[i]
                b = array[i + 1]
                array[i] = b
                array[i + 1] = a
                sorted = False
        if sorted:
            break
    
    return array
