class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        for i in range(0,l+1):
            if i not in nums:
                return i
