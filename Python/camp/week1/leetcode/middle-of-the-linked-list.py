# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        traverse = head
        count = 0
        while traverse:
            traverse = traverse.next
            count +=1
        print(count)
        
        for i in range(count//2):
            head = head.next

        return head


