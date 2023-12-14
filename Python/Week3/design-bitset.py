class Bitset:
    def __init__(self, size: int):
            self.ones=set()
            self.zeros=set({*[i for i in range(size)]})
            self.res=[0 for i in range(size)]
    def fix(self, idx: int) -> None:
        if idx in self.zeros:self.zeros.remove(idx)
        self.ones.add(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.ones:self.ones.remove(idx)
        self.zeros.add(idx)

    def flip(self) -> None:
        prev=self.ones
        self.ones=self.zeros        
        self.zeros=prev
    def all(self) -> bool:
    
        return len(self.zeros)==0

    def one(self) -> bool:
        
        return len(self.ones)>0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        for i in self.ones:
            self.res[i]="1"
        for i in self.zeros:
            self.res[i]="0"
        return "".join([i for i in self.res])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()