# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        sum_ = 0

        def ranges(root, low, high):

            nonlocal sum_

            if not root:
                return 0

            if root.val <= high and root.val >=low:
                sum_ += root.val
                print(root.val)

            ranges(root.left, low, high)
            ranges(root.right, low, high)

        ranges(root, low, high)
        return sum_