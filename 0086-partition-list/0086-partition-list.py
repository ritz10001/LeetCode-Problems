# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        dummy = ListNode(0)
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        p1 = small_dummy
        p2 = big_dummy
        curr = head

        while curr:
            if curr.val >= x:
                p2.next = curr
                p2 = p2.next
            else:
                p1.next = curr
                p1 = p1.next
            curr = curr.next
        p2.next = None
        p1.next = big_dummy.next
        dummy.next = small_dummy.next
        return dummy.next

        