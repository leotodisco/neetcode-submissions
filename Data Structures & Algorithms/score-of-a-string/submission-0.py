class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []
        for i in range(1, len(s)):
            scores.append(abs(ord(s[i])-ord(s[i-1])))
            
        return sum(scores)