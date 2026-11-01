class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=0

        while l < len(nums):
            if nums[l]%2==0:
                nums[r], nums[l] = nums[l], nums[r]
                r+=1
            l+=1

        return nums   