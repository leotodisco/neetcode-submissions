class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ci sono al più due elementi che possono ocmparire più di n/3 volte
        num1 = None
        num2 = None
        counter1 = 0
        counter2 = 0

        for num in nums:
            if num == num1:
                counter1 += 1
            elif num == num2:
                counter2 += 1
            elif counter1 == 0:
                num1 = num
                counter1 = 1
            elif counter2 == 0:
                num2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1

        # 2° passaggio: verifica reale frequenza
        counter1 = counter2 = 0
        for num in nums:
            if num == num1:
                counter1 += 1
            elif num == num2:
                counter2 += 1
        res = []
        n = len(nums)
        if counter1 > n // 3:
            res.append(num1)
        if counter2 > n // 3:
            res.append(num2)

        return res


            
        