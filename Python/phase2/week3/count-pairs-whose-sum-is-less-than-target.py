class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=1
        count=0
        while  i < len(nums)-1 :
            if  j < len(nums) and nums[i] + nums[j] < target:
                count+=1
                j+=1
            else:
                i+=1
                j=i+1

            
        return count
        

            