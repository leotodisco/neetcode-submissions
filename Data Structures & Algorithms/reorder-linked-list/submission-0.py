# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    # 1 2 3 4 5
    # se trovo il medio 
    # faccio reverse della parte destra
    # leggo una volta a sx e una volta a destra
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge    
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


        
