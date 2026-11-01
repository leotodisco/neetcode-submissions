class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0]*len(digits)
        carry = 0

        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                res[i] = (digits[i]+1) % 10
                carry = (digits[i]+1)//10
            else:
                res[i] = (digits[i]+carry)%10
                carry = (digits[i]+carry)//10

        if carry:
            return [1] + res
        
        return res

        
        


