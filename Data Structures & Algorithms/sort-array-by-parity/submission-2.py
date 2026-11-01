class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenIndex=0 # prima posizione in cui mettere il prossimo numero pari
        curr=0 # indice attuale, non so se pari o dispari ma so che se è pari devo swappare con evenIndex

        while curr < len(nums):
            if nums[curr]%2==0:
                nums[evenIndex], nums[curr] = nums[curr], nums[evenIndex]
                evenIndex+=1
            curr+=1

        return nums   