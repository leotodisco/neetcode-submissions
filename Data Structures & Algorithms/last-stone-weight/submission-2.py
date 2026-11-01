import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stoneX = heapq.heappop(stones)
            stoneY = heapq.heappop(stones)
            
            if stoneX != stoneY:
                heapq.heappush(stones, stoneX - stoneY)
        
        return 0 if not stones else -stones[0]
        
            
        

        