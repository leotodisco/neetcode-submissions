class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0)=0, sqrt(1)=1

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1

        # right è floor(sqrt(x)) in questo schema
        return right