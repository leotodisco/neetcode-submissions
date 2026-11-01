import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x1, y1 in points:
            distance = math.sqrt((x1)**2 + (y1)**2)
            heapq.heappush(heap, (distance, [x1, y1]))
        
        res = [[x,y] for _, [x, y] in heapq.nsmallest(k, heap)]
        return res

            

