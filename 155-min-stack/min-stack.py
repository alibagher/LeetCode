class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.stackMin:
            self.stackMin = val

        self.stack.append((val, self.stackMin))

    def pop(self) -> None:
        print (self.stack.pop())
        if not self.stack:
            self.stackMin = sys.maxsize
        else:
            self.stackMin = (self.stack[-1])[1]

    def top(self) -> int:
        return (self.stack[-1])[0]

    def getMin(self) -> int:
        print ("getMin: ", self.stack[-1][1], self.stack[-1][1])
        return (self.stack[-1])[1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()