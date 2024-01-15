class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j=0,0
        total=0
        for i in range(k):
           total+=nums[i]
        maxim=total 
        j=0
        for i in range(k,len(nums)):
           total-=nums[j]
           total+=nums[i]
           
           maxim=max(maxim,total)
           j+=1

        return maxim/k
