class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * (2*nums_len)

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+nums_len] = n

        return ans