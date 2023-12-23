class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        answer = r = 0
        
        while r < rows - 2:
            i = 0
            j = 2
            
            currSumL1 = sum(grid[r][0: 3])
            l2 = grid[r + 1][i + 1]
            currSumL3 = sum(grid[r + 2][0: 3])
            answer = max(answer, currSumL1 + l2 + currSumL3)
            
            while j < cols - 1:
                j += 1
                currSumL1 = currSumL1 + grid[r][j] - grid[r][i]
                currSumL3 = currSumL3 + grid[r + 2][j] - grid[r + 2][i]
                i += 1
                l2 = grid[r + 1][i + 1]
                answer = max(answer, currSumL1 + l2 + currSumL3)
            
            r += 1
        
        return answer