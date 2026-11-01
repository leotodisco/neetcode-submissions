class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        x = None
        for i in range(len(self.q1)-1):
            x = self.q1[0]
            self.q1 = self.q1[1:]
            self.q2.append(x)
        val = self.q1.pop()
        self.q1 = [x for x in self.q2]
        self.q2 = []
        return val
        

    def top(self) -> int:
        for i in range(len(self.q1)-1):
            x = self.q1[0]
            self.q1 = self.q1[1:]
            self.q2.append(x)
        numTop = self.q1[-1]
        self.q1 = [x for x in self.q2] 
        self.q2 = []
        self.q1.append(numTop)

        return numTop


        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()