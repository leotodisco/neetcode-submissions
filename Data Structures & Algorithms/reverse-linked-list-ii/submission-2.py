# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = dummy

        i = 0
        for i in range(left-1):
            res.next = head
            head = head.next
            res = res.next

        # find reverse List
        prev = None
        i = left
        while head and i <= right:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            i+=1
        
        while prev:
            res.next = prev
            prev = prev.next
            res = res.next

        #final append
        while head:
            res.next = head
            head = head.next
            res = res.next

        return dummy.next