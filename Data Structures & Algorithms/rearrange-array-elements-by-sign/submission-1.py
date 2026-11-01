class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [n for n in nums if n >= 0]
        negatives = [n for n in nums if n < 0]
        res = []
        i = 0
        
        while i < len(positives):
            res.append(positives[i])
            res.append(negatives[i])
            i+=1

        return res
        
        
