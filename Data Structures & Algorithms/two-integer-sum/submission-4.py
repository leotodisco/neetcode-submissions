class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {k: index for index, k in enumerate(nums)}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hm.keys() and index != hm[target - num]:
                return [min(hm[complement], index), max(hm[complement], index)]
        
        return []