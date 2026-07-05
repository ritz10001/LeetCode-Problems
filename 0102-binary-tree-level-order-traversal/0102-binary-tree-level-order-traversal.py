# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        res = [[root.val]]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    temp.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    queue.append(node.right)
            if temp:
                res.append(temp)
        return res
        


        