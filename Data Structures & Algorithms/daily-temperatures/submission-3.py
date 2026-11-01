class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        res = [0]*len(temperatures)

        for index, num in enumerate(temperatures):
            while monotonic_stack and num > temperatures[monotonic_stack[-1]]:
                old_index = monotonic_stack.pop()
                res[old_index]=index-old_index

            monotonic_stack.append(index)

        return res

        