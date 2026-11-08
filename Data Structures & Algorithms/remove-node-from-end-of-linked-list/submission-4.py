# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            curr = curr.next

        toDrop =ListNode(0, head)
        dummy = toDrop
        while curr:
            curr = curr.next
            toDrop = toDrop.next

        toDrop.next = toDrop.next.next
        return dummy.next

