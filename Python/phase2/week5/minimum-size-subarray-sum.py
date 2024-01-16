class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        minim=len(nums)
        total=0

        left=0
        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                total -= nums[left]
                minim = min(minim, j-left+1)
                left+=1
        
        return minim 
