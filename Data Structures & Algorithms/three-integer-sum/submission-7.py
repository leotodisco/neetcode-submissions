class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for index, n in enumerate(nums):
            complement = -n
            lst = self.twoSum(complement, nums)
            if lst:
                for r in lst:
                    if index not in r:
                        a = r[0]
                        b = r[1]
                        intermediateRes = [nums[index], nums[a], nums[b]]
                        intermediateRes.sort()
                        res.add(tuple(intermediateRes))

        return [list(r) for r in res]

    def twoSum(self, target, lst):
        res = set()
        hashMap = {}

        for i, n in enumerate(lst):
            complement = target - n

            if complement in hashMap:
                res.add((i, hashMap[complement]))

            hashMap[n] = i

        return list(res)
        


