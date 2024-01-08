class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        j,i=len(nums)-1, 0
        maxim=0
        while i<j:
            if nums[i]+nums[j]==k:
                maxim+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            else:
                j-=1
        return maxim
                