# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd = head
        even = head.next

        curr_odd = odd
        curr_even = even

        while curr_odd.next and curr_even.next:
            curr_odd.next = curr_even.next
            curr_even.next = curr_even.next.next
            
            curr_odd = curr_odd.next
            curr_even = curr_even.next
        curr_odd.next = even

        return odd