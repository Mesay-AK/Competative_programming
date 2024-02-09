class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        print(prefix)

        ans = [0] * n

        for i in range(n):
            first = (i * nums[i]) - prefix[i]
            second = ((n-1-i)*nums[i]) - (prefix[n]-prefix[i+1])
            ans[i] = abs(first) + abs(second)

        return ans