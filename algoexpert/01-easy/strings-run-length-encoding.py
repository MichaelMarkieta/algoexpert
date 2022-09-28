# Solution 1
def runLengthEncoding(string):
    rle = dict()
    for i, x in enumerate(string):
        rle[x] = rle.get(x, 1) + 1
    rlestring = [item for sublist in zip(rle.values(), rle.keys()) for item in sublist]
    rlestring = map(str, rlestring)
    rlestring = "".join(rlestring)
    return rlestring


# Solution 2
def runLengthEncoding(string):
    rle = ""
    countChar = 0
    lastChar = ord(string[0])

    for i, x in enumerate(string):
        if ord(x) != lastChar:
            rle += str(countChar)
            rle += chr(lastChar)
            countChar = 1
            lastChar = ord(x)
        else:
            countChar += 1

        if countChar == 9:
            rle += str(countChar)
            rle += chr(lastChar)
            countChar = 0
            lastChar = ord(string[i + 1])

    rle += str(countChar)
    rle += chr(lastChar)

    return rle
