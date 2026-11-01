import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1*i for i in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            x = abs(heapq.heappop(gifts))
            x = math.floor(x ** 0.5)
            x = x*(-1)
            heapq.heappush(gifts, x)


        return sum([abs(x) for x in gifts])
        