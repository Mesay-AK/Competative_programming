class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {}
        for idx, num in enumerate(nums):
            my_dict[num] = idx
        for a, b in operations:
            temp = my_dict[a]
            nums[temp] = b
            my_dict[b] = temp
            del my_dict[a]
        return nums
            
        



































        
        # rep_by_dict = dict()  # key replaced by val
        # for a, b in reversed(operations):
        #     if b not in rep_by_dict:
        #         rep_by_dict[a] = b
        #     else:
        #         rep_by_dict[a] = rep_by_dict[b]
        
        # for i in range(len(nums)):
        #     if nums[i] in rep_by_dict:
        #         nums[i] = rep_by_dict[nums[i]]
        
        # return nums
        