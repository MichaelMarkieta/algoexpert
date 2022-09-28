# Solution 1
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphalist = [*alphabet]
    cipher = ""
    
    while key > len(alphalist):
        key = key - len(alphalist)
        
    for x in string:
        idx = alphalist.index(x) + key
        
        if idx < len(alphalist) + key:
            idx = idx - len(alphalist)
        
        cipher += alphalist[idx]
        
    return cipher
