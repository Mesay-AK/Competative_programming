class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        total=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                total+=nums[i]
        for i, j in queries:
            if nums[j]%2==0:
                total-=nums[j]
            nums[j]+=i
            if nums[j]%2==0:
                total+=nums[j]
            result.append(total)
        return result
        

       
        
        
        
        
