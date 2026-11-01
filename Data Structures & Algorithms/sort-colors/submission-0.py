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
        
        print(buckets)
        for i in range(buckets[0]):
            nums[i] = 0

        for i in range(buckets[0], buckets[0]+buckets[1]):
            nums[i] = 1

        for i in range(buckets[0]+ buckets[1],buckets[0]+ buckets[1]+buckets[2]):
            nums[i] = 2