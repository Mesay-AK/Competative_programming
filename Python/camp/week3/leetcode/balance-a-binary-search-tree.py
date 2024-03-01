# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        list_ = []

        def order(root):
            if not root:
                return

            order(root.left)
            list_.append(root.val)
            order(root.right)

        def build(left, right, arr):
            if left > right:
                return None

            middle = (left + right)//2

            root = TreeNode(arr[middle])
            root.left = build(left, middle - 1, arr )
            root.right = build(middle + 1,right, arr )

            return root

        order(root)
        return build(0, len(list_) - 1, list_)

