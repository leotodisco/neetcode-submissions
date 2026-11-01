class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.next=None




class MyHashMap:

    def __init__(self):
        self.maxSize = 10000
        self.hm = [Node(-1,-1) for _ in range(self.maxSize)]

        
    def hashFunction(self, key):
        return key % self.maxSize


    def put(self, key: int, value: int) -> None:
        index = self.hashFunction(key)
        curr = self.hm[index]

        while curr.next:
            if curr.next.key == key:
                nxt = curr.next.next
                curr.next = Node(key, value)
                curr.next.next = nxt
                return
            curr = curr.next
        
        curr.next = Node(key, value)
        return
        

    def get(self, key: int) -> int:
        index = self.hashFunction(key)
        curr = self.hm[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1

        

    def remove(self, key: int) -> None:
        index = self.hashFunction(key)
        curr = self.hm[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)