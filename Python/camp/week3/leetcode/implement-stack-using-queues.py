class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        if not self.q1 and not self.q2:
            self.q1.append(x)
        elif not self.q2:
            self.q1.append(x)
        elif not self.q1:
            self.q2.append(x)
        
    def pop(self):
        # print(self.q1, self.q2)
        if self.q1:
            while len(self.q1) >= 2:
                self.q2.append(self.q1.popleft())
            
            popd = self.q1.popleft()
            
        else:
            while len(self.q2) >= 2:
                self.q1.append(self.q2.popleft())
            popd = self.q2.popleft()
            
        return popd
        
    def top(self):
        if self.q1:
            return self.q1[-1]
        
        return self.q2[-1]


    def empty(self):
        return not (self.q1 or self.q2)
  
        

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()