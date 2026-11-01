class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(st: str):
            return st[::-1] == st

        l=0
        r=len(s)-1
        s = s.lower()
        while l<r:
            if s[l] != s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            
            l+=1
            r-=1
        return True
        