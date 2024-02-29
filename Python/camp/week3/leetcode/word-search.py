class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols, length = len(board), len(board[0]), len(word)
        track = set()
        # result = [[0] * cols for r in range(rows)]

        def backtracking(i, r, c):

            if length == i:
                return True

            elif r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            elif board[r][c] != word[i]:
                return False

            elif (r,c) in track:
                return False

            track.add((r,c))


            up = backtracking(i + 1, r-1, c)
            down = backtracking(i + 1, r+1, c )
            left = backtracking(i + 1, r, c-1)
            right = backtracking(i + 1, r, c+1)

            
            result = up or down or left or right

            track.remove((r,c))

            return result

        backtracking(0, 0, 0)
        
        for i in range(rows):
            for j in range(cols):
                if backtracking(0, i, j):
                    return True
                

        # return False



