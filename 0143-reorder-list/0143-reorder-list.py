# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        l1 = head
        l2 = slow
        l1_head = head
        l2_head = slow
        while l1 and l1.next != slow:
            l1 = l1.next
        while l2 and l2.next != fast:
            l2 = l2.next
        # now reverse l2
        prev = None
        curr = l2_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l2_reversed = prev
        # print("here is l1 normal", l1_head)
        # print("here is l2 reversed", l2_reversed)
        # now, alternatively, swap l1 and l2 nodes
        order = 0
        dummy = ListNode(0)
        final = dummy
        while l1_head and l2_reversed:
            if order % 2 == 0:
                final.next = l1_head
                l1_head = l1_head.next
            else:
                final.next = l2_reversed
                l2_reversed = l2_reversed.next
            final = final.next
            order += 1
        return dummy.next

        