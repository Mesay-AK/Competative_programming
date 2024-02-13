# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dictionary = {}
        current= head
        index=0
        while current:
            if current not in dictionary:
                dictionary[current] = index
            else:
                return current
            current=current.next
            index =+1
        return None