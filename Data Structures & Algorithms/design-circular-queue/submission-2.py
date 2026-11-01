class Node:
    def __init__(self, val: int = 0, nxt: Node = None, prev:Node = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = None
        self.tail = None
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False

        node = Node(val=value, nxt=None, prev=self.tail)
        self.size += 1
        if not self.front:
            self.front = node

        if not self.tail:
            self.tail =node
        else:
            self.tail.nxt = node
            self.tail = self.tail.nxt

        return True

    def deQueue(self) -> bool:
        if self.size == 1:
            self.front = self.tail = None
            self.size -= 1
            return True

        if not self.front:
            return False
        self.front.prev = None
        self.front = self.front.nxt
        
        self.size -= 1

        return True
        

    def Front(self) -> int:
        if self.front is None:
            return -1
        
        toReturn = self.front.val
        if toReturn is not None:
            return toReturn
        else:
            return -1
        

    def Rear(self) -> int:
        if self.tail is None:
            return -1

        toReturn = self.tail.val
        if toReturn is not None:
            return toReturn
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()