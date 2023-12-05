class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maximum=0
        j=0
        while j+2<len(nums):
            if nums[j]<nums[j+1]+nums[j+2]:
                maximum=max(maximum,nums[j]+nums[j+1]+nums[j+2])
                return maximum
            j+=1
        return maximum 
