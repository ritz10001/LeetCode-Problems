# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isValidBST(self, root):
        queue = deque([(root, -float("inf"), float("inf"))])
        while queue:
            node, left, right = queue.popleft()
            if not left < node.val < right:
                return False
            if node.left:
                queue.append([node.left, left, node.val])
            if node.right:
                queue.append([node.right, node.val, right])
        return True