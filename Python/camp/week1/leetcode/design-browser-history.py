class BrowserHistory(object):

    def __init__(self, homepage):

        self.home=homepage
        self.stack1=[self.home]
        self.stack2=[]
        

    def visit(self, url):

        self.stack1.append(url)
        while self.stack2:
            self.stack2.pop()

    def back(self, steps):

        for i in range(steps-1,-1,-1):
            if len(self.stack1)>1:
                self.stack2.append(self.stack1.pop())
        return self.stack1[-1]

    def forward(self, steps):

        for i in range(steps):
            if len(self.stack2)>0:
                self.stack1.append(self.stack2.pop())
        return self.stack1[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)