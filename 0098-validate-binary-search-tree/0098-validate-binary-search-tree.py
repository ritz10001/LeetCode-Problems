# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
        def isValidBST(self, root):
            self.arr = []
            def inorder(root):
                if not root:
                    return
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)

            inorder(root)

            for i in range(1, len(self.arr)):
                if self.arr[i] <= self.arr[i-1]:
                    return False
            return True
            
