class MinStack:

    def __init__(self):
        self.minval = float("inf")
        self.stack = []
        

    def push(self, val: int) -> None:
        self.minval = min(val, self.minval)

        self.stack.append(val)

        

    def pop(self) -> None:
        n = self.stack.pop()

        if self.stack and n not in self.stack:
            self.minval = min(self.stack)        
        else:
            if not self.stack:
                self.minval = float("inf")

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval
        
