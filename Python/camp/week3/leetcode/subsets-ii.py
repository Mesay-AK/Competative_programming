class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        power = set()
        nums.sort()

        def backtrack(i, arr):
            if i > len(nums):
                return
                
            power.add(tuple(arr[:]))
            for j in range(i, len(nums)):
                
                arr.append(nums[j])
                backtrack(j+1, arr)  
                arr.pop()          

        backtrack(0, [])
        return power