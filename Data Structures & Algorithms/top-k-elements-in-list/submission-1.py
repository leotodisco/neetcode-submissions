class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        buckets = [[] for i in range(len(nums)+1)]

        for n in nums:
            count = hm.get(n, 0)
            count += 1
            hm[n] = count
        
        for num, count in hm.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res




        return res