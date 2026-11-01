class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy day
        r = 1
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l=r
            res = max(res, prices[r]-prices[l])

        return res