class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                topTemp, topIndex = stack.pop()
                res[topIndex] = index-topIndex

            stack.append([t, index])
        
        return res


                
