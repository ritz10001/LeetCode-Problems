# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def checkSymmetry(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2 or node1 and not node2:
                return False
            if node1 and node2 and node1.val != node2.val:
                return False
            return checkSymmetry(node1.left, node2.right) and checkSymmetry(node1.right, node2.left)
        return checkSymmetry(root.left, root.right)
        

    
        
