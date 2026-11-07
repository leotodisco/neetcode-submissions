# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        dummy = ListNode(0, head)

        while curr and curr.next:
            if curr == dummy:
                return True
            curr = curr.next.next
            dummy = dummy.next

        
        return False
        