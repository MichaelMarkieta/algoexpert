# Solution 1
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    recursiveSum(root, 0, sums)
    return sums


def recursiveSum(root, currentSum, sums):
    if root is None:
        return

    currentSum += root.value
    if root.left is None and root.right is None:
        sums.append(currentSum)
        return

    recursiveSum(root.left, currentSum, sums)
    recursiveSum(root.right, currentSum, sums)
