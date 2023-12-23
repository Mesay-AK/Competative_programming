class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for rows in matrix:
            rows.reverse()

        right=len(matrix)-1

        for row in range(len(matrix)):
            left=0
            while left<right:
                matrix[row][left],matrix[len(matrix)-left-1][right] =  matrix[len(matrix)-left-1][right], matrix[row][left]

                left+=1
                

            right-=1

        return matrix 
        
        
        