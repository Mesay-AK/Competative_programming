class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                multiple=i*j
                if multiple%k==0 and nums[i]==nums[j]:
                    count+=1
        return count