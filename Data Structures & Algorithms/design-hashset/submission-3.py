class Node:
    def __init__(self, key):
        self.next = None
        self.key = key


class MyHashSet:

    def __init__(self):
        self.maxSize=10000
        self.hashSet = [Node(-1) for _ in range(self.maxSize)] 

    def _hash(self, key):
        return key%self.maxSize

    def add(self, key: int) -> None:
        index = self._hash(key)
        currentNode = self.hashSet[index]
        while currentNode.next:
            if currentNode.next.key == key:
                return
            currentNode = currentNode.next
        
        currentNode.next = Node(key)
        
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        currentNode = self.hashSet[index]
        prev = currentNode
        while currentNode.next:
            if currentNode.next.key == key:
                prev.next = currentNode.next.next
                return
            prev = currentNode
            currentNode = currentNode.next


    def contains(self, key: int) -> bool:
        index = self._hash(key)
        currentNode = self.hashSet[index]
        while currentNode.next:
            if currentNode.next.key == key:
                return True
            currentNode = currentNode.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)