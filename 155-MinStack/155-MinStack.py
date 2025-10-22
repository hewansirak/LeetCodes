# Last updated: 10/22/2025, 6:45:24 AM
class MinStack:

    def __init__(self):
        self.stack = [] 
        self.MinStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()