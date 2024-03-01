# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def construct(nums):
            if not nums:
                return

            maxim = max(nums)
            root = TreeNode(maxim)

            mid = nums.index(maxim)

            root.left = construct(nums[:mid])
            root.right = construct(nums[mid+1:])

            return root
            

        return construct(nums)

        

    