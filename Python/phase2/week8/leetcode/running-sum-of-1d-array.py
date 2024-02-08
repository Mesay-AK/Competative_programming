class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        total = nums[0]
        ans[0] = total

        for n in range(1,len(nums)):
            total = total + nums[n]
            ans[n] = total

        return ans