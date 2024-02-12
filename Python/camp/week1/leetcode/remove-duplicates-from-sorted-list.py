# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        first = head
        second = head.next

        while second:
            if first.val == second.val:
                first.next = second.next
                second = second.next
            else:
                first = first.next
                second = second.next

        return head

            
