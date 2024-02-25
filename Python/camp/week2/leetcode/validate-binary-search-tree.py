# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
 
        def checkValid(root, left, right):
            if not root:
                return True

            elif not(left < root.val and right > root.val):
                return False

            left_side = checkValid(root.left, left, root.val)
            right_side = checkValid(root.right, root.val, right)

            return left_side and right_side

        return checkValid(root, -float('inf'), float('inf'))
