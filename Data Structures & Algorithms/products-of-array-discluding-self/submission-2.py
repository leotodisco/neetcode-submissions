class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = 1
        suffixes = 1
        res = [1]*len(nums)
        
        for i in range(1, len(nums)):
            prefixes = prefixes * nums[i-1]
            res[i] = prefixes

        for i in range(len(nums)-2, -1, -1):
            suffixes = suffixes * nums[i+1]
            res[i] *= suffixes
        

        return res