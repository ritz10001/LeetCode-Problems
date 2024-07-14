# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


        dummynode = ListNode(0, head)
        right = head
        dummynode.next = head
        left = dummynode
        c = 0

        while (c < n) and right:
            right = right.next
            c += 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummynode.next

        
        
        