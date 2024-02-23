# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == val:
            return root
        if root.val > val:
            root.left = self.searchBST(root.left, val)
            return root.left
        else:
            root.right = self.searchBST(root.right, val)
            return root.right