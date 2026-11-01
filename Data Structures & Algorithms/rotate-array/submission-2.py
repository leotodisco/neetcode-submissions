class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            new_index = (i+k)%len(nums)
            tmp[new_index] = nums[i]
            
        nums[:] = tmp