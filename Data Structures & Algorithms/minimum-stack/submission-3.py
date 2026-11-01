class MinStack:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        

    def push(self, value: int) -> None:
        self.input_stack.append(value)
        if not self.output_stack or value <= self.output_stack[-1]:
            self.output_stack.append(value)

    def pop(self) -> None:
        v = self.input_stack.pop()
        if self.output_stack[-1] == v:
            self.output_stack.pop()
        
    def top(self) -> int:
        return self.input_stack[-1]

    def getMin(self) -> int:
        return self.output_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()