# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            #initial pointers
            nextPair = current.next.next
            secondNode = current.next

            #swap nodes
            current.next = nextPair
            secondNode.next = current
            prev.next = secondNode

            #update pointers
            prev = current
            current = nextPair
            
        return dummy.next
        