class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        

        def build(n, arr):
            
            if n == 0:
                return arr
            temp = []
            for i in range(1,len(arr)):
                temp.append(arr[i-1] + arr[i])


            return build(n-1, [1] + temp + [1])

        return build(rowIndex, [1])