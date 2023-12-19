class FrequencyTracker:

    def __init__(self):
        self.dict={}
        self.dictf={}
    def add(self, number: int) -> None:
        self.dict[number]=self.dict.get(number,0)+1
        cnt=self.dict[number]
        self.dictf[cnt]=self.dictf.get(cnt,0)+1
        self.dictf[cnt-1]=self.dictf.get(cnt-1,1)-1

    def deleteOne(self, number: int) -> None:
        if(self.dict.get(number,0)!=0):
            self.dict[number]=self.dict.get(number)-1
            cnt=self.dict[number]
            self.dictf[cnt]=self.dictf.get(cnt,0)+1
            self.dictf[cnt+1]=self.dictf.get(cnt+1,1)-1

        

    def hasFrequency(self, frequency: int) -> bool:
        if(self.dictf.get(frequency,0)!=0):return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)