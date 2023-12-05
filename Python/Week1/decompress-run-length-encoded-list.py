class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #create a frequency and value variable to go thruought the array which will be incremented by 2 to have their order in check.
        frequency=0
        value=1
        
        result=[]
        while value<len(nums):
            for frequent in range(nums[frequency]): #appending the value using its frequency
                result.append(nums[value])
            frequency+=2
            value+=2
        return result
        