class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idea: max heap e fai k pop
        # usa min heap e fai pop fino a che len > k
        nums = [-n for n in nums]
        heapq.heapify(nums)
        n = 0
        for i in range(k):
            n = heapq.heappop(nums)

        return -n