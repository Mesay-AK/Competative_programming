class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:


        for row in range(len(matrix)+1):
            for col in range(len(matrix[0])+1):
                if row+1 <len(matrix) and col+1 <len(matrix[0]):
                    if matrix[row][col] != matrix[row+1][col+1]:
                        return False
        return True


