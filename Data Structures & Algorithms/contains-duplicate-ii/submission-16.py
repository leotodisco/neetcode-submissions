class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if k == 0:
            return False

        for index, n in enumerate(nums):
            if n in window:
                return True

            if len(window) >= k:
                window.remove(nums[index-k])
            window.add(n)
        return False
