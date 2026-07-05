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
        res = [root.val]
        while queue:
            level_size = len(queue)
            summ = 0
            nodes = 0
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    summ += node.left.val
                    nodes += 1
                if node.right:
                    queue.append(node.right)
                    summ += node.right.val
                    nodes += 1
            if nodes > 0:
                res.append(summ / float(nodes))
        return res
        