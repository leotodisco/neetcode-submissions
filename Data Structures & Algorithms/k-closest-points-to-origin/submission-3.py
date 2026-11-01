import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []

        for x, y in points:
            dist = (x**2 + y**2)**0.5
            lst.append((-dist, x, y))
        
        heapq.heapify(lst)
        while len(lst) > k:
            heapq.heappop(lst)

        return [[x,y] for _, x, y in lst]
        

        