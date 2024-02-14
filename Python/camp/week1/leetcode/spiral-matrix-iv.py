# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        mat =[[-1] * n  for _ in range(m)]
        curr = head
        start_row, start_col, end_row, end_col = 0, 0, m - 1, n - 1

        while curr:

            for col in range(start_col, end_col + 1):
                if curr:
                    mat[start_row][col] = curr.val
                    curr = curr.next

            start_row += 1

            for row in range(start_row, end_row + 1):
                if curr:
                    mat[row][end_col] = curr.val
                    curr = curr.next

            end_col -= 1

            for col in range(end_col, start_col - 1, -1):
                if curr:
                    mat[end_row][col] = curr.val
                    curr = curr.next
                    
            end_row -= 1

            for row in range(end_row, start_row - 1, -1):
                if curr:
                    mat[row][start_col] = curr.val
                    curr = curr.next
            start_col +=1
        return mat


            

            
                

                

        