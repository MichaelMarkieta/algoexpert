# Solution 1
def isPalindrome(string):
    for x in range(len(string)):
        a = string[x]
        b = string[len(string) - x - 1]
        if a != b:
            return False
        if x > len(string) - x - 1:
            break
    return True
