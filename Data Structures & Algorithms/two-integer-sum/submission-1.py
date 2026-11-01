class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = i
        
        for i in range(len(nums)):
            toSearch = target - nums[i]
            if toSearch in counter.keys():
                j = counter[toSearch]
                if i != j:
                    return [min(i,j), max(i,j)]

        

        