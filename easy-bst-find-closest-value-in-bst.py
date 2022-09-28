# Solution 1
def findClosestValueInBst(tree, target):
    closestVal = findClosest(tree, target, tree.value)
    return closestVal

def findClosest(node, target, closestVal):
    while node != None:
        closestVal = node.value if abs(target - node.value) < abs(target - closestVal) else closestVal
        if closestVal == target:
            return closestVal
        direction = "left" if target - node.value < 0 else "right"
        node = getattr(node, direction)
        findClosest(node, target, closestVal)
    return closestVal
    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
