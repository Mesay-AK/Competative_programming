# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        def traverse(root, stg):
            
            nonlocal result
            
            if not root:
                return

            stg += str(root.val)
            if not(root.left or root.right):
                result += int(stg)
            
            
            traverse(root.left, stg)
            traverse(root.right, stg)

        traverse(root, '')
        return result