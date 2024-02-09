class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * (len(nums)+2)
        suffix = [1] * (len(nums)+2)

        prefix[1]= nums[0]
        suffix[len(prefix)-2] = nums[len(nums)-1]
        r = len(suffix)-3
        for i in range(1,len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
            suffix[r+1] = suffix[r+2] * nums[r]
            r-=1
        suffix[r+1] = suffix[r+2] * nums[r]

        for i in range(len(nums)):
            nums[i] = suffix[i+2] * prefix[i]
                
        return nums