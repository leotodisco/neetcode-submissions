class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
                total += a + b
            elif op == "C":
                total-= stack.pop()
            elif op == "D":
                a = stack[-1]
                stack.append(a*2)
                total+=a*2
            else:
                stack.append(int(op))
                total+=int(op)
        
        return total

        