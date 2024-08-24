# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root == [] or root is None:
            return []
        queue = []
        temp = []
        res = []
        c = 0
        queue.append(root)
        temp.append(root.val)
        res.append([root.val])
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.pop(0)
                temp.pop(0)
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
            if temp != []:
                c += 1
                if c%2 != 0:
                    res.append(copy.deepcopy(temp[::-1]))
                else:
                    res.append(copy.deepcopy(temp))
        return res