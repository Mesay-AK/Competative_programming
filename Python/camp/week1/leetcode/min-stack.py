class MinStack:

    def __init__(self):
        
        self.minim = []
        self.stack =[]
    def push(self, val: int) -> None:

        if self.minim:
            temp = min(self.minim[-1],val)
            self.minim.append(temp)
        else:
            self.minim.append(val)
        self.stack.append(val)
            
    def pop(self) -> None:
        self.minim.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minim[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()