class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        def backtracking(i, arr):
            if k == len(arr):
                result.append(arr[:])
                return 

            if i >= n+1:
                return 

            arr.append(i)
            backtracking(i+1,arr)
            arr.pop()

            backtracking(i+1, arr)

        backtracking(1, [])
        return result