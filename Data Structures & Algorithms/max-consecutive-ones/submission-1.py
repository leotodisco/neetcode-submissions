class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxCounter = 0
        for n in nums:
            if n == 1:
                counter += 1
                maxCounter = max(counter, maxCounter)
            else:
                counter = 0

        return maxCounter
