

class MyHashSet:

    def __init__(self):
        self.hashSet = [None]*10000


    def _hash(self, key):
        return key%10000
        

    def add(self, key: int) -> None:
        index = self._hash(key)
        self.hashSet[index] = key
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.hashSet[index] = None

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        if self.hashSet[index] is not None:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)