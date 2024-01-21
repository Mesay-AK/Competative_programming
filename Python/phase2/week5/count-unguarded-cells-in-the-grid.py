class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        state = [[0] * n  for i in range(m)]

        grd = 1
        wall = 2
        used = 3

        for x, y in guards:
            state[x][y] = grd

        for x, y in walls:
            state[x][y] = wall

        for i in range(m):
            curr = 0
            for j in range(n):
                if state[i][j] == grd:
                    curr = used
                elif state[i][j] == wall:
                    curr = 0
                elif state[i][j] == 0:
                    if curr == used:
                        state[i][j] = used

        for i in range(m):
            curr = 0
            for j in range(n-1, -1, -1):
                if state[i][j] == grd:
                    curr = used
                elif state[i][j] == wall:
                    curr = 0
                elif state[i][j] == 0:
                    if curr == used:
                        state[i][j] = used

        for j in range(n):
            curr = 0
            for i in range(m):
                if state[i][j] == grd:
                    curr = used
                elif state[i][j] == wall:
                    curr = 0
                elif state[i][j] == 0:
                    if curr == used:
                        state[i][j] = used

        for j in range(n):
            curr = 0
            for i in range(m-1, -1, -1):
                if state[i][j] == grd:
                    curr = used
                elif state[i][j] == wall:
                    curr = 0
                elif state[i][j] == 0:
                    if curr == used:
                        state[i][j] = used
        count = 0
        for i in range(m):
            for j in range(n):
                if state[i][j] == 0:
                    count += 1
        return count


                    



