# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        deq = deque([root] if root else [])

        while deq:
            level = []
            for i in range(len(deq)):
                curr = deq.popleft()
                level.append(curr.val)
                if curr.left:
                    deq.append(curr.left)

                if curr.right:
                    deq.append(curr.right)

            level = reversed(level) if len(result) % 2 else level

            result.append(level)

        return result
