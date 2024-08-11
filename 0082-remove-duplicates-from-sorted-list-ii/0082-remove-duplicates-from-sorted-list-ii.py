# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = head, dummy
        while p1:
            if p1.next and p1.val == p1.next.val:
                while p1.next and p1.val == p1.next.val:
                    p1 = p1.next
                p2.next = p1.next
            else:  
                p2 = p2.next
            p1 = p1.next
                
        return dummy.next
        