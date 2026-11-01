import heapq

class Solution:
    def maxDifference(self, s: str) -> int:
        mp = dict()
        for c in s:
            currentN = mp.get(c, 0)
            mp[c] = currentN+1
        
        vals = list(mp.values())
        print(vals)

        maxVals = [-v for v in vals]
        heapq.heapify(maxVals)
        
        maxVal = abs(heapq.heappop(maxVals))
        while maxVal%2==0:
            maxVal = abs(heapq.heappop(maxVals))
        
        heapq.heapify(vals)
        minVal = heapq.heappop(vals)
        while minVal%2!=0:
            minVal = heapq.heappop(vals)
        return maxVal-minVal


        