class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l]) # vuol dire che l'array è ordinato e basta prendere elemento a sx
                break

            mid=(l+r)//2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]: 
                # questo vuol dire che sono nella porzione ordinata a sinistra 
                # ed essendo l'array rotato troverò il minimo a destra
                l = mid+1
            else:
                # sono nella porzione ordinata a destra
                # elementi più piccoli POSSONO essere solo a sinistra
                # poichè a r+1 dovrò avere per forza elementi più grandi
                r = mid-1


        return res