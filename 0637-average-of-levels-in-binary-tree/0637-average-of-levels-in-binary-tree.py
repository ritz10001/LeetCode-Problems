# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_size = len(queue)
            summ = 0
            for i in range(level_size):
                node = queue.popleft()
                summ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(summ / float(level_size))
        return res
        