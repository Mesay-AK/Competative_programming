class MyStack(object):

    def __init__(self):
        self.queue=[]

    def push(self, x):

        self.queue.append(x)
        

    def pop(self):

        return self.queue.pop()
        
    def top(self):

        return self.queue[-1]
        

    def empty(self):
  
        if len(self.queue)==0:
          return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()