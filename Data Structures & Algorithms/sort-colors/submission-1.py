class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for n in nums:
            if n == 0:
                buckets[0]+=1
            elif n == 1:
                buckets[1]+=1
            else:
                buckets[2]+=1
        

        k = 0
        for i in range(len(buckets)):
            for j in range(buckets[i]):
                nums[k] = i
                k += 1
        