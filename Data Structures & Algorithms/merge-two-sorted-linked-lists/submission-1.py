# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        while list1 or list2:
            list1Val = list1.val if list1 else float("inf")
            list2Val = list2.val if list2 else float("inf")
            if list1Val > list2Val:
                newNode = ListNode(val=list2Val)
                list2 = list2.next
            else:
                newNode = ListNode(val=list1Val)
                list1 = list1.next
            dummy.next = newNode
            dummy = dummy.next


        return res.next
