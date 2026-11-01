class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        substrLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            substrLen = max(substrLen, r-l+1)
        return substrLen