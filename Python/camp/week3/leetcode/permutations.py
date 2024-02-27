class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        track = set()

        N = len(nums)
        
        def backtracking(i, arr):
            if len(arr) == N:
                permutation.append(arr[:])
                return


            for j in range(N):
                if nums[j] not in track:
                    arr.append(nums[j])
                    track.add(nums[j])
                    backtracking(j+1, arr)
                    arr.pop()
                    track.remove(nums[j])
    
        backtracking(0, [])

        return permutation