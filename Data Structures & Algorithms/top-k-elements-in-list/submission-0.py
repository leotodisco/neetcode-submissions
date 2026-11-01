class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # keys are nums_values but values are freqs
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # create the buckets
        for key, v in counter.items():
            buckets[v].append(key)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

