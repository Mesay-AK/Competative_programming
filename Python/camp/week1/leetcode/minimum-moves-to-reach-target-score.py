class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles:
            if target %2:
                target -= 1
                moves += 1
            
            target /= 2
            maxDoubles -= 1
            moves += 1

        if target:
            moves += target - 1

        return int(moves)
            

