class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        i = 0
        nums = [0,1]
        while i < n:
            tmp = nums[1]
            nums[1] = tmp+nums[0]
            nums[0] = tmp

            i+=1

        
        return nums[1]


