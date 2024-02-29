# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traversing(left, right):
            if not left and not right:
                return True

            elif (not left or not right):
                return False

            checker = left.val == right.val
            left_side = traversing(left.right, right.left)
            right_side = traversing(left.left, right.right)

            return checker and left_side and right_side

        return traversing(root.left, root.right)