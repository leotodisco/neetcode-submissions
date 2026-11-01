class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterMap = {}
        monotonicStack = []

        for i, n in enumerate(nums2):
            while monotonicStack and nums2[monotonicStack[-1]] < n:
                v = monotonicStack.pop()
                nextGreaterMap[nums2[v]] = n
            monotonicStack.append(i)
        
        for x in nums2:
            if x not in nextGreaterMap:
                nextGreaterMap[x]=-1 
            

        return [nextGreaterMap[n] for n in nums1]