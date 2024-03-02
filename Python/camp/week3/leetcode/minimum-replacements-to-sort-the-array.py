class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        replacements = 0

        replace = nums[-1]
        for i in range(len(nums)-2, -1, -1):

            curr = nums[i]
            remain = (curr + replace - 1) // replace
            replacements += remain - 1
            replace = curr // remain

        return replacements