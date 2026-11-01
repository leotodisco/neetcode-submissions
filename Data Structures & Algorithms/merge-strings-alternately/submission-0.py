class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""
        i = 0
        
        while i < n:
            res += word1[i]
            res += word2[i]
            i+=1
        
        if len(word1) > len(word2):
            res += word1[i:]
        if len(word2) > len(word1):
            res += word2[i:]

        return res