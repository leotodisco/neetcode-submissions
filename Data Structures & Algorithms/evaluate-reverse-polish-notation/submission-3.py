import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATIONS = {'+', '-', '/', '*'}

        for i, ch in enumerate(tokens):
            if ch in OPERATIONS:
                op1 = stack.pop()
                op2 = stack.pop()
                if ch == "+":
                    stack.append(op1+op2)
                elif ch == "-":
                    stack.append(op2-op1)
                elif ch == "/":
                    stack.append(int(op2/op1))
                else:
                    stack.append(op2*op1)
            else:
                stack.append(int(ch))
        return stack.pop()