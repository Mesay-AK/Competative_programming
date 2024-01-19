class Solution:
    def longestSubarray(self, nums: List[int]) -> int:


        z={}
        left = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i]==0 and len(z)>0:
                longest= max(longest,i-left-1)
                left = z[0] +1 
                z[0]=i
            elif nums[i]==0:
                z[0]=i
        longest= max(longest,i-left)
        return longest
            
                
            