class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums={}
        for i in range(len(nums)):
            if nums[0] != val :
                new_nums[i]= nums[0]
            nums.pop(0)
        for i in new_nums.keys():
            nums.append(new_nums[i]) 
            
        return len(nums)