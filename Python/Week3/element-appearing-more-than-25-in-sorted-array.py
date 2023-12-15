class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq=defaultdict(int)
        length=len(arr)
        for i in arr:
            freq[i]+=1
            if freq[i]/length>0.25:
                return i
        
        