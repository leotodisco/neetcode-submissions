import heapq

class Solution:
    def maxDifference(self, s: str) -> int:
        res = float("-inf")
        mp = dict()
        for c in s:
            currentN = mp.get(c, 0)
            mp[c] = currentN+1
        
        vals = list(mp.values())

        for odd in vals:
            if odd%2 == 0: continue
            for even in vals:
                if even % 2 == 1: continue
                res = max(res, odd-even)

        return res


        