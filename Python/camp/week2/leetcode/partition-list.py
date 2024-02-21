# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        small = ListNode() 
        large = ListNode()
        s = small
        l = large
    
        while head:
            if head.val < x:
                small.next = head
                small = small.next
                head = head.next
                small.next = None

            else:
                large.next = head
                large = large.next
                head = head.next
                large.next = None
            
            
        small.next = l.next
        return s.next