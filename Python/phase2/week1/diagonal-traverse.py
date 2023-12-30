class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        ans=[]
        temp=defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                temp[row+col].append(mat[row][col])
        for key in range(len(temp)):
            if key%2:
                ans.extend(temp[key])
            else:
                ans.extend(temp[key][::-1])
        return ans
            
            
            
            
            
            