class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        l = 0
        r = len(nums)-1
        res_index = len(nums)-1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                arr[res_index] = nums[l]**2
                l+=1
            else:
                arr[res_index] = nums[r]**2
                r-=1
            res_index -= 1
    
        return arr