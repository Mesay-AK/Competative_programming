class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=nums.count(1)
        zeros=0
        result=[]
        score=0
        for i in range(len(nums)):
            score=zeros+ones
            if nums[i]==0:
                zeros+=1
            else:
                ones-=1
            result.append(score)
            
        result.append(zeros+ones)
        
        maxim=max(result)
        ans=[]
        for i in range(len(result)):
            if result[i]==maxim:
                ans.append(i)
        return ans

