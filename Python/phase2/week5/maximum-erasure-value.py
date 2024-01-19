class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        track={}
        left, total, maxim= 0, 0, 0

        for r in range(len(nums)):
            if nums[r] not in track:
                track[nums[r]] = r
                total += nums[r]
            else:
                while left <= track[nums[r]]:
                    total -= nums[left]
                    left += 1  
                total += nums[r]
                track[nums[r]]=r  
            maxim = max(maxim, total)
            
            
        return maxim

        