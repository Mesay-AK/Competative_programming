class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, maxim = 0, 0

        for i in range(len(nums)):
            k -= (1- nums[i])

            if k < 0:
                k += (1 - nums[left])
                left += 1
            maxim = max(maxim, i-left+1)

        return maxim