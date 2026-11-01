class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            windowLen = r-l+1
            maxFreq = max(freqs.values())

            while (r - l + 1) - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
