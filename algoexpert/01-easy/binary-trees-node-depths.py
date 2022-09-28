# Solution 1
# def nodeDepths(root):
#     depths = []
#     dfs(root, -1, depths)
#     return sum(depths)

# def dfs(node, depth, depths):
#     depth += 1

#     if node is None:
#         return

#     depths.append(depth)

#     dfs(node.left, depth, depths)
#     dfs(node.right, depth, depths)


# # This is the class of the input binary tree.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# Solution 2
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
