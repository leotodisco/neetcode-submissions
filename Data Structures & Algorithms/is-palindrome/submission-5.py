class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalizedS = ''.join([c.lower() for c in s if c.isalnum()])
        l = 0
        r = len(normalizedS)-1

        while l<r:
            if normalizedS[l] != normalizedS[r]:
                return False
            l+=1
            r-=1
        
        return True
        