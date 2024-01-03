class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0 
        maxim=0

        for i in range(1,len(flips)+1):
            
            maxim=max(maxim,flips[i-1])
            if maxim==i and flips[i-1]<=maxim:
                count+=1
            
        return count

