class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outputStack.pop()

    def peek(self) -> int:
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())

        return self.outputStack[-1]

    def empty(self) -> bool:
        return not self.inputStack and not self.outputStack