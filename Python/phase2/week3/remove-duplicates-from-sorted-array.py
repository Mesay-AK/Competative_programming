class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        change=1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[change]=nums[i]
                change+=1
           
        return change