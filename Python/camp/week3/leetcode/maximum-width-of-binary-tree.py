# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return

        q = deque()
        q.append((root, 1))
        maxim = 0

        while q:

            length = len(q)
            maxim = max(maxim, q[-1][-1]-q[0][-1] +1)
            
            for i in range(length):

                curr = q[0][0]
                j = q[0][1]

                if curr.left:
                    q.append((curr.left,2*j))
                if curr.right:
                    q.append((curr.right, 2* j + 1))
            
                q.popleft()

             
        return maxim
            

            






























