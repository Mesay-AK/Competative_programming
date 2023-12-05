class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        maxim=0
        
        for i in range(1,len(nums)):
            #check the number of preceeding numbers that are greater than thieir successor.
            if nums[i-1]>nums[i]:
                maxim+=1
            #The number of greater predecessors more than one indicates that our result should be false according to our question. 
                if maxim>1:
                    return False
            # In order to check if previously grater number is also larger than upcoming numbers...
                if i < 2 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
