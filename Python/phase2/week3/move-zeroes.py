class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        for seeker in range(len(nums)):
            if nums[seeker] != 0 and nums[holder] == 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]

            if nums[holder] != 0:
                holder += 1
