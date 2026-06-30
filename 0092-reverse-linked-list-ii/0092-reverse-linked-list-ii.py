# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = head
        for i in range(left - 1):
            p1 = p1.next
        for i in range(right - 1):
            p2 = p2.next
        right_head = p2.next
        middle_head = p1.next
        # print("middle head at now", middle_head)
        p1.next = None # unlink p1
        p2.next = None # unlink p2
        # now reverse middle
        prev = None
        curr = middle_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # now join them in order
        p1.next = prev
        # prev.next = right_head
        reversed_head = prev
        while reversed_head and reversed_head.next:
            reversed_head = reversed_head.next
        reversed_head.next = right_head
    
        return dummy.next

        