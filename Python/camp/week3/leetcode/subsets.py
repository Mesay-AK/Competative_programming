class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = []

        def backtrack(i, arr):
            if i > len(nums):
                return
            power.append(arr[:])

            for j in range(i, len(nums)):
                
                arr.append(nums[j])
                backtrack(j+1, arr)  
                arr.pop()          

        backtrack(0, [])
        return power