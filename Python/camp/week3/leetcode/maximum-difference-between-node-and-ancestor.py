# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def traverse(root , curr_min, curr_max):
            if not root:
                return 

            self.result = max(abs(curr_min - root.val), abs(curr_max- root.val), self.result)

            max_ = max(curr_max, root.val)
            min_ = min(curr_min, root.val)

            traverse(root.left, min_, max_) 
            traverse(root.right, min_, max_)

        traverse(root, root.val, root.val)
        return self.result