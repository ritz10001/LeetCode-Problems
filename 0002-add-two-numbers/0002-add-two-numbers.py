# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        ll = dummy
        s = 0
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = temp // 10
            ll.next = ListNode(temp % 10)
            ll = ll.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = l1.val + carry
            carry = temp // 10
            ll.next = ListNode(temp % 10)
            ll = ll.next
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            carry = temp // 10
            ll.next = ListNode(temp % 10)
            ll = ll.next
            l2 = l2.next
        if carry > 0:
            ll.next = ListNode(carry)

        return dummy.next

