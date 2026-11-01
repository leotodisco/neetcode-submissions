class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for i in range(len(intervals)):
            oldStart, oldEnd = res[-1]
            newStart, newEnd = intervals[i]
            if newStart <= oldEnd:
                res[-1][1] = max(oldEnd, newEnd)
            else:
                res.append(intervals[i])
        
        return res

