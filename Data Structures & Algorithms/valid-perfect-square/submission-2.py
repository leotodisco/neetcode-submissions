class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        for i in range(num//2):
            if i**2 == num:
                return True
        
        return False