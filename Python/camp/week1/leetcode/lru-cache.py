class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.vals = {}
        self.nodes = {}
        self.s = 0
        self.cap = capacity
    def get(self, key: int) -> int:
        if key in self.vals:
            if self.tail == self.vals[key]:
                
                return self.vals[key].val
            r = self.vals[key].prev
            f = self.vals[key].next
            self.tail.next = self.vals[key]
            self.tail.next.next = None
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            r.next = f
            f.prev = r
            return self.vals[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        
        if key in self.vals:
            self.vals[key].val = value
            if self.tail == self.vals[key]:
                return 
            r = self.vals[key].prev
            f = self.vals[key].next
            self.tail.next = self.vals[key]
            self.tail.next.next = None
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            r.next = f
            f.prev = r
            
            return

        self.tail.next = ListNode(value,None,self.tail)
        self.tail = self.tail.next
        self.vals[key]=self.tail
        self.nodes[self.tail] = key
        self.s += 1
        if self.s > self.cap:
            self.vals.pop(self.nodes[self.dummy.next])
            self.nodes.pop(self.dummy.next)
            self.dummy.next = self.dummy.next.next
            self.dummy.next.prev=self.dummy
            self.s -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)