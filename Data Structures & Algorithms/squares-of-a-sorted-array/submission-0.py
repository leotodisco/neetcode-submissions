class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [abs(x) for x in nums]
        nums.sort()
        return [n**2 for n in nums]