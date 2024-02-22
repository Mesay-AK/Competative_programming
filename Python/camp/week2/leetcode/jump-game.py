class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start form the last postion and check if the 

        i = len(nums) - 1
        good = len(nums) - 1
        while i > -1:
            if i + nums[i] >= good:
                good = i
            i -= 1

        if good == 0:
            return True
        return False
