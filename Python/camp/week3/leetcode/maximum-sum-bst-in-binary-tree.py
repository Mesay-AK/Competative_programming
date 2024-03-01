# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        self.maxim = 0

        def findmax(root):

            if not root:
                return -float('inf'), float('inf'), True, 0

            maxim_, mnl, bool_l , curr1_ = findmax( root.left ) 
            mxr, minim_ , bool_r , curr2_ = findmax(root.right )

            if maxim_ < root.val < minim_ and bool_l and bool_r:

                curr_ = root.val + curr1_ + curr2_
                
                maxim = max(mxr, root.val)
                minim = min(mnl, root.val)

                self.maxim = max(curr_, self.maxim)
                
                return maxim, minim, True, curr_

            return -float('inf'), float('inf'), False, 0

        
        findmax(root)

        return self.maxim

