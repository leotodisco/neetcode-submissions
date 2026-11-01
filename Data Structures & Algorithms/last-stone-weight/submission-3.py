import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1: 
            stoneX = heapq.heappop(stones) 
            stoneY = heapq.heappop(stones) 
            
            if stoneY == stoneX: 
                continue 
            
            elif stoneX < stoneY: 
                stoneY = stoneX - stoneY
                heapq.heappush(stones, stoneY)
        
        return 0 if not stones else abs(stones[0])
        
            
        

        