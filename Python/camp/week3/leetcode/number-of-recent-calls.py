class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.size = 0
        
    def ping(self, t: int) -> int:

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.size -= 1

        self.q.append(t)
        self.size += 1
        
        return self.size
        

        
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)