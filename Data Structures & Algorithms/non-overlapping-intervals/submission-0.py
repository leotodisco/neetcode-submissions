class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        res = 0
        oldE = intervals[0][1]

        for i in range(1, len(intervals)):
            newS, newE = intervals[i]

            if newS < oldE:
                res += 1
                oldE = min(oldE, newE)
            else:
                oldE = newE
        
        return res