class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for character in word:
            if character not in curr.children:
                curr.children[character] = TrieNode()
            
            curr = curr.children[character]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.root

        for character in word:
            if character not in curr.children:
                return False
            
            curr = curr.children[character]

        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for character in prefix:
            if character not in curr.children:
                return False
            
            curr = curr.children[character]

        return True
        