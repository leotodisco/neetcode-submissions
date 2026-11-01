class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = [n for n in nums if n >= 0]
        negative_nums = [n for n in nums if n < 0]

        total_size = len(positive_nums) + len(negative_nums)
        result = []

        for i in range(len(positive_nums)):
            result.append(positive_nums[i])
            result.append(negative_nums[i])

        return result
