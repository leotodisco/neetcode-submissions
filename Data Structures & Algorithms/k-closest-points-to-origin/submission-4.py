import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []

        for x, y in points:
            dist = (x**2 + y**2)**0.5
            lst.append((dist, x, y))
        
        heapq.heapify(lst)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(lst)
            res.append([x, y])
            k-=1

        return [[x,y] for x, y in res]
        

        