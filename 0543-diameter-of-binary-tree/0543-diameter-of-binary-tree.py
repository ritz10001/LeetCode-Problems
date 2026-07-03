# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        maxDiameter = [0]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxDiameter[0] = max(maxDiameter[0], left + right)
            return 1 + max(left, right)
        dfs(root)
        return maxDiameter[0]