class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        calls = [0] * len(nums)
        for start, end in requests:
            calls[start] += 1
            if end + 1 < len(nums):
                calls[end+1] -= 1 
        
        total = 0
        for idx, val in enumerate(calls):
            total += val
            calls[idx] = total

        calls.sort()
        nums.sort()
        result = 0
        l, r = len(nums) - 1 , len(calls) - 1
        while r > -1:
            result += calls[r] * nums[l]
            l -= 1
            r -= 1
        return result % (10 ** 9 + 7)