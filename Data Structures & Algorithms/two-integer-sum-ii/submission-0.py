class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            tmp_sum = numbers[l] + numbers[r]
            if tmp_sum == target:
                return [l+1,r+1]
            if tmp_sum > target:
                r -=1
            if tmp_sum < target:
                l+=1
        
        return [l+1, r+1]