class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0 # i is for s, j is for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1

        
        return i == len(s)