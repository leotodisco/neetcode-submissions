import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        
        for x,y in points:
            d = (x**2 + y**2)**0.5
            heap.append((d, (x,y)))

        heapq.heapify(heap)
        
        for i in range(k):
            d, point = heapq.heappop(heap)
            res.append([point[0], point[1]])

        return res