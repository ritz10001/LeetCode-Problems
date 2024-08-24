# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution(object):
    def sumNumbers(self, root):
        return self.preorder(root, 0)
    def preorder(self, root, current_num):
        if not root:
            return 0
        current_num = current_num * 10 + root.val
        if not root.left and not root.right:
            return current_num
        left_sum = self.preorder(root.left, current_num)
        right_sum = self.preorder(root.right, current_num)

        return left_sum + right_sum