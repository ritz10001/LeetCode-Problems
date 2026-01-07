# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        p1 = head
        p2 = head.next
        
        while p1 and p2:
            while p1 and p2 and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p1.next
        return dummy.next

        