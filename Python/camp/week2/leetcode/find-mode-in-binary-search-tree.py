# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)

        def traverse(root):
            if not root:
                return 

            modes[root.val] += 1
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        maxMode = max(modes.values())
        
        result = []
        for i, v in modes.items():
            if v == maxMode:
                result.append(i)

        return result