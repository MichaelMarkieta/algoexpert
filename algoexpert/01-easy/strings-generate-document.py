# Solution 1
def generateDocument(characters, document):

    charsDict = dict()
    docDict = dict()
    
    for i, x in enumerate(characters):
        charsDict[ord(x)] = charsDict.get(ord(x), 1) + 1
    for i, x in enumerate(document):
        docDict[ord(x)] = docDict.get(ord(x), 1) + 1
    
    for x in docDict.keys():
        if x not in charsDict:
            return False
        if charsDict[x] < docDict[x]:
            return False
    
    return True
