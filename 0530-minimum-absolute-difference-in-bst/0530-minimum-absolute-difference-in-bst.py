# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        self.minimum = float("inf")
        self.prev = None
        def inOrderTraverse(root):
            if not root:
                return
            inOrderTraverse(root.left)
            if self.prev is not None:
                self.minimum = min(self.minimum, root.val - self.prev)
            self.prev = root.val
            inOrderTraverse(root.right)
        inOrderTraverse(root)
        return self.minimum
        