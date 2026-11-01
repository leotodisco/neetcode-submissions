# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(val=0, next=head)
        res = prev

        while head:
            nxt = head.next
            if head.val == val:
                prev.next = nxt
            else:
                prev = head

            head = nxt

        return res.next

        