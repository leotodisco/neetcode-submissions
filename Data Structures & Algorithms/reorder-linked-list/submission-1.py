# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        firstHalf = head

        slow=fast=head
        centerIndex = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            centerIndex+=1

        center = slow.next
        slow.next = None
        prev = None
        while center:
            tmp = center.next
            center.next = prev
            prev = center
            center = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return
        