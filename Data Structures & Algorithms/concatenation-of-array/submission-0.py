class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [n for n in nums]
        ans.extend(nums)
        return ans