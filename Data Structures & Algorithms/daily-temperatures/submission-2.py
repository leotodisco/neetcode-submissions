class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pairs (val, index)
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                prevIndex, prevVal = stack.pop()
                result[prevIndex] = i-prevIndex

            stack.append((i, temperatures[i]))

        return result
