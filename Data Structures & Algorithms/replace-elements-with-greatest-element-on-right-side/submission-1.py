class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMost = [-1] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            rightMost[i] = max(rightMost[i+1], arr[i+1])
        
        return rightMost