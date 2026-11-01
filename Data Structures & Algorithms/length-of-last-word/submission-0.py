class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = [w for w in s.split(" ")]
        return len(words[-1])