
class ListNode:
    def __init__(self, val: int = None, nxt: ListNode = None):
        self.val = val
        self.nxt = nxt

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        

    def get(self, index: int) -> int:
        curr = self.head.nxt
        for i in range(index):
            if not curr:
                return -1
            curr = curr.nxt
            
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.nxt)
        self.head.nxt = newNode
        

    def addAtTail(self, val: int) -> None:
        curr = self.head.nxt
        while curr and curr.nxt:
            curr = curr.nxt
        curr.nxt = ListNode(val, None)
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.nxt
        for i in range(index-1):
            curr = curr.nxt
        
        newNode = ListNode(val, curr.nxt)
        if curr:
            curr.nxt = newNode


    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.nxt
        for i in range(index-1):
            curr = curr.nxt
        
        if curr.nxt:
            curr.nxt = curr.nxt.nxt

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)