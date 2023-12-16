class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers={}
        
        for i in range(len(nums)):
            numbers[nums[i]]=i
        
        for item in range(len(nums)):
            found=target-nums[item]
            if found in numbers and numbers[found]!=item:
                return (item,numbers[found])
            
        return []
