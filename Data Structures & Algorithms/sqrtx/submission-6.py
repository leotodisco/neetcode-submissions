class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        res = 0
        r=x
        while l<=r:
            mid = l + (r - l) // 2
            if mid ** 2 == x:
                return mid
            else:
                if mid ** 2 > x:
                    r = mid - 1
                else:
                    l = mid+ 1
                    res = mid
        
        return res