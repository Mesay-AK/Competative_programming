class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combine = set()
        arr = []
        self.sum = 0
        
        def backtracking(i):

            if self.sum == target:
                combine.add(tuple(sorted(arr[:])))

            for j in range(i-1, len(candidates)):

                if candidates[j] + self.sum > target: continue
                self.sum += candidates[j]
                arr.append(candidates[j])

                backtracking(j+1)

                self.sum -= candidates[j]
                arr.pop()


        backtracking(0)
        
        return combine
