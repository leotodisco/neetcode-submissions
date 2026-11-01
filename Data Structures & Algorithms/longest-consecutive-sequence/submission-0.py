class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxlen = 0

        for i in range(len(nums)):
            tmpLen = 1
            if nums[i]-1 not in numsSet:
                while nums[i]+tmpLen in numsSet:
                    tmpLen+=1
            maxlen = max(maxlen, tmpLen)

        return maxlen
            
        