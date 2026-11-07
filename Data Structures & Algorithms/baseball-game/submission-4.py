class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o not in ('+', 'D', 'C'):
                stack.append(int(o))
            else:
                if o == 'D':
                    curr = stack[-1]
                    stack.append(curr*2)
                elif o == 'C':
                    stack.pop()
                elif o == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b)
                    stack.append(a)
                    stack.append(a+b)

        return sum(stack)