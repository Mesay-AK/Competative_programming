# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def common(root, m, n):

            if root.val < m.val and root.val< n.val:
                return common(root.right, m, n)
                
            if root.val > m.val and root.val > n.val:
                return common(root.left, m, n)

            return root


        return common(root, p, q)