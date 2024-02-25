# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        track = defaultdict(list)
        def traverse(root, row, col):

            nonlocal track
            if not root:
                return 
            
            track[col].append([row, root.val])

            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)

        traverse(root, 0, 0)
        
        result = []
        for i, value in sorted(track.items()):
            value.sort(key = lambda x: x[1])
            value.sort()
            curr = [v for r, v in value]
            result.append(curr)

            
        return result

