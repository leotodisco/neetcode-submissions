class Node:
    def __init__(self, key = 0):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.arr = [Node() for i in range(10**4)]

    def _hashF(self, key: int):
        return key % len(self.arr)

    def add(self, key: int) -> None:
        index = self._hashF(key)
        curr = self.arr[index]

        while curr and curr.next:
            if curr.key == key:
                return
            curr = curr.next

        curr.next = Node(key)
        

    def remove(self, key: int) -> None:
        index = self._hashF(key)
        curr = self.arr[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
        

    def contains(self, key: int) -> bool:
        index = self._hashF(key)
        curr = self.arr[index]
        curr = curr.next

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)