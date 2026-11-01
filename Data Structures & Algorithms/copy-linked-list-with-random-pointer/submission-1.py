"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        hm = {}
        curr = head
        while curr:
            hm[curr] = Node(x=curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = hm[curr]
            new.next = hm[curr.next] if curr.next else None
            new.random = hm[curr.random] if curr.random else None
            hm[curr] = new
            curr = curr.next
        
        return hm[head]