class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(s):
            return s==s[::-1]
        normalized = ''.join([x.lower() for x in s if x.isalnum()])
        l=0
        r=len(normalized)-1

        while l<=r:
            if normalized[l] != normalized[r]:
                return isPal(normalized[l+1:r+1]) or isPal(normalized[l:r])

            l=l+1
            r=r-1
        
        return True